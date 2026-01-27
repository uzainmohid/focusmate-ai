import { useState, useEffect, useRef } from 'react'
import axios from 'axios'

function FocusSession() {
  const [duration, setDuration] = useState(25)
  const [isRunning, setIsRunning] = useState(false)
  const [timeLeft, setTimeLeft] = useState(25 * 60)
  const [currentSession, setCurrentSession] = useState(null)
  const [distractions, setDistractions] = useState(0)
  const [focusLevel, setFocusLevel] = useState(null)
  const [optimalBreak, setOptimalBreak] = useState(5)
  const intervalRef = useRef(null)
  
  useEffect(() => {
    if (isRunning && timeLeft > 0) {
      intervalRef.current = setInterval(() => {
        setTimeLeft((prev) => prev - 1)
      }, 1000)
    } else if (timeLeft === 0) {
      completeSession()
    }
    
    return () => clearInterval(intervalRef.current)
  }, [isRunning, timeLeft])
  
  const startSession = async () => {
    try {
      const response = await axios.post('/api/focus-sessions', {
        duration,
        start_time: new Date().toISOString(),
        distractions: 0,
        completed: false
      })
      
      setCurrentSession(response.data)
      setFocusLevel(response.data.focus_level)
      setOptimalBreak(response.data.optimal_break)
      setTimeLeft(duration * 60)
      setDistractions(0)
      setIsRunning(true)
    } catch (error) {
      console.error('Error starting session:', error)
    }
  }
  
  const pauseSession = () => {
    setIsRunning(false)
  }
  
  const resumeSession = () => {
    setIsRunning(true)
  }
  
  const completeSession = async () => {
    if (!currentSession) return
    
    try {
      await axios.put(`/api/focus-sessions/${currentSession.id}`, {
        end_time: new Date().toISOString(),
        completed: true,
        distractions
      })
      
      setIsRunning(false)
      setCurrentSession(null)
      setTimeLeft(duration * 60)
      // Show completion animation/message
      setTimeout(() => {
        alert(`🎉 Focus session complete! Take a ${optimalBreak}-minute break.`)
      }, 100)
    } catch (error) {
      console.error('Error completing session:', error)
    }
  }
  
  const addDistraction = () => {
    setDistractions((prev) => prev + 1)
  }
  
  const formatTime = (seconds) => {
    const mins = Math.floor(seconds / 60)
    const secs = seconds % 60
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`
  }
  
  const getProgress = () => {
    const total = duration * 60
    return ((total - timeLeft) / total) * 100
  }
  
  const getFocusLevelColor = () => {
    if (focusLevel === 'High') return '#10b981'
    if (focusLevel === 'Medium') return '#f59e0b'
    return '#ef4444'
  }
  
  const presetDurations = [15, 25, 30, 45, 60]
  
  return (
    <div className="animate-fade-in">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <div className="glass-panel p-6 mb-8">
          <h2 className="text-3xl font-display font-bold mb-2">Focus Session</h2>
          <p className="text-gray-400">Deep work mode with AI-powered focus tracking</p>
        </div>
        
        {!isRunning && !currentSession ? (
          /* Setup Screen */
          <div className="glass-panel p-12">
            <div className="text-center mb-8">
              <div className="text-8xl mb-6 animate-float">🎯</div>
              <h3 className="text-3xl font-display font-bold mb-3">Ready to Focus?</h3>
              <p className="text-gray-400 text-lg">Choose your focus duration and start deep work</p>
            </div>
            
            {/* Duration Selection */}
            <div className="mb-8">
              <label className="block text-center text-sm font-semibold text-gray-400 mb-4">
                Select Duration (minutes)
              </label>
              <div className="flex justify-center gap-3 mb-6">
                {presetDurations.map((preset) => (
                  <button
                    key={preset}
                    onClick={() => setDuration(preset)}
                    className={`px-6 py-3 rounded-xl font-semibold transition-all duration-300 ${
                      duration === preset
                        ? 'bg-gradient-focus text-white shadow-lg shadow-cyber-blue/30 scale-110'
                        : 'bg-slate-deep/60 text-gray-300 hover:bg-slate-deep hover:scale-105'
                    }`}
                  >
                    {preset}
                  </button>
                ))}
              </div>
              
              <div className="max-w-md mx-auto">
                <input
                  type="range"
                  min="5"
                  max="90"
                  step="5"
                  value={duration}
                  onChange={(e) => setDuration(parseInt(e.target.value))}
                  className="w-full mb-2"
                />
                <div className="text-center">
                  <span className="text-5xl font-display font-bold text-gradient">{duration}</span>
                  <span className="text-gray-400 ml-2">minutes</span>
                </div>
              </div>
            </div>
            
            {/* AI Prediction Box */}
            <div className="max-w-md mx-auto mb-8 p-6 bg-gradient-to-r from-cyber-blue/10 to-focus-purple/10 
                          rounded-2xl border border-cyber-blue/20">
              <div className="flex items-center gap-3 mb-3">
                <span className="text-2xl">🤖</span>
                <span className="font-semibold text-cyber-blue">AI Focus Prediction</span>
              </div>
              <p className="text-gray-400 text-sm">
                Based on your session duration and time of day, AI will predict your focus level 
                and suggest optimal break times.
              </p>
            </div>
            
            <div className="text-center">
              <button onClick={startSession} className="btn-primary text-xl px-12 py-4">
                Start Focus Session
              </button>
            </div>
          </div>
        ) : (
          /* Active Session Screen */
          <div className="glass-panel p-12 relative overflow-hidden">
            {/* Animated background based on focus level */}
            <div 
              className="absolute inset-0 opacity-10 blur-3xl transition-all duration-1000"
              style={{ 
                background: `radial-gradient(circle at 50% 50%, ${getFocusLevelColor()} 0%, transparent 70%)`
              }}
            ></div>
            
            <div className="relative z-10">
              {/* Timer Display */}
              <div className="text-center mb-12">
                <div className="relative inline-block">
                  {/* Progress Ring */}
                  <svg className="w-80 h-80" viewBox="0 0 200 200">
                    <circle
                      cx="100"
                      cy="100"
                      r="85"
                      fill="none"
                      stroke="rgba(255,255,255,0.1)"
                      strokeWidth="8"
                    />
                    <circle
                      cx="100"
                      cy="100"
                      r="85"
                      fill="none"
                      stroke={getFocusLevelColor()}
                      strokeWidth="8"
                      strokeLinecap="round"
                      strokeDasharray={`${2 * Math.PI * 85}`}
                      strokeDashoffset={`${2 * Math.PI * 85 * (1 - getProgress() / 100)}`}
                      className="progress-ring transition-all duration-1000"
                      style={{ filter: `drop-shadow(0 0 20px ${getFocusLevelColor()})` }}
                    />
                  </svg>
                  
                  <div className="absolute inset-0 flex flex-col items-center justify-center">
                    <div className="text-7xl font-display font-bold text-white mb-2 font-mono">
                      {formatTime(timeLeft)}
                    </div>
                    <div className="text-sm text-gray-400 font-mono">
                      {Math.round(getProgress())}% COMPLETE
                    </div>
                  </div>
                </div>
              </div>
              
              {/* Focus Info Bar */}
              <div className="grid grid-cols-3 gap-4 mb-8">
                <div className="glass-panel p-4 text-center">
                  <div className="text-sm text-gray-400 mb-2">Focus Level</div>
                  <div 
                    className="text-2xl font-display font-bold"
                    style={{ color: getFocusLevelColor() }}
                  >
                    {focusLevel}
                  </div>
                  <div className="text-xs text-gray-500 mt-1 font-mono">AI PREDICTED</div>
                </div>
                
                <div className="glass-panel p-4 text-center">
                  <div className="text-sm text-gray-400 mb-2">Distractions</div>
                  <div className="text-2xl font-display font-bold text-danger-red">
                    {distractions}
                  </div>
                  <button 
                    onClick={addDistraction}
                    className="text-xs text-gray-500 mt-1 hover:text-danger-red transition-colors"
                  >
                    + Add Distraction
                  </button>
                </div>
                
                <div className="glass-panel p-4 text-center">
                  <div className="text-sm text-gray-400 mb-2">Break After</div>
                  <div className="text-2xl font-display font-bold text-cyber-blue">
                    {optimalBreak}m
                  </div>
                  <div className="text-xs text-gray-500 mt-1 font-mono">RECOMMENDED</div>
                </div>
              </div>
              
              {/* Controls */}
              <div className="flex justify-center gap-4">
                {isRunning ? (
                  <button onClick={pauseSession} className="btn-secondary px-12 py-4 text-lg">
                    ⏸️ Pause
                  </button>
                ) : (
                  <button onClick={resumeSession} className="btn-primary px-12 py-4 text-lg">
                    ▶️ Resume
                  </button>
                )}
                <button onClick={completeSession} className="btn-secondary px-12 py-4 text-lg">
                  ⏹️ End Session
                </button>
              </div>
              
              {/* Tips */}
              <div className="mt-8 p-4 bg-slate-deep/40 rounded-xl border border-white/5">
                <div className="flex items-start gap-3">
                  <span className="text-xl">💡</span>
                  <div>
                    <div className="font-semibold text-gray-300 mb-1">Focus Tips</div>
                    <ul className="text-sm text-gray-400 space-y-1">
                      <li>• Silence notifications on all devices</li>
                      <li>• Keep water nearby to stay hydrated</li>
                      <li>• Take the recommended break after the session</li>
                      <li>• Track distractions to improve future sessions</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default FocusSession
