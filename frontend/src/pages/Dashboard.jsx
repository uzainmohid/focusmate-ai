import { useState, useEffect } from 'react'
import axios from 'axios'

function ProductivityRing({ score }) {
  const radius = 70
  const circumference = 2 * Math.PI * radius
  const offset = circumference - (score / 100) * circumference

  const getColor = () => {
    if (score >= 80) return '#10b981'
    if (score >= 60) return '#00d4ff'
    if (score >= 40) return '#f59e0b'
    return '#ef4444'
  }

  return (
    <div className="relative w-48 h-48">
      <svg className="w-full h-full" viewBox="0 0 160 160">
        <circle
          cx="80"
          cy="80"
          r={radius}
          fill="none"
          stroke="rgba(255,255,255,0.1)"
          strokeWidth="12"
        />
        <circle
          cx="80"
          cy="80"
          r={radius}
          fill="none"
          stroke={getColor()}
          strokeWidth="12"
          strokeLinecap="round"
          strokeDasharray={circumference}
          strokeDashoffset={offset}
          className="transition-all duration-1000 ease-out"
          style={{ filter: `drop-shadow(0 0 10px ${getColor()})` }}
        />
      </svg>

      <div className="absolute inset-0 flex flex-col items-center justify-center">
        <div className="text-5xl font-display font-bold text-gradient">
          {score}
        </div>
        <div className="text-xs text-gray-400 font-mono">SCORE</div>
      </div>
    </div>
  )
}

/* 🔮 AI Focus Prediction Logic */
function getFocusPrediction(data) {
  if (!data) return null

  const { focus_sessions_today = 0, total_focus_minutes = 0 } = data

  if (total_focus_minutes >= 120) {
    return {
      window: 'Evening',
      message:
        'Your productivity spikes later in the day. Schedule deep work after sunset.'
    }
  }

  if (focus_sessions_today >= 2) {
    return {
      window: 'Afternoon',
      message:
        'Mid-day is your strongest focus zone. Protect it from distractions.'
    }
  }

  return {
    window: 'Morning',
    message:
      'Your focus is highest early in the day. Start with your hardest task.'
  }
}

/* 🧩 AI Productivity Persona Logic */
function getProductivityPersona(data) {
  if (!data) return null

  const { tasks_completed_today = 0, total_focus_minutes = 0, current_focus_level } = data

  if (total_focus_minutes >= 120 && current_focus_level === 'High') {
    return {
      persona: 'Deep Thinker',
      description:
        'You excel in long, focused sessions. Perfect for coding, writing, and analysis.'
    }
  }

  if (tasks_completed_today >= 5 && total_focus_minutes < 90) {
    return {
      persona: 'Sprinter',
      description:
        'You work best in short bursts. Quick wins and high-intensity tasks are your strength.'
    }
  }

  return {
    persona: 'Marathoner',
    description:
      'You maintain moderate focus consistently. Ideal for steady progress throughout the day.'
  }
}

function Dashboard() {
  const [dashboardData, setDashboardData] = useState(null)
  const [loading, setLoading] = useState(true)

  /* 🔥 AI Focus Tips */
  const focusTips = [
    'Start your day with a 25-minute deep focus sprint.',
    'Complete high-effort tasks before checking notifications.',
    'Short breaks improve long-term focus. Try 5 minutes.',
    'Focus on one task. Multitasking kills productivity.',
    'Your energy is highest in the first 3 hours — use it wisely.'
  ]

  const dailyTip =
    focusTips[Math.floor(Math.random() * focusTips.length)]

  useEffect(() => {
    fetchDashboard()
    const interval = setInterval(fetchDashboard, 30000)
    return () => clearInterval(interval)
  }, [])

  const fetchDashboard = async () => {
    try {
      const response = await axios.get('/api/dashboard')
      setDashboardData(response.data)
      setLoading(false)
    } catch (error) {
      console.error('Error fetching dashboard:', error)
      setLoading(false)
    }
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center h-96">
        <div className="text-center">
          <div className="w-16 h-16 border-4 border-cyber-blue/30 border-t-cyber-blue rounded-full animate-spin mx-auto mb-4"></div>
          <p className="text-gray-400">
            Loading your productivity data...
          </p>
        </div>
      </div>
    )
  }

  const focusPrediction = getFocusPrediction(dashboardData)
  const productivityPersona = getProductivityPersona(dashboardData)

  const getFocusLevelClass = (level) => {
    if (level === 'High') return 'focus-level-high'
    if (level === 'Medium') return 'focus-level-medium'
    return 'focus-level-low'
  }

  return (
    <div className="animate-fade-in">

      {/* Hero Section: Welcome Back First */}
      <div className="glass-panel p-8 mb-8 relative overflow-hidden">
        <div className="absolute top-0 right-0 w-96 h-96 bg-gradient-focus opacity-10 blur-3xl rounded-full"></div>
        <div className="relative z-10 flex flex-col sm:flex-row items-center justify-between gap-6">
          <div>
            <h2 className="text-4xl font-display font-bold mb-2">
              Welcome back, <span className="text-gradient">Champion</span>
            </h2>
            <p className="text-gray-400 text-lg">
              {dashboardData?.productivity_insight ||
                'Ready to crush your goals today?'}
            </p>
          </div>
          <ProductivityRing
            score={dashboardData?.productivity_score || 0}
          />
        </div>
      </div>

      {/* Triple AI Features Section */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-8">
        {/* AI Focus Tip */}
        <div className="glass-panel p-4 sm:p-6">
          <p className="text-xs text-gray-400 mb-1 font-mono">AI FOCUS TIP</p>
          <h3 className="text-base sm:text-lg font-semibold text-white leading-snug">
            🧠 {dailyTip}
          </h3>
        </div>

        {/* AI Focus Prediction */}
        {focusPrediction && (
          <div className="glass-panel p-4 sm:p-6 border border-cyber-blue/20">
            <p className="text-xs text-gray-400 mb-1 font-mono">
              AI FOCUS PREDICTION
            </p>
            <h3 className="text-lg font-semibold text-white">
              Best focus window:{' '}
              <span className="text-cyber-blue">{focusPrediction.window}</span>
            </h3>
            <p className="text-sm text-gray-400 mt-1 max-w-2xl">
              {focusPrediction.message}
            </p>
          </div>
        )}

        {/* AI Productivity Persona */}
        {productivityPersona && (
          <div className="glass-panel p-4 sm:p-6 border border-cyber-blue/20">
            <p className="text-xs text-gray-400 mb-1 font-mono">
              AI PRODUCTIVITY PERSONA
            </p>
            <h3 className="text-lg font-semibold text-white">
              {productivityPersona.persona}
            </h3>
            <p className="text-sm text-gray-400 mt-1 max-w-2xl">
              {productivityPersona.description}
            </p>
          </div>
        )}
      </div>

      {/* Stats Section */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <div className="metric-card group animate-slide-up">
          <div className="flex items-center justify-between mb-4">
            <div className="text-4xl">✓</div>
            <div className="text-3xl font-display font-bold text-success-green">
              {dashboardData?.tasks_completed_today || 0}
            </div>
          </div>
          <div className="text-sm text-gray-400">Tasks Completed</div>
          <div className="mt-2 text-xs text-success-green font-mono">TODAY</div>
        </div>

        <div className="metric-card group animate-slide-up">
          <div className="flex items-center justify-between mb-4">
            <div className="text-4xl">🎯</div>
            <div className="text-3xl font-display font-bold text-cyber-blue">
              {dashboardData?.focus_sessions_today || 0}
            </div>
          </div>
          <div className="text-sm text-gray-400">Focus Sessions</div>
          <div className="mt-2 text-xs text-cyber-blue font-mono">TODAY</div>
        </div>

        <div className="metric-card group animate-slide-up">
          <div className="flex items-center justify-between mb-4">
            <div className="text-4xl">⏱️</div>
            <div className="text-3xl font-display font-bold text-focus-purple">
              {dashboardData?.total_focus_minutes || 0}
            </div>
          </div>
          <div className="text-sm text-gray-400">Focus Minutes</div>
          <div className="mt-2 text-xs text-focus-purple font-mono">TODAY</div>
        </div>

        <div className="metric-card group animate-slide-up">
          <div className="flex items-center justify-between mb-4">
            <div className="text-4xl">🧠</div>
            <div
              className={`text-3xl font-display font-bold ${getFocusLevelClass(
                dashboardData?.current_focus_level
              )}`}
            >
              {dashboardData?.current_focus_level || 'N/A'}
            </div>
          </div>
          <div className="text-sm text-gray-400">Current Focus</div>
          <div className="mt-2 text-xs text-gray-500 font-mono">AI PREDICTED</div>
        </div>
      </div>
    </div>
  )
}

export default Dashboard
