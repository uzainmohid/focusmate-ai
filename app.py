# # from flask import Flask, request, jsonify
# # from flask_cors import CORS
# # from datetime import datetime, timedelta
# # import sqlite3
# # import os
# # import json
# # import math

# # app = Flask(__name__)
# # CORS(app)

# # # app = Flask(__name__)
# # # CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
# # # app = Flask(__name__)
# # # CORS(app, resources={r"/api/*": {"origins": "https://focuscoach-ai.netlify.app/"}})


# # # Database setup
# # def init_db():
# #     conn = sqlite3.connect('focusmate.db')
# #     c = conn.cursor()
    
# #     # Tasks table
# #     c.execute('''CREATE TABLE IF NOT EXISTS tasks
# #                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                   title TEXT NOT NULL,
# #                   urgency INTEGER,
# #                   effort INTEGER,
# #                   deadline TEXT,
# #                   completed BOOLEAN DEFAULT 0,
# #                   created_at TEXT,
# #                   completed_at TEXT,
# #                   ai_priority_score REAL)''')
    
# #     # Focus sessions table
# #     c.execute('''CREATE TABLE IF NOT EXISTS focus_sessions
# #                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                   duration INTEGER,
# #                   start_time TEXT,
# #                   end_time TEXT,
# #                   focus_level TEXT,
# #                   distractions INTEGER DEFAULT 0,
# #                   completed BOOLEAN DEFAULT 0)''')
    
# #     # Productivity metrics table
# #     c.execute('''CREATE TABLE IF NOT EXISTS metrics
# #                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                   date TEXT,
# #                   tasks_completed INTEGER,
# #                   focus_sessions INTEGER,
# #                   total_focus_minutes INTEGER,
# #                   productivity_score REAL,
# #                   distraction_count INTEGER)''')
    
# #     conn.commit()
# #     conn.close()

# # # AI/ML Logic - Focus Prediction Engine
# # class FocusPredictionEngine:
# #     @staticmethod
# #     def predict_focus_level(time_of_day, session_duration, past_completion_rate):
# #         """
# #         Predicts focus level: High, Medium, or Low
# #         Based on time of day, session duration, and historical performance
# #         """
# #         score = 0
        
# #         # Time of day factor (morning = better focus)
# #         hour = int(time_of_day.split(':')[0])
# #         if 8 <= hour <= 11:  # Peak morning hours
# #             score += 40
# #         elif 14 <= hour <= 16:  # Post-lunch dip
# #             score += 20
# #         elif 17 <= hour <= 20:  # Evening
# #             score += 30
# #         else:
# #             score += 10
        
# #         # Session duration factor (25-45 min = optimal)
# #         if 25 <= session_duration <= 45:
# #             score += 35
# #         elif session_duration < 25:
# #             score += 20
# #         else:
# #             score += 15  # Too long = fatigue
        
# #         # Past performance factor
# #         score += past_completion_rate * 25
        
# #         # Classify
# #         if score >= 70:
# #             return "High"
# #         elif score >= 45:
# #             return "Medium"
# #         else:
# #             return "Low"
    
# #     @staticmethod
# #     def calculate_optimal_break(focus_minutes):
# #         """Calculate optimal break duration"""
# #         if focus_minutes <= 25:
# #             return 5
# #         elif focus_minutes <= 50:
# #             return 10
# #         else:
# #             return 15

# # # AI/ML Logic - Task Prioritization Engine
# # class TaskPrioritizationEngine:
# #     @staticmethod
# #     def calculate_priority_score(urgency, effort, deadline_str):
# #         """
# #         Calculate AI priority score for tasks
# #         Score = urgency * 0.4 + deadline_proximity * 0.4 + (1/effort) * 0.2
# #         """
# #         # Urgency component (1-5 scale)
# #         urgency_score = (urgency / 5) * 40
        
# #         # Deadline proximity component
# #         if deadline_str:
# #             try:
# #                 deadline = datetime.fromisoformat(deadline_str)
# #                 now = datetime.now()
# #                 days_until = (deadline - now).days
                
# #                 if days_until < 0:
# #                     deadline_score = 50  # Overdue
# #                 elif days_until == 0:
# #                     deadline_score = 45
# #                 elif days_until <= 1:
# #                     deadline_score = 40
# #                 elif days_until <= 3:
# #                     deadline_score = 30
# #                 elif days_until <= 7:
# #                     deadline_score = 20
# #                 else:
# #                     deadline_score = 10
# #             except:
# #                 deadline_score = 15
# #         else:
# #             deadline_score = 15
        
# #         # Effort component (inverse - lower effort = higher priority)
# #         effort_score = ((6 - effort) / 5) * 20
        
# #         total_score = urgency_score + deadline_score + effort_score
# #         return round(total_score, 2)
    
# #     @staticmethod
# #     def get_smart_recommendations(tasks):
# #         """Generate AI recommendations based on task analysis"""
# #         if not tasks:
# #             return ["Add your first task to get started!", "Break large tasks into smaller chunks"]
        
# #         recommendations = []
        
# #         # Check for overdue tasks
# #         overdue = [t for t in tasks if t.get('deadline') and 
# #                    datetime.fromisoformat(t['deadline']) < datetime.now() and not t['completed']]
# #         if overdue:
# #             recommendations.append(f"⚠️ {len(overdue)} overdue task(s) need immediate attention")
        
# #         # Check for high-urgency tasks
# #         urgent = [t for t in tasks if t['urgency'] >= 4 and not t['completed']]
# #         if urgent:
# #             recommendations.append(f"🔥 Focus on {len(urgent)} high-urgency task(s) first")
        
# #         # Check task load
# #         pending = [t for t in tasks if not t['completed']]
# #         if len(pending) > 10:
# #             recommendations.append("📊 Consider breaking down large tasks into smaller chunks")
# #         elif len(pending) == 0:
# #             recommendations.append("✨ Great job! All tasks completed. Time to plan ahead.")
        
# #         # Time-based recommendations
# #         hour = datetime.now().hour
# #         if 8 <= hour <= 11:
# #             recommendations.append("🌅 Morning energy is high - tackle complex tasks now")
# #         elif 14 <= hour <= 16:
# #             recommendations.append("☕ Post-lunch dip - consider lighter tasks or a focus session")
        
# #         return recommendations[:3] if recommendations else ["Keep up the great work! 🚀"]

# # # AI/ML Logic - Productivity Analytics Engine
# # class ProductivityAnalytics:
# #     @staticmethod
# #     def calculate_productivity_score(tasks_completed, focus_sessions, distractions, total_focus_minutes):
# #         """
# #         Calculate daily productivity score (0-100)
# #         Formula: (tasks*10 + sessions*15 + focus_minutes*0.5) - (distractions*5)
# #         """
# #         base_score = (tasks_completed * 10) + (focus_sessions * 15) + (total_focus_minutes * 0.5)
# #         penalty = distractions * 5
# #         score = max(0, min(100, base_score - penalty))
# #         return round(score, 1)
    
# #     @staticmethod
# #     def get_productivity_insights(score, tasks_completed, focus_sessions):
# #         """Generate personalized productivity insights"""
# #         if score >= 80:
# #             return "🌟 Exceptional productivity! You're in the zone."
# #         elif score >= 60:
# #             return "✅ Solid performance! Keep the momentum going."
# #         elif score >= 40:
# #             return "📈 Good progress. Small improvements can boost your score."
# #         else:
# #             return "🎯 Let's focus on completing tasks and focus sessions."

# # # Routes
# # @app.route('/api/health', methods=['GET'])
# # def health_check():
# #     return jsonify({"status": "healthy", "message": "FocusMate AI Backend Running"})

# # @app.route('/api/tasks', methods=['GET', 'POST'])
# # def handle_tasks():
# #     conn = sqlite3.connect('focusmate.db')
# #     c = conn.cursor()
    
# #     if request.method == 'GET':
# #         c.execute('SELECT * FROM tasks ORDER BY ai_priority_score DESC, created_at DESC')
# #         tasks = []
# #         for row in c.fetchall():
# #             tasks.append({
# #                 'id': row[0],
# #                 'title': row[1],
# #                 'urgency': row[2],
# #                 'effort': row[3],
# #                 'deadline': row[4],
# #                 'completed': bool(row[5]),
# #                 'created_at': row[6],
# #                 'completed_at': row[7],
# #                 'ai_priority_score': row[8]
# #             })
# #         conn.close()
# #         return jsonify(tasks)
    
# #     elif request.method == 'POST':
# #         data = request.json
# #         title = data['title']
# #         urgency = data.get('urgency', 3)
# #         effort = data.get('effort', 3)
# #         deadline = data.get('deadline')
# #         created_at = datetime.now().isoformat()
        
# #         # Calculate AI priority score
# #         priority_score = TaskPrioritizationEngine.calculate_priority_score(
# #             urgency, effort, deadline
# #         )
        
# #         c.execute('''INSERT INTO tasks (title, urgency, effort, deadline, created_at, ai_priority_score)
# #                      VALUES (?, ?, ?, ?, ?, ?)''',
# #                   (title, urgency, effort, deadline, created_at, priority_score))
# #         conn.commit()
# #         task_id = c.lastrowid
# #         conn.close()
        
# #         return jsonify({
# #             'id': task_id,
# #             'title': title,
# #             'urgency': urgency,
# #             'effort': effort,
# #             'deadline': deadline,
# #             'completed': False,
# #             'created_at': created_at,
# #             'completed_at': None,
# #             'ai_priority_score': priority_score
# #         }), 201

# # @app.route('/api/tasks/<int:task_id>', methods=['PUT', 'DELETE'])
# # def handle_task(task_id):
# #     conn = sqlite3.connect('focusmate.db')
# #     c = conn.cursor()
    
# #     if request.method == 'PUT':
# #         data = request.json
        
# #         if 'completed' in data:
# #             completed = data['completed']
# #             completed_at = datetime.now().isoformat() if completed else None
# #             c.execute('UPDATE tasks SET completed = ?, completed_at = ? WHERE id = ?',
# #                       (completed, completed_at, task_id))
        
# #         if 'title' in data or 'urgency' in data or 'effort' in data or 'deadline' in data:
# #             c.execute('SELECT urgency, effort, deadline FROM tasks WHERE id = ?', (task_id,))
# #             current = c.fetchone()
            
# #             urgency = data.get('urgency', current[0])
# #             effort = data.get('effort', current[1])
# #             deadline = data.get('deadline', current[2])
            
# #             priority_score = TaskPrioritizationEngine.calculate_priority_score(
# #                 urgency, effort, deadline
# #             )
            
# #             c.execute('''UPDATE tasks SET title = ?, urgency = ?, effort = ?, 
# #                          deadline = ?, ai_priority_score = ? WHERE id = ?''',
# #                       (data.get('title'), urgency, effort, deadline, priority_score, task_id))
        
# #         conn.commit()
# #         conn.close()
# #         return jsonify({"message": "Task updated"})
    
# #     elif request.method == 'DELETE':
# #         c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
# #         conn.commit()
# #         conn.close()
# #         return jsonify({"message": "Task deleted"})

# # @app.route('/api/focus-sessions', methods=['GET', 'POST'])
# # def handle_focus_sessions():
# #     conn = sqlite3.connect('focusmate.db')
# #     c = conn.cursor()
    
# #     if request.method == 'GET':
# #         c.execute('SELECT * FROM focus_sessions ORDER BY start_time DESC LIMIT 10')
# #         sessions = []
# #         for row in c.fetchall():
# #             sessions.append({
# #                 'id': row[0],
# #                 'duration': row[1],
# #                 'start_time': row[2],
# #                 'end_time': row[3],
# #                 'focus_level': row[4],
# #                 'distractions': row[5],
# #                 'completed': bool(row[6])
# #             })
# #         conn.close()
# #         return jsonify(sessions)
    
# #     elif request.method == 'POST':
# #         data = request.json
# #         duration = data['duration']
# #         start_time = data.get('start_time', datetime.now().isoformat())
# #         distractions = data.get('distractions', 0)
# #         completed = data.get('completed', False)
        
# #         # AI Focus Prediction
# #         time_of_day = datetime.now().strftime("%H:%M")
        
# #         # Calculate past completion rate
# #         c.execute('SELECT COUNT(*) FROM focus_sessions WHERE completed = 1')
# #         completed_sessions = c.fetchone()[0]
# #         c.execute('SELECT COUNT(*) FROM focus_sessions')
# #         total_sessions = c.fetchone()[0]
# #         completion_rate = completed_sessions / total_sessions if total_sessions > 0 else 0.5
        
# #         focus_level = FocusPredictionEngine.predict_focus_level(
# #             time_of_day, duration, completion_rate
# #         )
        
# #         end_time = data.get('end_time')
        
# #         c.execute('''INSERT INTO focus_sessions 
# #                      (duration, start_time, end_time, focus_level, distractions, completed)
# #                      VALUES (?, ?, ?, ?, ?, ?)''',
# #                   (duration, start_time, end_time, focus_level, distractions, completed))
# #         conn.commit()
# #         session_id = c.lastrowid
# #         conn.close()
        
# #         # Calculate optimal break
# #         optimal_break = FocusPredictionEngine.calculate_optimal_break(duration)
        
# #         return jsonify({
# #             'id': session_id,
# #             'duration': duration,
# #             'start_time': start_time,
# #             'end_time': end_time,
# #             'focus_level': focus_level,
# #             'distractions': distractions,
# #             'completed': completed,
# #             'optimal_break': optimal_break
# #         }), 201

# # @app.route('/api/focus-sessions/<int:session_id>', methods=['PUT'])
# # def update_focus_session(session_id):
# #     conn = sqlite3.connect('focusmate.db')
# #     c = conn.cursor()
    
# #     data = request.json
# #     end_time = data.get('end_time', datetime.now().isoformat())
# #     completed = data.get('completed', True)
# #     distractions = data.get('distractions', 0)
    
# #     c.execute('''UPDATE focus_sessions 
# #                  SET end_time = ?, completed = ?, distractions = ?
# #                  WHERE id = ?''',
# #               (end_time, completed, distractions, session_id))
# #     conn.commit()
# #     conn.close()
    
# #     return jsonify({"message": "Focus session updated"})

# # # @app.route('/api/dashboard', methods=['GET'])
# # # def get_dashboard():
# # #     conn = sqlite3.connect('focusmate.db')
# # #     c = conn.cursor()
    
# # #     today = datetime.now().date().isoformat()
    
# # #     # Tasks completed today
# # #     c.execute('''SELECT COUNT(*) FROM tasks 
# # #                  WHERE completed = 1 AND DATE(completed_at) = ?''', (today,))
# # #     tasks_completed = c.fetchone()[0]
    
# # #     # Focus sessions today
# # #     c.execute('''SELECT COUNT(*), SUM(duration) FROM focus_sessions 
# # #                  WHERE completed = 1 AND DATE(start_time) = ?''', (today,))
# # #     session_data = c.fetchone()
# # #     focus_sessions = session_data[0]
# # #     total_focus_minutes = session_data[1] or 0
    
# # #     # Total distractions today
# # #     c.execute('''SELECT SUM(distractions) FROM focus_sessions 
# # #                  WHERE DATE(start_time) = ?''', (today,))
# # #     distractions = c.fetchone()[0] or 0
    
# # #     # Calculate productivity score
# # #     productivity_score = ProductivityAnalytics.calculate_productivity_score(
# # #         tasks_completed, focus_sessions, distractions, total_focus_minutes
# # #     )
    
# # #     # Get productivity insight
# # #     productivity_insight = ProductivityAnalytics.get_productivity_insights(
# # #         productivity_score, tasks_completed, focus_sessions
# # #     )
    
# # #     # Get top 3 priority tasks
# # #     c.execute('''SELECT * FROM tasks WHERE completed = 0 
# # #                  ORDER BY ai_priority_score DESC LIMIT 3''')
# # #     top_tasks = []
# # #     for row in c.fetchall():
# # #         top_tasks.append({
# # #             'id': row[0],
# # #             'title': row[1],
# # #             'urgency': row[2],
# # #             'ai_priority_score': row[8]
# # #         })
    
# # #     # Get all pending tasks for recommendations
# # #     c.execute('SELECT * FROM tasks WHERE completed = 0')
# # #     all_pending_tasks = []
# # #     for row in c.fetchall():
# # #         all_pending_tasks.append({
# # #             'id': row[0],
# # #             'title': row[1],
# # #             'urgency': row[2],
# # #             'effort': row[3],
# # #             'deadline': row[4],
# # #             'completed': bool(row[5]),
# # #             'ai_priority_score': row[8]
# # #         })
    
# # #     # Get AI recommendations
# # #     recommendations = TaskPrioritizationEngine.get_smart_recommendations(all_pending_tasks)
    
# # #     # Predict current focus level
# # #     time_of_day = datetime.now().strftime("%H:%M")
# # #     c.execute('SELECT COUNT(*) FROM focus_sessions WHERE completed = 1')
# # #     completed_sessions = c.fetchone()[0]
# # #     c.execute('SELECT COUNT(*) FROM focus_sessions')
# # #     total_sessions = c.fetchone()[0]
# # #     completion_rate = completed_sessions / total_sessions if total_sessions > 0 else 0.5
    
# # #     current_focus = FocusPredictionEngine.predict_focus_level(time_of_day, 30, completion_rate)
    
# # #     conn.close()
    
# # #     return jsonify({
# # #         'productivity_score': productivity_score,
# # #         'productivity_insight': productivity_insight,
# # #         'tasks_completed_today': tasks_completed,
# # #         'focus_sessions_today': focus_sessions,
# # #         'total_focus_minutes': total_focus_minutes,
# # #         'distractions_today': distractions,
# # #         'top_tasks': top_tasks,
# # #         'current_focus_level': current_focus,
# # #         'ai_recommendations': recommendations
# # #     })

# # # @app.route('/api/dashboard', methods=['GET'])
# # # def get_dashboard():
# # #     try:
# # #         conn = sqlite3.connect('focusmate.db')
# # #         c = conn.cursor()
        
# # #         today = datetime.now().date().isoformat()
        
# # #         # Tasks completed today
# # #         c.execute('''SELECT COUNT(*) FROM tasks 
# # #                      WHERE completed = 1 AND DATE(completed_at) = ?''', (today,))
# # #         row = c.fetchone()
# # #         tasks_completed = row[0] if row else 0
        
# # #         # Focus sessions today
# # #         c.execute('''SELECT COUNT(*), SUM(duration) FROM focus_sessions 
# # #                      WHERE completed = 1 AND DATE(start_time) = ?''', (today,))
# # #         session_data = c.fetchone()
# # #         focus_sessions = session_data[0] if session_data and session_data[0] else 0
# # #         total_focus_minutes = session_data[1] if session_data and session_data[1] else 0
        
# # #         # Total distractions today
# # #         c.execute('''SELECT SUM(distractions) FROM focus_sessions 
# # #                      WHERE DATE(start_time) = ?''', (today,))
# # #         row = c.fetchone()
# # #         distractions = row[0] if row and row[0] else 0
        
# # #         # Productivity score
# # #         productivity_score = ProductivityAnalytics.calculate_productivity_score(
# # #             tasks_completed, focus_sessions, distractions, total_focus_minutes
# # #         )
        
# # #         productivity_insight = ProductivityAnalytics.get_productivity_insights(
# # #             productivity_score, tasks_completed, focus_sessions
# # #         )
        
# # #         # Top 3 priority tasks
# # #         c.execute('''SELECT * FROM tasks WHERE completed = 0 
# # #                      ORDER BY ai_priority_score DESC LIMIT 3''')
# # #         top_tasks = []
# # #         for row in c.fetchall() or []:
# # #             top_tasks.append({
# # #                 'id': row[0],
# # #                 'title': row[1],
# # #                 'urgency': row[2],
# # #                 'ai_priority_score': row[8]
# # #             })
        
# # #         # Pending tasks for recommendations
# # #         c.execute('SELECT * FROM tasks WHERE completed = 0')
# # #         all_pending_tasks = []
# # #         for row in c.fetchall() or []:
# # #             all_pending_tasks.append({
# # #                 'id': row[0],
# # #                 'title': row[1],
# # #                 'urgency': row[2],
# # #                 'effort': row[3],
# # #                 'deadline': row[4],
# # #                 'completed': bool(row[5]),
# # #                 'ai_priority_score': row[8]
# # #             })
        
# # #         recommendations = TaskPrioritizationEngine.get_smart_recommendations(all_pending_tasks)
        
# # #         # Current focus prediction
# # #         time_of_day = datetime.now().strftime("%H:%M")
        
# # #         c.execute('SELECT COUNT(*) FROM focus_sessions WHERE completed = 1')
# # #         row1 = c.fetchone()
# # #         completed_sessions = row1[0] if row1 else 0
        
# # #         c.execute('SELECT COUNT(*) FROM focus_sessions')
# # #         row2 = c.fetchone()
# # #         total_sessions = row2[0] if row2 else 0
        
# # #         completion_rate = completed_sessions / total_sessions if total_sessions > 0 else 0.5
        
# # #         current_focus = FocusPredictionEngine.predict_focus_level(
# # #             time_of_day, 30, completion_rate
# # #         )
        
# # #         conn.close()
        
# # #         return jsonify({
# # #             'productivity_score': productivity_score,
# # #             'productivity_insight': productivity_insight,
# # #             'tasks_completed_today': tasks_completed,
# # #             'focus_sessions_today': focus_sessions,
# # #             'total_focus_minutes': total_focus_minutes,
# # #             'distractions_today': distractions,
# # #             'top_tasks': top_tasks,
# # #             'current_focus_level': current_focus,
# # #             'ai_recommendations': recommendations
# # #         })
    
# # #     except Exception as e:
# # #         print("Dashboard error:", str(e))
# # #         return jsonify({"error": str(e)}), 500

# # @app.route('/api/dashboard', methods=['GET'])
# # def get_dashboard():
# #     try:
# #         conn = sqlite3.connect('focusmate.db')
# #         c = conn.cursor()
        
# #         today = datetime.now().date().isoformat()
        
# #         # -------------------
# #         # Tasks completed today
# #         # -------------------
# #         c.execute('''SELECT COUNT(*) FROM tasks 
# #                      WHERE completed = 1 AND completed_at IS NOT NULL AND DATE(completed_at) = ?''', (today,))
# #         row = c.fetchone()
# #         tasks_completed = row[0] if row and row[0] is not None else 0
        
# #         # -------------------
# #         # Focus sessions today
# #         # -------------------
# #         c.execute('''SELECT COUNT(*), IFNULL(SUM(duration), 0) FROM focus_sessions 
# #                      WHERE completed = 1 AND DATE(start_time) = ?''', (today,))
# #         session_data = c.fetchone() or (0, 0)
# #         focus_sessions = session_data[0] or 0
# #         total_focus_minutes = session_data[1] or 0
        
# #         # -------------------
# #         # Total distractions today
# #         # -------------------
# #         c.execute('''SELECT IFNULL(SUM(distractions), 0) FROM focus_sessions 
# #                      WHERE DATE(start_time) = ?''', (today,))
# #         row = c.fetchone()
# #         distractions = row[0] or 0
        
# #         # -------------------
# #         # Productivity score
# #         # -------------------
# #         productivity_score = ProductivityAnalytics.calculate_productivity_score(
# #             tasks_completed, focus_sessions, distractions, total_focus_minutes
# #         )
        
# #         productivity_insight = ProductivityAnalytics.get_productivity_insights(
# #             productivity_score, tasks_completed, focus_sessions
# #         )
        
# #         # -------------------
# #         # Top 3 priority tasks
# #         # -------------------
# #         c.execute('''SELECT * FROM tasks WHERE completed = 0 
# #                      ORDER BY IFNULL(ai_priority_score, 0) DESC LIMIT 3''')
# #         top_tasks = []
# #         for row in c.fetchall() or []:
# #             top_tasks.append({
# #                 'id': row[0],
# #                 'title': row[1],
# #                 'urgency': row[2] or 0,
# #                 'ai_priority_score': row[8] or 0
# #             })
        
# #         # -------------------
# #         # Pending tasks for recommendations
# #         # -------------------
# #         c.execute('SELECT * FROM tasks WHERE completed = 0')
# #         all_pending_tasks = []
# #         for row in c.fetchall() or []:
# #             all_pending_tasks.append({
# #                 'id': row[0],
# #                 'title': row[1],
# #                 'urgency': row[2] or 0,
# #                 'effort': row[3] or 0,
# #                 'deadline': row[4],
# #                 'completed': bool(row[5]),
# #                 'ai_priority_score': row[8] or 0
# #             })
        
# #         recommendations = TaskPrioritizationEngine.get_smart_recommendations(all_pending_tasks)
        
# #         # -------------------
# #         # Current focus prediction
# #         # -------------------
# #         time_of_day = datetime.now().strftime("%H:%M")
        
# #         c.execute('SELECT COUNT(*) FROM focus_sessions WHERE completed = 1')
# #         row1 = c.fetchone()
# #         completed_sessions = row1[0] if row1 and row1[0] is not None else 0
        
# #         c.execute('SELECT COUNT(*) FROM focus_sessions')
# #         row2 = c.fetchone()
# #         total_sessions = row2[0] if row2 and row2[0] is not None else 0
        
# #         completion_rate = completed_sessions / total_sessions if total_sessions > 0 else 0.5
        
# #         current_focus = FocusPredictionEngine.predict_focus_level(
# #             time_of_day, 30, completion_rate
# #         )
        
# #         conn.close()
        
# #         # -------------------
# #         # Return JSON
# #         # -------------------
# #         return jsonify({
# #             'productivity_score': productivity_score,
# #             'productivity_insight': productivity_insight,
# #             'tasks_completed_today': tasks_completed,
# #             'focus_sessions_today': focus_sessions,
# #             'total_focus_minutes': total_focus_minutes,
# #             'distractions_today': distractions,
# #             'top_tasks': top_tasks,
# #             'current_focus_level': current_focus,
# #             'ai_recommendations': recommendations
# #         })
    
# #     except Exception as e:
# #         print("Dashboard error:", str(e))
# #         return jsonify({"error": str(e)}), 500


# # @app.route('/api/insights', methods=['GET'])
# # def get_insights():
# #     conn = sqlite3.connect('focusmate.db')
# #     c = conn.cursor()
    
# #     # Get last 7 days of data
# #     insights = []
# #     for i in range(6, -1, -1):
# #         date = (datetime.now() - timedelta(days=i)).date().isoformat()
        
# #         c.execute('''SELECT COUNT(*) FROM tasks 
# #                      WHERE completed = 1 AND DATE(completed_at) = ?''', (date,))
# #         tasks = c.fetchone()[0]
        
# #         c.execute('''SELECT COUNT(*), SUM(duration), SUM(distractions) FROM focus_sessions 
# #                      WHERE completed = 1 AND DATE(start_time) = ?''', (date,))
# #         session_data = c.fetchone()
# #         sessions = session_data[0]
# #         minutes = session_data[1] or 0
# #         distractions = session_data[2] or 0
        
# #         score = ProductivityAnalytics.calculate_productivity_score(
# #             tasks, sessions, distractions, minutes
# #         )
        
# #         insights.append({
# #             'date': date,
# #             'tasks_completed': tasks,
# #             'focus_sessions': sessions,
# #             'focus_minutes': minutes,
# #             'productivity_score': score,
# #             'distractions': distractions
# #         })
    
# #     conn.close()
# #     return jsonify(insights)

# # # if __name__ == '__main__':
# # #     init_db()
# # #     app.run(debug=True, port=5000)

# # if __name__ == "__main__":
# #     init_db()
# #     app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

# import os
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from datetime import datetime, timedelta
# import sqlite3
# import logging

# # -----------------------
# # App Setup
# # -----------------------
# app = Flask(__name__)
# CORS(app, resources={r"/api/*": {"origins": "*"}})

# # Logging
# logging.basicConfig(level=logging.INFO)

# # Database path
# DB_PATH = os.environ.get("DB_PATH", "focusmate.db")

# # -----------------------
# # Database Initialization
# # -----------------------
# def init_db():
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     # Tasks
#     c.execute('''CREATE TABLE IF NOT EXISTS tasks
#                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                   title TEXT NOT NULL,
#                   urgency INTEGER,
#                   effort INTEGER,
#                   deadline TEXT,
#                   completed BOOLEAN DEFAULT 0,
#                   created_at TEXT,
#                   completed_at TEXT,
#                   ai_priority_score REAL)''')
#     # Focus sessions
#     c.execute('''CREATE TABLE IF NOT EXISTS focus_sessions
#                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                   duration INTEGER,
#                   start_time TEXT,
#                   end_time TEXT,
#                   focus_level TEXT,
#                   distractions INTEGER DEFAULT 0,
#                   completed BOOLEAN DEFAULT 0)''')
#     # Productivity metrics
#     c.execute('''CREATE TABLE IF NOT EXISTS metrics
#                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                   date TEXT,
#                   tasks_completed INTEGER,
#                   focus_sessions INTEGER,
#                   total_focus_minutes INTEGER,
#                   productivity_score REAL,
#                   distraction_count INTEGER)''')
#     conn.commit()
#     conn.close()

# # -----------------------
# # AI Engines
# # -----------------------
# class FocusPredictionAI:
#     @staticmethod
#     def predict_focus(time_of_day, session_duration, past_completion_rate):
#         score = 0
#         hour = int(time_of_day.split(':')[0])
#         if 8 <= hour <= 11:
#             score += 40
#         elif 14 <= hour <= 16:
#             score += 20
#         elif 17 <= hour <= 20:
#             score += 30
#         else:
#             score += 10
#         if 25 <= session_duration <= 45:
#             score += 35
#         elif session_duration < 25:
#             score += 20
#         else:
#             score += 15
#         score += past_completion_rate * 25
#         if score >= 70:
#             return "High"
#         elif score >= 45:
#             return "Medium"
#         else:
#             return "Low"

#     @staticmethod
#     def optimal_break(focus_minutes):
#         if focus_minutes <= 25:
#             return 5
#         elif focus_minutes <= 50:
#             return 10
#         else:
#             return 15

# class TaskPrioritizationAI:
#     @staticmethod
#     def priority_score(urgency, effort, deadline_str):
#         urgency_score = (urgency / 5) * 40
#         try:
#             if deadline_str:
#                 deadline = datetime.fromisoformat(deadline_str)
#                 days_until = (deadline - datetime.now()).days
#                 if days_until < 0:
#                     deadline_score = 50
#                 elif days_until == 0:
#                     deadline_score = 45
#                 elif days_until <= 1:
#                     deadline_score = 40
#                 elif days_until <= 3:
#                     deadline_score = 30
#                 elif days_until <= 7:
#                     deadline_score = 20
#                 else:
#                     deadline_score = 10
#             else:
#                 deadline_score = 15
#         except:
#             deadline_score = 15
#         effort_score = ((6 - effort) / 5) * 20
#         return round(urgency_score + deadline_score + effort_score, 2)

#     @staticmethod
#     def smart_recommendations(tasks):
#         if not tasks:
#             return ["Add your first task to get started!", "Break large tasks into smaller chunks"]
#         recommendations = []
#         overdue = [t for t in tasks if t.get('deadline') and 
#                    datetime.fromisoformat(t['deadline']) < datetime.now() and not t['completed']]
#         if overdue:
#             recommendations.append(f"⚠️ {len(overdue)} overdue task(s) need attention")
#         urgent = [t for t in tasks if t['urgency'] >= 4 and not t['completed']]
#         if urgent:
#             recommendations.append(f"🔥 Focus on {len(urgent)} high-urgency task(s) first")
#         pending = [t for t in tasks if not t['completed']]
#         if len(pending) > 10:
#             recommendations.append("📊 Break large tasks into smaller chunks")
#         elif len(pending) == 0:
#             recommendations.append("✨ All tasks completed! Time to plan ahead.")
#         hour = datetime.now().hour
#         if 8 <= hour <= 11:
#             recommendations.append("🌅 Morning energy high - tackle complex tasks now")
#         elif 14 <= hour <= 16:
#             recommendations.append("☕ Post-lunch dip - consider lighter tasks")
#         return recommendations[:3] if recommendations else ["Keep up the great work! 🚀"]

# class ProductivityAI:
#     @staticmethod
#     def score(tasks_completed, focus_sessions, distractions, total_focus_minutes):
#         base_score = (tasks_completed * 10) + (focus_sessions * 15) + (total_focus_minutes * 0.5)
#         score = max(0, min(100, base_score - distractions * 5))
#         return round(score, 1)

#     @staticmethod
#     def insights(score):
#         if score >= 80:
#             return "🌟 Exceptional productivity!"
#         elif score >= 60:
#             return "✅ Solid performance! Keep going."
#         elif score >= 40:
#             return "📈 Good progress, improve focus."
#         else:
#             return "🎯 Focus on completing tasks and sessions."

# # -----------------------
# # Routes
# # -----------------------
# @app.route('/api/health', methods=['GET'])
# def health_check():
#     return jsonify({"status": "healthy", "message": "FocusMate AI Backend Running"})

# # Tasks CRUD
# @app.route('/api/tasks', methods=['GET', 'POST'])
# def tasks():
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     if request.method == 'GET':
#         c.execute('SELECT * FROM tasks ORDER BY ai_priority_score DESC, created_at DESC')
#         tasks = [dict(zip([col[0] for col in c.description], row)) for row in c.fetchall()]
#         conn.close()
#         return jsonify(tasks)
#     else:  # POST
#         data = request.json
#         title = data['title']
#         urgency = data.get('urgency', 3)
#         effort = data.get('effort', 3)
#         deadline = data.get('deadline')
#         created_at = datetime.now().isoformat()
#         priority = TaskPrioritizationAI.priority_score(urgency, effort, deadline)
#         c.execute('INSERT INTO tasks (title, urgency, effort, deadline, created_at, ai_priority_score) VALUES (?, ?, ?, ?, ?, ?)',
#                   (title, urgency, effort, deadline, created_at, priority))
#         conn.commit()
#         task_id = c.lastrowid
#         conn.close()
#         return jsonify({
#             "id": task_id, "title": title, "urgency": urgency, "effort": effort,
#             "deadline": deadline, "completed": False, "created_at": created_at,
#             "completed_at": None, "ai_priority_score": priority
#         }), 201

# @app.route('/api/tasks/<int:task_id>', methods=['PUT', 'DELETE'])
# def update_task(task_id):
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     data = request.json
#     if request.method == 'PUT':
#         c.execute('SELECT urgency, effort, deadline FROM tasks WHERE id=?', (task_id,))
#         current = c.fetchone()
#         if not current:
#             conn.close()
#             return jsonify({"error": "Task not found"}), 404
#         urgency = data.get('urgency', current[0])
#         effort = data.get('effort', current[1])
#         deadline = data.get('deadline', current[2])
#         priority = TaskPrioritizationAI.priority_score(urgency, effort, deadline)
#         completed = data.get('completed', False)
#         completed_at = datetime.now().isoformat() if completed else None
#         c.execute('UPDATE tasks SET title=?, urgency=?, effort=?, deadline=?, completed=?, completed_at=?, ai_priority_score=? WHERE id=?',
#                   (data.get('title'), urgency, effort, deadline, completed, completed_at, priority, task_id))
#         conn.commit()
#         conn.close()
#         return jsonify({"message": "Task updated"})
#     else:  # DELETE
#         c.execute('DELETE FROM tasks WHERE id=?', (task_id,))
#         conn.commit()
#         conn.close()
#         return jsonify({"message": "Task deleted"})

# # Focus Sessions
# @app.route('/api/focus-sessions', methods=['GET', 'POST'])
# def focus_sessions():
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     if request.method == 'GET':
#         c.execute('SELECT * FROM focus_sessions ORDER BY start_time DESC LIMIT 10')
#         sessions = [dict(zip([col[0] for col in c.description], row)) for row in c.fetchall()]
#         conn.close()
#         return jsonify(sessions)
#     else:  # POST
#         data = request.json
#         duration = data['duration']
#         start_time = data.get('start_time', datetime.now().isoformat())
#         distractions = data.get('distractions', 0)
#         completed = data.get('completed', False)
#         c.execute('SELECT COUNT(*) FROM focus_sessions WHERE completed=1')
#         completed_sessions = c.fetchone()[0]
#         c.execute('SELECT COUNT(*) FROM focus_sessions')
#         total_sessions = c.fetchone()[0]
#         past_rate = completed_sessions / total_sessions if total_sessions > 0 else 0.5
#         focus_level = FocusPredictionAI.predict_focus(datetime.now().strftime("%H:%M"), duration, past_rate)
#         end_time = data.get('end_time')
#         c.execute('INSERT INTO focus_sessions (duration, start_time, end_time, focus_level, distractions, completed) VALUES (?, ?, ?, ?, ?, ?)',
#                   (duration, start_time, end_time, focus_level, distractions, completed))
#         conn.commit()
#         session_id = c.lastrowid
#         conn.close()
#         return jsonify({
#             "id": session_id, "duration": duration, "start_time": start_time,
#             "end_time": end_time, "focus_level": focus_level,
#             "distractions": distractions, "completed": completed,
#             "optimal_break": FocusPredictionAI.optimal_break(duration)
#         }), 201

# @app.route('/api/focus-sessions/<int:session_id>', methods=['PUT'])
# def update_focus(session_id):
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     data = request.json
#     end_time = data.get('end_time', datetime.now().isoformat())
#     completed = data.get('completed', True)
#     distractions = data.get('distractions', 0)
#     c.execute('UPDATE focus_sessions SET end_time=?, completed=?, distractions=? WHERE id=?',
#               (end_time, completed, distractions, session_id))
#     conn.commit()
#     conn.close()
#     return jsonify({"message": "Focus session updated"})

# # Dashboard
# @app.route('/api/dashboard', methods=['GET'])
# def dashboard():
#     try:
#         conn = sqlite3.connect(DB_PATH)
#         c = conn.cursor()
#         today = datetime.now().date().isoformat()
#         c.execute('SELECT COUNT(*) FROM tasks WHERE completed=1 AND completed_at IS NOT NULL AND DATE(completed_at)=?', (today,))
#         tasks_done = c.fetchone()[0] or 0
#         c.execute('SELECT COUNT(*), IFNULL(SUM(duration),0) FROM focus_sessions WHERE completed=1 AND DATE(start_time)=?', (today,))
#         fs = c.fetchone() or (0,0)
#         focus_sessions, total_minutes = fs
#         c.execute('SELECT IFNULL(SUM(distractions),0) FROM focus_sessions WHERE DATE(start_time)=?', (today,))
#         distractions = c.fetchone()[0] or 0
#         productivity_score = ProductivityAI.score(tasks_done, focus_sessions, distractions, total_minutes)
#         insight = ProductivityAI.insights(productivity_score)
#         # Top tasks
#         c.execute('SELECT * FROM tasks WHERE completed=0 ORDER BY IFNULL(ai_priority_score,0) DESC LIMIT 3')
#         top_tasks = [dict(zip([col[0] for col in c.description], row)) for row in c.fetchall()]
#         # Recommendations
#         c.execute('SELECT * FROM tasks WHERE completed=0')
#         pending_tasks = [dict(zip([col[0] for col in c.description], row)) for row in c.fetchall()]
#         recommendations = TaskPrioritizationAI.smart_recommendations(pending_tasks)
#         # Current focus
#         c.execute('SELECT COUNT(*) FROM focus_sessions WHERE completed=1')
#         completed_sessions = c.fetchone()[0] or 0
#         c.execute('SELECT COUNT(*) FROM focus_sessions')
#         total_sessions = c.fetchone()[0] or 0
#         completion_rate = completed_sessions / total_sessions if total_sessions > 0 else 0.5
#         current_focus = FocusPredictionAI.predict_focus(datetime.now().strftime("%H:%M"), 30, completion_rate)
#         conn.close()
#         return jsonify({
#             "productivity_score": productivity_score,
#             "productivity_insight": insight,
#             "tasks_completed_today": tasks_done,
#             "focus_sessions_today": focus_sessions,
#             "total_focus_minutes": total_minutes,
#             "distractions_today": distractions,
#             "top_tasks": top_tasks,
#             "current_focus_level": current_focus,
#             "ai_recommendations": recommendations
#         })
#     except Exception as e:
#         logging.error(f"Dashboard error: {str(e)}")
#         return jsonify({"error": str(e)}), 500

# # Insights last 7 days
# @app.route('/api/insights', methods=['GET'])
# def insights():
#     try:
#         conn = sqlite3.connect(DB_PATH)
#         c = conn.cursor()
#         last_7_days = []
#         for i in range(6, -1, -1):
#             date = (datetime.now() - timedelta(days=i)).date().isoformat()
#             c.execute('SELECT COUNT(*) FROM tasks WHERE completed=1 AND DATE(completed_at)=?', (date,))
#             tasks = c.fetchone()[0] or 0
#             c.execute('SELECT COUNT(*), SUM(duration), SUM(distractions) FROM focus_sessions WHERE completed=1 AND DATE(start_time)=?', (date,))
#             fs = c.fetchone() or (0,0,0)
#             sessions, minutes, distractions = fs
#             score = ProductivityAI.score(tasks, sessions, distractions or 0, minutes or 0)
#             last_7_days.append({
#                 "date": date,
#                 "tasks_completed": tasks,
#                 "focus_sessions": sessions,
#                 "focus_minutes": minutes or 0,
#                 "productivity_score": score,
#                 "distractions": distractions or 0
#             })
#         conn.close()
#         return jsonify(last_7_days)
#     except Exception as e:
#         logging.error(f"Insights error: {str(e)}")
#         return jsonify({"error": str(e)}), 500

# # Run server
# if __name__ == "__main__":
#     init_db()
#     PORT = int(os.environ.get("PORT", 5000))
#     DEBUG = os.environ.get("DEBUG", "False") == "True"
#     app.run(debug=DEBUG, host="0.0.0.0", port=PORT)


import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
import sqlite3
import logging
import sys

# -----------------------
# Logging Configuration
# -----------------------
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

# -----------------------
# App Setup
# -----------------------
app = Flask(__name__)

# CORS - Allow all origins for production
CORS(app, resources={
    r"/api/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# Database path - Use Render's persistent directory
if os.environ.get("RENDER"):
    # Render production environment
    DB_PATH = "/opt/render/project/src/focusmate.db"
else:
    # Local development
    DB_PATH = os.environ.get("DB_PATH", "focusmate.db")

logger.info(f"Database path: {DB_PATH}")

# -----------------------
# Database Initialization
# -----------------------
def init_db():
    """Initialize database tables - MUST be called before any DB operation"""
    try:
        logger.info("Initializing database...")
        
        # Ensure directory exists
        db_dir = os.path.dirname(DB_PATH)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir, exist_ok=True)
            logger.info(f"Created directory: {db_dir}")
        
        conn = sqlite3.connect(DB_PATH)
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
        
        # Metrics table
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
        logger.info("✅ Database initialized successfully")
        return True
    except Exception as e:
        logger.error(f"❌ Database initialization failed: {str(e)}")
        return False

def ensure_db_exists():
    """Ensure database and tables exist before operations"""
    if not os.path.exists(DB_PATH):
        logger.warning("Database file not found, creating...")
        init_db()
    else:
        # Verify tables exist
        try:
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tasks'")
            if not c.fetchone():
                logger.warning("Tables missing, reinitializing...")
                conn.close()
                init_db()
            else:
                conn.close()
        except Exception as e:
            logger.error(f"Database check failed: {e}")
            init_db()

# Initialize database on module load (CRITICAL for Gunicorn)
init_db()

# -----------------------
# AI Engines
# -----------------------
class FocusPredictionAI:
    @staticmethod
    def predict_focus(time_of_day, session_duration, past_completion_rate):
        try:
            score = 0
            hour = int(time_of_day.split(':')[0])
            if 8 <= hour <= 11:
                score += 40
            elif 14 <= hour <= 16:
                score += 20
            elif 17 <= hour <= 20:
                score += 30
            else:
                score += 10
            
            if 25 <= session_duration <= 45:
                score += 35
            elif session_duration < 25:
                score += 20
            else:
                score += 15
            
            score += past_completion_rate * 25
            
            if score >= 70:
                return "High"
            elif score >= 45:
                return "Medium"
            else:
                return "Low"
        except Exception as e:
            logger.error(f"Focus prediction error: {e}")
            return "Medium"

    @staticmethod
    def optimal_break(focus_minutes):
        try:
            if focus_minutes <= 25:
                return 5
            elif focus_minutes <= 50:
                return 10
            else:
                return 15
        except:
            return 5

class TaskPrioritizationAI:
    @staticmethod
    def priority_score(urgency, effort, deadline_str):
        try:
            urgency_score = (urgency / 5) * 40
            
            if deadline_str:
                try:
                    deadline = datetime.fromisoformat(deadline_str)
                    days_until = (deadline - datetime.now()).days
                    if days_until < 0:
                        deadline_score = 50
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
            
            effort_score = ((6 - effort) / 5) * 20
            return round(urgency_score + deadline_score + effort_score, 2)
        except Exception as e:
            logger.error(f"Priority score error: {e}")
            return 50.0

    @staticmethod
    def smart_recommendations(tasks):
        try:
            if not tasks:
                return ["Add your first task to get started!", "Break large tasks into smaller chunks"]
            
            recommendations = []
            overdue = [t for t in tasks if t.get('deadline') and 
                       datetime.fromisoformat(t['deadline']) < datetime.now() and not t.get('completed', False)]
            if overdue:
                recommendations.append(f"⚠️ {len(overdue)} overdue task(s) need attention")
            
            urgent = [t for t in tasks if t.get('urgency', 0) >= 4 and not t.get('completed', False)]
            if urgent:
                recommendations.append(f"🔥 Focus on {len(urgent)} high-urgency task(s) first")
            
            pending = [t for t in tasks if not t.get('completed', False)]
            if len(pending) > 10:
                recommendations.append("📊 Break large tasks into smaller chunks")
            elif len(pending) == 0:
                recommendations.append("✨ All tasks completed! Time to plan ahead.")
            
            hour = datetime.now().hour
            if 8 <= hour <= 11:
                recommendations.append("🌅 Morning energy high - tackle complex tasks now")
            elif 14 <= hour <= 16:
                recommendations.append("☕ Post-lunch dip - consider lighter tasks")
            
            return recommendations[:3] if recommendations else ["Keep up the great work! 🚀"]
        except Exception as e:
            logger.error(f"Recommendations error: {e}")
            return ["Keep up the great work! 🚀"]

class ProductivityAI:
    @staticmethod
    def score(tasks_completed, focus_sessions, distractions, total_focus_minutes):
        try:
            base_score = (tasks_completed * 10) + (focus_sessions * 15) + (total_focus_minutes * 0.5)
            score = max(0, min(100, base_score - distractions * 5))
            return round(score, 1)
        except:
            return 0.0

    @staticmethod
    def insights(score):
        try:
            if score >= 80:
                return "🌟 Exceptional productivity!"
            elif score >= 60:
                return "✅ Solid performance! Keep going."
            elif score >= 40:
                return "📈 Good progress, improve focus."
            else:
                return "🎯 Focus on completing tasks and sessions."
        except:
            return "Keep pushing forward!"

# -----------------------
# Error Handler Decorator
# -----------------------
def handle_db_errors(f):
    """Decorator to handle database errors gracefully"""
    def wrapper(*args, **kwargs):
        try:
            ensure_db_exists()
            return f(*args, **kwargs)
        except sqlite3.Error as e:
            logger.error(f"Database error in {f.__name__}: {str(e)}")
            return jsonify({"error": f"Database error: {str(e)}"}), 500
        except Exception as e:
            logger.error(f"Error in {f.__name__}: {str(e)}")
            return jsonify({"error": f"Server error: {str(e)}"}), 500
    wrapper.__name__ = f.__name__
    return wrapper

# -----------------------
# Routes
# -----------------------
@app.route('/', methods=['GET'])
def home():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "message": "FocusMate AI Backend Running",
        "version": "1.0.0",
        "database": "connected" if os.path.exists(DB_PATH) else "not found"
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    """Detailed health check"""
    db_status = "connected"
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM tasks")
        task_count = c.fetchone()[0]
        conn.close()
    except Exception as e:
        db_status = f"error: {str(e)}"
        task_count = 0
    
    return jsonify({
        "status": "healthy",
        "message": "FocusMate AI Backend Running",
        "database": db_status,
        "tasks_count": task_count,
        "db_path": DB_PATH
    })

@app.route('/api/tasks', methods=['GET', 'POST'])
@handle_db_errors
def tasks():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    if request.method == 'GET':
        c.execute('SELECT * FROM tasks ORDER BY ai_priority_score DESC, created_at DESC')
        tasks = [dict(zip([col[0] for col in c.description], row)) for row in c.fetchall()]
        conn.close()
        return jsonify(tasks), 200
    
    else:  # POST
        data = request.json
        if not data or 'title' not in data:
            conn.close()
            return jsonify({"error": "Title is required"}), 400
        
        title = data['title']
        urgency = data.get('urgency', 3)
        effort = data.get('effort', 3)
        deadline = data.get('deadline')
        created_at = datetime.now().isoformat()
        priority = TaskPrioritizationAI.priority_score(urgency, effort, deadline)
        
        c.execute('''INSERT INTO tasks (title, urgency, effort, deadline, created_at, ai_priority_score) 
                     VALUES (?, ?, ?, ?, ?, ?)''',
                  (title, urgency, effort, deadline, created_at, priority))
        conn.commit()
        task_id = c.lastrowid
        conn.close()
        
        return jsonify({
            "id": task_id, "title": title, "urgency": urgency, "effort": effort,
            "deadline": deadline, "completed": False, "created_at": created_at,
            "completed_at": None, "ai_priority_score": priority
        }), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT', 'DELETE'])
@handle_db_errors
def update_task(task_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    if request.method == 'PUT':
        data = request.json
        c.execute('SELECT urgency, effort, deadline, title FROM tasks WHERE id=?', (task_id,))
        current = c.fetchone()
        
        if not current:
            conn.close()
            return jsonify({"error": "Task not found"}), 404
        
        title = data.get('title', current[3])
        urgency = data.get('urgency', current[0])
        effort = data.get('effort', current[1])
        deadline = data.get('deadline', current[2])
        priority = TaskPrioritizationAI.priority_score(urgency, effort, deadline)
        completed = data.get('completed')
        
        if completed is not None:
            completed_at = datetime.now().isoformat() if completed else None
            c.execute('''UPDATE tasks SET title=?, urgency=?, effort=?, deadline=?, 
                         completed=?, completed_at=?, ai_priority_score=? WHERE id=?''',
                      (title, urgency, effort, deadline, completed, completed_at, priority, task_id))
        else:
            c.execute('''UPDATE tasks SET title=?, urgency=?, effort=?, deadline=?, 
                         ai_priority_score=? WHERE id=?''',
                      (title, urgency, effort, deadline, priority, task_id))
        
        conn.commit()
        conn.close()
        return jsonify({"message": "Task updated successfully"}), 200
    
    else:  # DELETE
        c.execute('DELETE FROM tasks WHERE id=?', (task_id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "Task deleted successfully"}), 200

@app.route('/api/focus-sessions', methods=['GET', 'POST'])
@handle_db_errors
def focus_sessions():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    if request.method == 'GET':
        c.execute('SELECT * FROM focus_sessions ORDER BY start_time DESC LIMIT 10')
        sessions = [dict(zip([col[0] for col in c.description], row)) for row in c.fetchall()]
        conn.close()
        return jsonify(sessions), 200
    
    else:  # POST
        data = request.json
        if not data or 'duration' not in data:
            conn.close()
            return jsonify({"error": "Duration is required"}), 400
        
        duration = data['duration']
        start_time = data.get('start_time', datetime.now().isoformat())
        distractions = data.get('distractions', 0)
        completed = data.get('completed', False)
        
        # Calculate completion rate
        c.execute('SELECT COUNT(*) FROM focus_sessions WHERE completed=1')
        completed_sessions = c.fetchone()[0] or 0
        c.execute('SELECT COUNT(*) FROM focus_sessions')
        total_sessions = c.fetchone()[0] or 0
        past_rate = completed_sessions / total_sessions if total_sessions > 0 else 0.5
        
        focus_level = FocusPredictionAI.predict_focus(
            datetime.now().strftime("%H:%M"), duration, past_rate
        )
        end_time = data.get('end_time')
        
        c.execute('''INSERT INTO focus_sessions (duration, start_time, end_time, focus_level, distractions, completed) 
                     VALUES (?, ?, ?, ?, ?, ?)''',
                  (duration, start_time, end_time, focus_level, distractions, completed))
        conn.commit()
        session_id = c.lastrowid
        conn.close()
        
        return jsonify({
            "id": session_id, "duration": duration, "start_time": start_time,
            "end_time": end_time, "focus_level": focus_level,
            "distractions": distractions, "completed": completed,
            "optimal_break": FocusPredictionAI.optimal_break(duration)
        }), 201

@app.route('/api/focus-sessions/<int:session_id>', methods=['PUT'])
@handle_db_errors
def update_focus(session_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    data = request.json
    
    end_time = data.get('end_time', datetime.now().isoformat())
    completed = data.get('completed', True)
    distractions = data.get('distractions', 0)
    
    c.execute('''UPDATE focus_sessions SET end_time=?, completed=?, distractions=? WHERE id=?''',
              (end_time, completed, distractions, session_id))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Focus session updated successfully"}), 200

@app.route('/api/dashboard', methods=['GET'])
@handle_db_errors
def dashboard():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    today = datetime.now().date().isoformat()
    
    # Tasks completed today
    c.execute('''SELECT COUNT(*) FROM tasks 
                 WHERE completed=1 AND completed_at IS NOT NULL AND DATE(completed_at)=?''', (today,))
    tasks_done = c.fetchone()[0] or 0
    
    # Focus sessions today
    c.execute('''SELECT COUNT(*), IFNULL(SUM(duration),0) FROM focus_sessions 
                 WHERE completed=1 AND DATE(start_time)=?''', (today,))
    fs = c.fetchone()
    focus_sessions = fs[0] if fs else 0
    total_minutes = fs[1] if fs else 0
    
    # Distractions today
    c.execute('''SELECT IFNULL(SUM(distractions),0) FROM focus_sessions WHERE DATE(start_time)=?''', (today,))
    distractions = c.fetchone()[0] or 0
    
    # Calculate productivity score
    productivity_score = ProductivityAI.score(tasks_done, focus_sessions, distractions, total_minutes)
    insight = ProductivityAI.insights(productivity_score)
    
    # Top tasks
    c.execute('''SELECT * FROM tasks WHERE completed=0 
                 ORDER BY IFNULL(ai_priority_score,0) DESC LIMIT 3''')
    top_tasks = [dict(zip([col[0] for col in c.description], row)) for row in c.fetchall()]
    
    # All pending tasks for recommendations
    c.execute('SELECT * FROM tasks WHERE completed=0')
    pending_tasks = [dict(zip([col[0] for col in c.description], row)) for row in c.fetchall()]
    recommendations = TaskPrioritizationAI.smart_recommendations(pending_tasks)
    
    # Current focus prediction
    c.execute('SELECT COUNT(*) FROM focus_sessions WHERE completed=1')
    completed_sessions = c.fetchone()[0] or 0
    c.execute('SELECT COUNT(*) FROM focus_sessions')
    total_sessions = c.fetchone()[0] or 0
    completion_rate = completed_sessions / total_sessions if total_sessions > 0 else 0.5
    current_focus = FocusPredictionAI.predict_focus(datetime.now().strftime("%H:%M"), 30, completion_rate)
    
    conn.close()
    
    return jsonify({
        "productivity_score": productivity_score,
        "productivity_insight": insight,
        "tasks_completed_today": tasks_done,
        "focus_sessions_today": focus_sessions,
        "total_focus_minutes": total_minutes,
        "distractions_today": distractions,
        "top_tasks": top_tasks,
        "current_focus_level": current_focus,
        "ai_recommendations": recommendations
    }), 200

@app.route('/api/insights', methods=['GET'])
@handle_db_errors
def insights():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    last_7_days = []
    
    for i in range(6, -1, -1):
        date = (datetime.now() - timedelta(days=i)).date().isoformat()
        
        c.execute('SELECT COUNT(*) FROM tasks WHERE completed=1 AND DATE(completed_at)=?', (date,))
        tasks = c.fetchone()[0] or 0
        
        c.execute('''SELECT COUNT(*), IFNULL(SUM(duration),0), IFNULL(SUM(distractions),0) 
                     FROM focus_sessions WHERE completed=1 AND DATE(start_time)=?''', (date,))
        fs = c.fetchone()
        sessions = fs[0] if fs else 0
        minutes = fs[1] if fs else 0
        distractions = fs[2] if fs else 0
        
        score = ProductivityAI.score(tasks, sessions, distractions, minutes)
        
        last_7_days.append({
            "date": date,
            "tasks_completed": tasks,
            "focus_sessions": sessions,
            "focus_minutes": minutes,
            "productivity_score": score,
            "distractions": distractions
        })
    
    conn.close()
    return jsonify(last_7_days), 200

# -----------------------
# Error Handlers
# -----------------------
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(e):
    logger.error(f"Internal server error: {str(e)}")
    return jsonify({"error": "Internal server error"}), 500

# -----------------------
# Run Server
# -----------------------
if __name__ == "__main__":
    # Local development only
    PORT = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=PORT)