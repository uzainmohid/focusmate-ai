# 🧠 FocusMate AI - Smart Focus & Productivity Coach

A premium SaaS product that helps users improve focus and productivity through AI-powered task prioritization, focus prediction, and productivity insights.

![FocusMate AI](https://img.shields.io/badge/AI-Powered-00d4ff?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-Flask-green?style=for-the-badge)
![React](https://img.shields.io/badge/React-Vite-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

---

## 🎯 Product Overview

**FocusMate AI** is NOT just another todo app. It's a complete productivity coaching system that:

- **Predicts focus levels** based on time of day, session duration, and historical performance
- **Smart task prioritization** using AI scoring algorithms (urgency + effort + deadline proximity)
- **Tracks productivity metrics** with real-time scoring and insights
- **Suggests optimal breaks** based on focus session duration
- **Provides AI recommendations** for productivity improvements

### Key Features

✅ **Smart Task Manager** - AI auto-prioritizes tasks based on multiple factors  
🎯 **Focus Session Tracker** - Live timer with focus level prediction  
📊 **Productivity Dashboard** - Real-time metrics and AI insights  
📈 **Analytics & Insights** - 7-day trend analysis with AI recommendations  
🤖 **100% Local AI** - No external API costs, no OpenAI, no paid services

---

## 🛠️ Tech Stack

### Frontend
- **React 18** with Vite
- **Tailwind CSS** with custom design system
- **React Router** for navigation
- **Axios** for API calls
- **Custom fonts**: Space Grotesk, Manrope, JetBrains Mono

### Backend
- **Python Flask** REST API
- **SQLite** database
- **Local AI/ML** - Rule-based algorithms

### AI/ML Features
- **Focus Prediction Engine** - Predicts High/Medium/Low focus based on context
- **Task Prioritization Engine** - Calculates optimal priority scores
- **Productivity Analytics** - Generates insights and recommendations
- **Break Optimization** - Suggests ideal break durations

---

## 📦 Installation & Setup

### Prerequisites
- **Python 3.8+**
- **Node.js 16+** and npm
- Basic terminal/command line knowledge

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd focusmate-ai
```

### Step 2: Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the backend server
python app.py
```

The backend will start on `http://localhost:5000`

### Step 3: Frontend Setup

Open a **NEW terminal window** (keep backend running):

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The frontend will start on `http://localhost:3000`

### Step 4: Access the Application

Open your browser and navigate to:
```
http://localhost:3000
```

You should see the FocusMate AI dashboard! 🎉

---

## 🚀 Usage Guide

### Dashboard
- View your **productivity score** (0-100)
- See **today's stats** (tasks completed, focus sessions, focus minutes)
- Check **current AI-predicted focus level**
- Get **AI recommendations** for productivity
- View your **top 3 priority tasks** (AI-ranked)

### Tasks Manager
1. Click **"+ Add Task"**
2. Enter task details:
   - **Title**: What needs to be done
   - **Urgency**: 1-5 scale (how important)
   - **Effort**: 1-5 scale (how difficult)
   - **Deadline**: Optional due date
3. AI automatically calculates **priority score** and ranks tasks
4. Check off tasks when complete
5. Delete tasks as needed

**AI Priority Scoring Formula:**
```
Score = (Urgency/5 * 40) + (Deadline Proximity * 40) + ((6-Effort)/5 * 20)
```

### Focus Sessions
1. Select duration (15-90 minutes)
2. Click **"Start Focus Session"**
3. AI predicts your focus level (High/Medium/Low)
4. AI suggests optimal break duration
5. Track distractions during session
6. Complete or pause as needed

**AI Focus Prediction:**
- Analyzes **time of day** (morning = better focus)
- Considers **session duration** (25-45 min = optimal)
- Uses **historical completion rate**

### Insights
- View **7-day productivity trends**
- See **average daily metrics**
- Get **AI-powered analysis** of strengths and opportunities
- Track tasks completed, focus time, and sessions over time

---

## 🧠 AI/ML Logic Explained

### 1. Focus Prediction Engine

**Algorithm:**
```python
score = 0
# Time factor (0-40 points)
if morning_hours: score += 40
elif afternoon: score += 20
elif evening: score += 30

# Duration factor (0-35 points)
if 25 <= duration <= 45: score += 35

# Historical factor (0-25 points)
score += completion_rate * 25

# Classification
if score >= 70: return "High"
elif score >= 45: return "Medium"
else: return "Low"
```

### 2. Task Prioritization Engine

**Algorithm:**
```python
urgency_score = (urgency / 5) * 40
deadline_score = calculate_proximity(deadline)  # 0-50 points
effort_score = ((6 - effort) / 5) * 20  # Inverse: lower effort = higher priority

total_score = urgency_score + deadline_score + effort_score
```

### 3. Productivity Score

**Formula:**
```python
score = (tasks_completed * 10) + (focus_sessions * 15) + (focus_minutes * 0.5) - (distractions * 5)
score = max(0, min(100, score))  # Clamped to 0-100
```

### 4. Smart Recommendations

AI analyzes your data and provides contextual recommendations:
- Overdue task alerts
- High-urgency task prioritization
- Task load management
- Time-of-day optimization suggestions

---

## 📊 Product Metrics Tracked

| Metric | Description | Usage |
|--------|-------------|-------|
| **Productivity Score** | 0-100 daily score based on performance | Dashboard, Insights |
| **Tasks Completed** | Number of tasks marked complete | All pages |
| **Focus Sessions** | Number of completed focus sessions | Dashboard, Insights |
| **Focus Minutes** | Total minutes in focus mode | Dashboard, Insights |
| **Distraction Count** | Tracked interruptions during sessions | Focus, Insights |
| **AI Priority Score** | Calculated priority for each task | Tasks |
| **Focus Level** | AI-predicted focus quality | Dashboard, Focus |
| **Completion Rate** | % of tasks completed | Tasks |

---

## 🎨 Design Philosophy

**Premium SaaS Aesthetic:**
- **Dark mode by default** with cyber-blue and purple accents
- **Glassmorphism** panels with backdrop blur
- **Smooth animations** and micro-interactions
- **Custom fonts** for distinctive typography
- **Gradient effects** for visual interest
- **Responsive design** for all screen sizes

**Color Palette:**
- Deep Night (#0a0e1a) - Background
- Cyber Blue (#00d4ff) - Primary accent
- Focus Purple (#a855f7) - Secondary accent
- Success Green (#10b981) - Positive actions
- Warning Amber (#f59e0b) - Alerts
- Danger Red (#ef4444) - Critical items

---

## 📂 Project Structure

```
focusmate-ai/
├── backend/
│   ├── app.py              # Flask application + AI logic
│   ├── requirements.txt    # Python dependencies
│   └── focusmate.db       # SQLite database (auto-created)
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx      # Main dashboard
│   │   │   ├── Tasks.jsx          # Task manager
│   │   │   ├── FocusSession.jsx   # Focus timer
│   │   │   └── Insights.jsx       # Analytics
│   │   ├── App.jsx         # Main app + routing
│   │   ├── main.jsx        # Entry point
│   │   └── index.css       # Global styles
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── postcss.config.js
│
└── README.md              # This file
```

---

## 🔧 API Endpoints

### Health Check
- `GET /api/health` - Check if backend is running

### Tasks
- `GET /api/tasks` - Get all tasks (sorted by AI priority)
- `POST /api/tasks` - Create new task
- `PUT /api/tasks/:id` - Update task
- `DELETE /api/tasks/:id` - Delete task

### Focus Sessions
- `GET /api/focus-sessions` - Get recent focus sessions
- `POST /api/focus-sessions` - Start new session (returns AI prediction)
- `PUT /api/focus-sessions/:id` - Update/complete session

### Dashboard
- `GET /api/dashboard` - Get dashboard data (tasks, metrics, AI recommendations)

### Insights
- `GET /api/insights` - Get 7-day productivity analytics

---

## 🎯 Product Thinking

### Problem Statement
Users struggle to:
- Prioritize tasks effectively
- Maintain focus in distracting environments
- Understand their productivity patterns
- Optimize work sessions and breaks

### Solution
FocusMate AI provides:
- **Automated prioritization** - No mental overhead
- **Focus prediction** - Know when you'll perform best
- **Data-driven insights** - Understand your patterns
- **Smart recommendations** - Actionable improvements

### Value Proposition
- **Save time** on task management
- **Increase focus** with AI-guided sessions
- **Improve productivity** through data insights
- **No costs** - 100% local, no API fees

---

## 🚀 Future Enhancements

### Phase 2 Features
- [ ] Goal tracking system
- [ ] Pomodoro technique integration
- [ ] Team collaboration features
- [ ] Mobile app (React Native)
- [ ] Export reports (PDF)
- [ ] Custom themes
- [ ] Notification system
- [ ] Calendar integration

### Advanced AI Features
- [ ] Machine learning model for focus prediction
- [ ] Natural language task parsing
- [ ] Habit pattern recognition
- [ ] Personalized productivity coaching
- [ ] Time estimation AI

---

## 🤝 Contributing

This is a demonstration project showcasing:
- Product management thinking
- Full-stack development skills
- AI/ML integration (local)
- Premium UI/UX design
- Metrics-driven approach

---

## 📝 License

MIT License - Feel free to use this project as a learning resource or portfolio piece.

---

## 🏆 Key Achievements

✅ **Zero API Costs** - All AI logic runs locally  
✅ **Production-Ready UI** - Premium SaaS design  
✅ **Smart AI Features** - Prediction, prioritization, analytics  
✅ **Real Product Thinking** - Metrics, insights, recommendations  
✅ **Clean Architecture** - Modular, maintainable code  
✅ **Complete Documentation** - Easy setup and usage  

---

## 💡 Tips for Best Results

1. **Add tasks regularly** - AI needs data to prioritize effectively
2. **Complete focus sessions** - Improves AI prediction accuracy
3. **Track distractions honestly** - Better insights over time
4. **Check insights daily** - Learn from your patterns
5. **Follow AI recommendations** - They're based on your data

---

## 📞 Support

For issues or questions:
1. Check this README thoroughly
2. Ensure all dependencies are installed
3. Verify both frontend and backend are running
4. Check browser console for errors

---

## 🎓 Learning Outcomes

This project demonstrates:
- **Full-stack development** (React + Flask)
- **AI/ML integration** (local algorithms)
- **Database design** (SQLite)
- **API development** (REST)
- **Premium UI/UX** (Tailwind + custom design)
- **Product management** (metrics, user value)
- **Clean code practices** (modular, documented)

---

**Built with 🧠 and ☕ - FocusMate AI**

*Your intelligent productivity companion*
