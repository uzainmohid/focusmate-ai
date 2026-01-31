from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
import sqlite3
import json
import math

# app = Flask(__name__)
# CORS(app)

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})


# Database setup
def init_db():
    conn = sqlite3.connect('focusmate.db')
    c = conn.cursor()
    
    # Tasks table
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  urgency INTEGER,
                  effort INTEGER,
                  deadline TEXT,
                  completed BOOLEAN DEFAULT 0,
                  created_at TEXT,
                  completed_at TEXT,
                  ai_priority_score REAL)''')
    
    # Focus sessions table
    c.execute('''CREATE TABLE IF NOT EXISTS focus_sessions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  duration INTEGER,
                  start_time TEXT,
                  end_time TEXT,
                  focus_level TEXT,
                  distractions INTEGER DEFAULT 0,
                  completed BOOLEAN DEFAULT 0)''')
    
    # Productivity metrics table
    c.execute('''CREATE TABLE IF NOT EXISTS metrics
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  date TEXT,
                  tasks_completed INTEGER,
                  focus_sessions INTEGER,
                  total_focus_minutes INTEGER,
                  productivity_score REAL,
                  distraction_count INTEGER)''')
    
    conn.commit()
    conn.close()

# AI/ML Logic - Focus Prediction Engine
class FocusPredictionEngine:
    @staticmethod
    def predict_focus_level(time_of_day, session_duration, past_completion_rate):
        """
        Predicts focus level: High, Medium, or Low
        Based on time of day, session duration, and historical performance
        """
        score = 0
        
        # Time of day factor (morning = better focus)
        hour = int(time_of_day.split(':')[0])
        if 8 <= hour <= 11:  # Peak morning hours
            score += 40
        elif 14 <= hour <= 16:  # Post-lunch dip
            score += 20
        elif 17 <= hour <= 20:  # Evening
            score += 30
        else:
            score += 10
        
        # Session duration factor (25-45 min = optimal)
        if 25 <= session_duration <= 45:
            score += 35
        elif session_duration < 25:
            score += 20
        else:
            score += 15  # Too long = fatigue
        
        # Past performance factor
        score += past_completion_rate * 25
        
        # Classify
        if score >= 70:
            return "High"
        elif score >= 45:
            return "Medium"
        else:
            return "Low"
    
    @staticmethod
    def calculate_optimal_break(focus_minutes):
        """Calculate optimal break duration"""
        if focus_minutes <= 25:
            return 5
        elif focus_minutes <= 50:
            return 10
        else:
            return 15

# AI/ML Logic - Task Prioritization Engine
class TaskPrioritizationEngine:
    @staticmethod
    def calculate_priority_score(urgency, effort, deadline_str):
        """
        Calculate AI priority score for tasks
        Score = urgency * 0.4 + deadline_proximity * 0.4 + (1/effort) * 0.2
        """
        # Urgency component (1-5 scale)
        urgency_score = (urgency / 5) * 40
        
        # Deadline proximity component
        if deadline_str:
            try:
                deadline = datetime.fromisoformat(deadline_str)
                now = datetime.now()
                days_until = (deadline - now).days
                
                if days_until < 0:
                    deadline_score = 50  # Overdue
                elif days_until == 0:
                    deadline_score = 45
                elif days_until <= 1:
                    deadline_score = 40
                elif days_until <= 3:
                    deadline_score = 30
                elif days_until <= 7:
                    deadline_score = 20
                else:
                    deadline_score = 10
            except:
                deadline_score = 15
        else:
            deadline_score = 15
        
        # Effort component (inverse - lower effort = higher priority)
        effort_score = ((6 - effort) / 5) * 20
        
        total_score = urgency_score + deadline_score + effort_score
        return round(total_score, 2)
    
    @staticmethod
    def get_smart_recommendations(tasks):
        """Generate AI recommendations based on task analysis"""
        if not tasks:
            return ["Add your first task to get started!", "Break large tasks into smaller chunks"]
        
        recommendations = []
        
        # Check for overdue tasks
        overdue = [t for t in tasks if t.get('deadline') and 
                   datetime.fromisoformat(t['deadline']) < datetime.now() and not t['completed']]
        if overdue:
            recommendations.append(f"⚠️ {len(overdue)} overdue task(s) need immediate attention")
        
        # Check for high-urgency tasks
        urgent = [t for t in tasks if t['urgency'] >= 4 and not t['completed']]
        if urgent:
            recommendations.append(f"🔥 Focus on {len(urgent)} high-urgency task(s) first")
        
        # Check task load
        pending = [t for t in tasks if not t['completed']]
        if len(pending) > 10:
            recommendations.append("📊 Consider breaking down large tasks into smaller chunks")
        elif len(pending) == 0:
            recommendations.append("✨ Great job! All tasks completed. Time to plan ahead.")
        
        # Time-based recommendations
        hour = datetime.now().hour
        if 8 <= hour <= 11:
            recommendations.append("🌅 Morning energy is high - tackle complex tasks now")
        elif 14 <= hour <= 16:
            recommendations.append("☕ Post-lunch dip - consider lighter tasks or a focus session")
        
        return recommendations[:3] if recommendations else ["Keep up the great work! 🚀"]

# AI/ML Logic - Productivity Analytics Engine
class ProductivityAnalytics:
    @staticmethod
    def calculate_productivity_score(tasks_completed, focus_sessions, distractions, total_focus_minutes):
        """
        Calculate daily productivity score (0-100)
        Formula: (tasks*10 + sessions*15 + focus_minutes*0.5) - (distractions*5)
        """
        base_score = (tasks_completed * 10) + (focus_sessions * 15) + (total_focus_minutes * 0.5)
        penalty = distractions * 5
        score = max(0, min(100, base_score - penalty))
        return round(score, 1)
    
    @staticmethod
    def get_productivity_insights(score, tasks_completed, focus_sessions):
        """Generate personalized productivity insights"""
        if score >= 80:
            return "🌟 Exceptional productivity! You're in the zone."
        elif score >= 60:
            return "✅ Solid performance! Keep the momentum going."
        elif score >= 40:
            return "📈 Good progress. Small improvements can boost your score."
        else:
            return "🎯 Let's focus on completing tasks and focus sessions."

# Routes
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "FocusMate AI Backend Running"})

@app.route('/api/tasks', methods=['GET', 'POST'])
def handle_tasks():
    conn = sqlite3.connect('focusmate.db')
    c = conn.cursor()
    
    if request.method == 'GET':
        c.execute('SELECT * FROM tasks ORDER BY ai_priority_score DESC, created_at DESC')
        tasks = []
        for row in c.fetchall():
            tasks.append({
                'id': row[0],
                'title': row[1],
                'urgency': row[2],
                'effort': row[3],
                'deadline': row[4],
                'completed': bool(row[5]),
                'created_at': row[6],
                'completed_at': row[7],
                'ai_priority_score': row[8]
            })
        conn.close()
        return jsonify(tasks)
    
    elif request.method == 'POST':
        data = request.json
        title = data['title']
        urgency = data.get('urgency', 3)
        effort = data.get('effort', 3)
        deadline = data.get('deadline')
        created_at = datetime.now().isoformat()
        
        # Calculate AI priority score
        priority_score = TaskPrioritizationEngine.calculate_priority_score(
            urgency, effort, deadline
        )
        
        c.execute('''INSERT INTO tasks (title, urgency, effort, deadline, created_at, ai_priority_score)
                     VALUES (?, ?, ?, ?, ?, ?)''',
                  (title, urgency, effort, deadline, created_at, priority_score))
        conn.commit()
        task_id = c.lastrowid
        conn.close()
        
        return jsonify({
            'id': task_id,
            'title': title,
            'urgency': urgency,
            'effort': effort,
            'deadline': deadline,
            'completed': False,
            'created_at': created_at,
            'completed_at': None,
            'ai_priority_score': priority_score
        }), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT', 'DELETE'])
def handle_task(task_id):
    conn = sqlite3.connect('focusmate.db')
    c = conn.cursor()
    
    if request.method == 'PUT':
        data = request.json
        
        if 'completed' in data:
            completed = data['completed']
            completed_at = datetime.now().isoformat() if completed else None
            c.execute('UPDATE tasks SET completed = ?, completed_at = ? WHERE id = ?',
                      (completed, completed_at, task_id))
        
        if 'title' in data or 'urgency' in data or 'effort' in data or 'deadline' in data:
            c.execute('SELECT urgency, effort, deadline FROM tasks WHERE id = ?', (task_id,))
            current = c.fetchone()
            
            urgency = data.get('urgency', current[0])
            effort = data.get('effort', current[1])
            deadline = data.get('deadline', current[2])
            
            priority_score = TaskPrioritizationEngine.calculate_priority_score(
                urgency, effort, deadline
            )
            
            c.execute('''UPDATE tasks SET title = ?, urgency = ?, effort = ?, 
                         deadline = ?, ai_priority_score = ? WHERE id = ?''',
                      (data.get('title'), urgency, effort, deadline, priority_score, task_id))
        
        conn.commit()
        conn.close()
        return jsonify({"message": "Task updated"})
    
    elif request.method == 'DELETE':
        c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Task deleted"})

@app.route('/api/focus-sessions', methods=['GET', 'POST'])
def handle_focus_sessions():
    conn = sqlite3.connect('focusmate.db')
    c = conn.cursor()
    
    if request.method == 'GET':
        c.execute('SELECT * FROM focus_sessions ORDER BY start_time DESC LIMIT 10')
        sessions = []
        for row in c.fetchall():
            sessions.append({
                'id': row[0],
                'duration': row[1],
                'start_time': row[2],
                'end_time': row[3],
                'focus_level': row[4],
                'distractions': row[5],
                'completed': bool(row[6])
            })
        conn.close()
        return jsonify(sessions)
    
    elif request.method == 'POST':
        data = request.json
        duration = data['duration']
        start_time = data.get('start_time', datetime.now().isoformat())
        distractions = data.get('distractions', 0)
        completed = data.get('completed', False)
        
        # AI Focus Prediction
        time_of_day = datetime.now().strftime("%H:%M")
        
        # Calculate past completion rate
        c.execute('SELECT COUNT(*) FROM focus_sessions WHERE completed = 1')
        completed_sessions = c.fetchone()[0]
        c.execute('SELECT COUNT(*) FROM focus_sessions')
        total_sessions = c.fetchone()[0]
        completion_rate = completed_sessions / total_sessions if total_sessions > 0 else 0.5
        
        focus_level = FocusPredictionEngine.predict_focus_level(
            time_of_day, duration, completion_rate
        )
        
        end_time = data.get('end_time')
        
        c.execute('''INSERT INTO focus_sessions 
                     (duration, start_time, end_time, focus_level, distractions, completed)
                     VALUES (?, ?, ?, ?, ?, ?)''',
                  (duration, start_time, end_time, focus_level, distractions, completed))
        conn.commit()
        session_id = c.lastrowid
        conn.close()
        
        # Calculate optimal break
        optimal_break = FocusPredictionEngine.calculate_optimal_break(duration)
        
        return jsonify({
            'id': session_id,
            'duration': duration,
            'start_time': start_time,
            'end_time': end_time,
            'focus_level': focus_level,
            'distractions': distractions,
            'completed': completed,
            'optimal_break': optimal_break
        }), 201

@app.route('/api/focus-sessions/<int:session_id>', methods=['PUT'])
def update_focus_session(session_id):
    conn = sqlite3.connect('focusmate.db')
    c = conn.cursor()
    
    data = request.json
    end_time = data.get('end_time', datetime.now().isoformat())
    completed = data.get('completed', True)
    distractions = data.get('distractions', 0)
    
    c.execute('''UPDATE focus_sessions 
                 SET end_time = ?, completed = ?, distractions = ?
                 WHERE id = ?''',
              (end_time, completed, distractions, session_id))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Focus session updated"})

@app.route('/api/dashboard', methods=['GET'])
def get_dashboard():
    conn = sqlite3.connect('focusmate.db')
    c = conn.cursor()
    
    today = datetime.now().date().isoformat()
    
    # Tasks completed today
    c.execute('''SELECT COUNT(*) FROM tasks 
                 WHERE completed = 1 AND DATE(completed_at) = ?''', (today,))
    tasks_completed = c.fetchone()[0]
    
    # Focus sessions today
    c.execute('''SELECT COUNT(*), SUM(duration) FROM focus_sessions 
                 WHERE completed = 1 AND DATE(start_time) = ?''', (today,))
    session_data = c.fetchone()
    focus_sessions = session_data[0]
    total_focus_minutes = session_data[1] or 0
    
    # Total distractions today
    c.execute('''SELECT SUM(distractions) FROM focus_sessions 
                 WHERE DATE(start_time) = ?''', (today,))
    distractions = c.fetchone()[0] or 0
    
    # Calculate productivity score
    productivity_score = ProductivityAnalytics.calculate_productivity_score(
        tasks_completed, focus_sessions, distractions, total_focus_minutes
    )
    
    # Get productivity insight
    productivity_insight = ProductivityAnalytics.get_productivity_insights(
        productivity_score, tasks_completed, focus_sessions
    )
    
    # Get top 3 priority tasks
    c.execute('''SELECT * FROM tasks WHERE completed = 0 
                 ORDER BY ai_priority_score DESC LIMIT 3''')
    top_tasks = []
    for row in c.fetchall():
        top_tasks.append({
            'id': row[0],
            'title': row[1],
            'urgency': row[2],
            'ai_priority_score': row[8]
        })
    
    # Get all pending tasks for recommendations
    c.execute('SELECT * FROM tasks WHERE completed = 0')
    all_pending_tasks = []
    for row in c.fetchall():
        all_pending_tasks.append({
            'id': row[0],
            'title': row[1],
            'urgency': row[2],
            'effort': row[3],
            'deadline': row[4],
            'completed': bool(row[5]),
            'ai_priority_score': row[8]
        })
    
    # Get AI recommendations
    recommendations = TaskPrioritizationEngine.get_smart_recommendations(all_pending_tasks)
    
    # Predict current focus level
    time_of_day = datetime.now().strftime("%H:%M")
    c.execute('SELECT COUNT(*) FROM focus_sessions WHERE completed = 1')
    completed_sessions = c.fetchone()[0]
    c.execute('SELECT COUNT(*) FROM focus_sessions')
    total_sessions = c.fetchone()[0]
    completion_rate = completed_sessions / total_sessions if total_sessions > 0 else 0.5
    
    current_focus = FocusPredictionEngine.predict_focus_level(time_of_day, 30, completion_rate)
    
    conn.close()
    
    return jsonify({
        'productivity_score': productivity_score,
        'productivity_insight': productivity_insight,
        'tasks_completed_today': tasks_completed,
        'focus_sessions_today': focus_sessions,
        'total_focus_minutes': total_focus_minutes,
        'distractions_today': distractions,
        'top_tasks': top_tasks,
        'current_focus_level': current_focus,
        'ai_recommendations': recommendations
    })

@app.route('/api/insights', methods=['GET'])
def get_insights():
    conn = sqlite3.connect('focusmate.db')
    c = conn.cursor()
    
    # Get last 7 days of data
    insights = []
    for i in range(6, -1, -1):
        date = (datetime.now() - timedelta(days=i)).date().isoformat()
        
        c.execute('''SELECT COUNT(*) FROM tasks 
                     WHERE completed = 1 AND DATE(completed_at) = ?''', (date,))
        tasks = c.fetchone()[0]
        
        c.execute('''SELECT COUNT(*), SUM(duration), SUM(distractions) FROM focus_sessions 
                     WHERE completed = 1 AND DATE(start_time) = ?''', (date,))
        session_data = c.fetchone()
        sessions = session_data[0]
        minutes = session_data[1] or 0
        distractions = session_data[2] or 0
        
        score = ProductivityAnalytics.calculate_productivity_score(
            tasks, sessions, distractions, minutes
        )
        
        insights.append({
            'date': date,
            'tasks_completed': tasks,
            'focus_sessions': sessions,
            'focus_minutes': minutes,
            'productivity_score': score,
            'distractions': distractions
        })
    
    conn.close()
    return jsonify(insights)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)

