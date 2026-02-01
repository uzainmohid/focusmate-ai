// import { useState, useEffect } from 'react'
// import axios from 'axios'

// function Insights() {
//   const [insights, setInsights] = useState([])
//   const [loading, setLoading] = useState(true)
  
//   useEffect(() => {
//     fetchInsights()
//   }, [])
  
//   const fetchInsights = async () => {
//     try {
//       const response = await axios.get('/api/insights')
//       setInsights(response.data)
//       setLoading(false)
//     } catch (error) {
//       console.error('Error fetching insights:', error)
//       setLoading(false)
//     }
//   }
  
//   const formatDate = (dateStr) => {
//     const date = new Date(dateStr)
//     const today = new Date()
//     const yesterday = new Date(today)
//     yesterday.setDate(yesterday.getDate() - 1)
    
//     if (date.toDateString() === today.toDateString()) return 'Today'
//     if (date.toDateString() === yesterday.toDateString()) return 'Yesterday'
//     return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
//   }
  
//   const getScoreColor = (score) => {
//     if (score >= 80) return '#10b981'
//     if (score >= 60) return '#00d4ff'
//     if (score >= 40) return '#f59e0b'
//     return '#ef4444'
//   }
  
//   const calculateAverage = (key) => {
//     if (insights.length === 0) return 0
//     const sum = insights.reduce((acc, day) => acc + day[key], 0)
//     return Math.round(sum / insights.length)
//   }
  
//   const maxScore = Math.max(...insights.map(d => d.productivity_score), 100)
  
//   if (loading) {
//     return (
//       <div className="flex items-center justify-center h-96">
//         <div className="text-center">
//           <div className="w-16 h-16 border-4 border-cyber-blue/30 border-t-cyber-blue rounded-full animate-spin mx-auto mb-4"></div>
//           <p className="text-gray-400">Analyzing your productivity data...</p>
//         </div>
//       </div>
//     )
//   }
  
//   return (
//     <div className="animate-fade-in">
//       {/* Header */}
//       <div className="glass-panel p-6 mb-8">
//         <h2 className="text-3xl font-display font-bold mb-2">Productivity Insights</h2>
//         <p className="text-gray-400">AI-powered analytics of your focus patterns and performance</p>
//       </div>
      
//       {/* Summary Stats */}
//       <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
//         <div className="metric-card">
//           <div className="flex items-center justify-between mb-3">
//             <span className="text-3xl">📊</span>
//             <div className="text-3xl font-display font-bold text-cyber-blue">
//               {calculateAverage('productivity_score')}
//             </div>
//           </div>
//           <div className="text-sm text-gray-400">Avg. Daily Score</div>
//           <div className="mt-2 text-xs text-gray-500 font-mono">7-DAY AVERAGE</div>
//         </div>
        
//         <div className="metric-card">
//           <div className="flex items-center justify-between mb-3">
//             <span className="text-3xl">✓</span>
//             <div className="text-3xl font-display font-bold text-success-green">
//               {calculateAverage('tasks_completed')}
//             </div>
//           </div>
//           <div className="text-sm text-gray-400">Avg. Tasks/Day</div>
//           <div className="mt-2 text-xs text-gray-500 font-mono">7-DAY AVERAGE</div>
//         </div>
        
//         <div className="metric-card">
//           <div className="flex items-center justify-between mb-3">
//             <span className="text-3xl">⏱️</span>
//             <div className="text-3xl font-display font-bold text-focus-purple">
//               {calculateAverage('focus_minutes')}
//             </div>
//           </div>
//           <div className="text-sm text-gray-400">Avg. Focus Minutes</div>
//           <div className="mt-2 text-xs text-gray-500 font-mono">7-DAY AVERAGE</div>
//         </div>
        
//         <div className="metric-card">
//           <div className="flex items-center justify-between mb-3">
//             <span className="text-3xl">🎯</span>
//             <div className="text-3xl font-display font-bold text-warning-amber">
//               {calculateAverage('focus_sessions')}
//             </div>
//           </div>
//           <div className="text-sm text-gray-400">Avg. Sessions/Day</div>
//           <div className="mt-2 text-xs text-gray-500 font-mono">7-DAY AVERAGE</div>
//         </div>
//       </div>
      
//       {/* Productivity Score Chart */}
//       <div className="glass-panel p-8 mb-8">
//         <div className="flex items-center justify-between mb-6">
//           <h3 className="text-2xl font-display font-bold">Productivity Score Trend</h3>
//           <div className="ai-badge">
//             <span>🤖</span>
//             <span>AI Calculated</span>
//           </div>
//         </div>
        
//         <div className="space-y-4">
//           {insights.map((day, index) => (
//             <div 
//               key={index} 
//               className="animate-slide-up"
//               style={{ animationDelay: `${index * 0.1}s` }}
//             >
//               <div className="flex items-center justify-between mb-2">
//                 <div className="flex items-center gap-4 flex-1">
//                   <div className="w-24 text-sm font-semibold text-gray-400">
//                     {formatDate(day.date)}
//                   </div>
//                   <div className="flex-1">
//                     <div className="h-12 bg-slate-deep/40 rounded-xl overflow-hidden relative">
//                       <div 
//                         className="h-full rounded-xl transition-all duration-1000 flex items-center justify-end pr-4 font-display font-bold"
//                         style={{ 
//                           width: `${(day.productivity_score / maxScore) * 100}%`,
//                           background: `linear-gradient(90deg, ${getScoreColor(day.productivity_score)}88, ${getScoreColor(day.productivity_score)})`,
//                           boxShadow: `0 0 20px ${getScoreColor(day.productivity_score)}44`
//                         }}
//                       >
//                         {day.productivity_score > 0 && (
//                           <span className="text-white text-lg">{day.productivity_score}</span>
//                         )}
//                       </div>
//                     </div>
//                   </div>
//                 </div>
//               </div>
              
//               {/* Daily details */}
//               <div className="ml-28 flex gap-6 text-xs text-gray-500">
//                 <span>✓ {day.tasks_completed} tasks</span>
//                 <span>🎯 {day.focus_sessions} sessions</span>
//                 <span>⏱️ {day.focus_minutes}m focus</span>
//                 {day.distractions > 0 && (
//                   <span className="text-danger-red">⚠️ {day.distractions} distractions</span>
//                 )}
//               </div>
//             </div>
//           ))}
//         </div>
        
//         {insights.length === 0 && (
//           <div className="text-center py-12 text-gray-500">
//             <div className="text-6xl mb-4">📈</div>
//             <p>No data yet. Start completing tasks and focus sessions to see insights!</p>
//           </div>
//         )}
//       </div>
      
//       {/* Detailed Metrics Grid */}
//       {insights.length > 0 && (
//         <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
//           {/* Tasks Completed Over Time */}
//           <div className="glass-panel p-6">
//             <h3 className="text-xl font-display font-bold mb-4">Tasks Completion</h3>
//             <div className="space-y-3">
//               {insights.map((day, index) => (
//                 <div key={index} className="flex items-center gap-4">
//                   <div className="w-20 text-xs text-gray-500">{formatDate(day.date)}</div>
//                   <div className="flex-1 bg-slate-deep/40 rounded-lg h-8 overflow-hidden">
//                     <div 
//                       className="h-full bg-gradient-to-r from-success-green to-success-green/60 flex items-center justify-end pr-3 text-white text-sm font-semibold transition-all duration-700"
//                       style={{ width: `${(day.tasks_completed / Math.max(...insights.map(d => d.tasks_completed), 10)) * 100}%` }}
//                     >
//                       {day.tasks_completed > 0 && day.tasks_completed}
//                     </div>
//                   </div>
//                 </div>
//               ))}
//             </div>
//           </div>
          
//           {/* Focus Time Over Time */}
//           <div className="glass-panel p-6">
//             <h3 className="text-xl font-display font-bold mb-4">Focus Time (minutes)</h3>
//             <div className="space-y-3">
//               {insights.map((day, index) => (
//                 <div key={index} className="flex items-center gap-4">
//                   <div className="w-20 text-xs text-gray-500">{formatDate(day.date)}</div>
//                   <div className="flex-1 bg-slate-deep/40 rounded-lg h-8 overflow-hidden">
//                     <div 
//                       className="h-full bg-gradient-to-r from-focus-purple to-focus-purple/60 flex items-center justify-end pr-3 text-white text-sm font-semibold transition-all duration-700"
//                       style={{ width: `${(day.focus_minutes / Math.max(...insights.map(d => d.focus_minutes), 100)) * 100}%` }}
//                     >
//                       {day.focus_minutes > 0 && day.focus_minutes}
//                     </div>
//                   </div>
//                 </div>
//               ))}
//             </div>
//           </div>
//         </div>
//       )}
      
//       {/* AI Insights Panel */}
//       <div className="mt-8 glass-panel p-8">
//         <div className="flex items-center gap-3 mb-6">
//           <span className="text-3xl">🤖</span>
//           <h3 className="text-2xl font-display font-bold">AI Analysis</h3>
//         </div>
        
//         <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
//           <div className="p-6 bg-slate-deep/40 rounded-xl border border-cyan-500/20">
//             <div className="text-cyan-400 font-semibold mb-3">💪 Strengths</div>
//             {insights.length > 3 ? (
//               <ul className="text-sm text-gray-300 space-y-2">
//                 {calculateAverage('productivity_score') >= 60 && (
//                   <li>• Consistent productivity levels maintained</li>
//                 )}
//                 {calculateAverage('focus_sessions') >= 2 && (
//                   <li>• Strong focus session habit established</li>
//                 )}
//                 {calculateAverage('tasks_completed') >= 3 && (
//                   <li>• High task completion rate</li>
//                 )}
//                 {insights.filter(d => d.productivity_score >= 70).length >= 3 && (
//                   <li>• Multiple high-performance days achieved</li>
//                 )}
//               </ul>
//             ) : (
//               <p className="text-sm text-gray-400">Complete more tasks and sessions for personalized insights</p>
//             )}
//           </div>
          
//           <div className="p-6 bg-slate-deep/40 rounded-xl border border-purple-500/20">
//             <div className="text-purple-400 font-semibold mb-3">🎯 Opportunities</div>
//             {insights.length > 3 ? (
//               <ul className="text-sm text-gray-300 space-y-2">
//                 {calculateAverage('focus_minutes') < 60 && (
//                   <li>• Increase daily focus time for better results</li>
//                 )}
//                 {insights.some(d => d.distractions > 3) && (
//                   <li>• Reduce distractions during focus sessions</li>
//                 )}
//                 {calculateAverage('tasks_completed') < 3 && (
//                   <li>• Break large tasks into smaller chunks</li>
//                 )}
//                 {insights.filter(d => d.focus_sessions === 0).length > 2 && (
//                   <li>• Schedule consistent focus sessions daily</li>
//                 )}
//               </ul>
//             ) : (
//               <p className="text-sm text-gray-400">Keep tracking to receive improvement suggestions</p>
//             )}
//           </div>
//         </div>
//       </div>
//     </div>
//   )
// }

// export default Insights

import { useState, useEffect } from 'react'
import { api } from '../api'  // ✅ FIXED

function Insights() {
  const [insights, setInsights] = useState([])
  const [loading, setLoading] = useState(true)
  
  useEffect(() => {
    fetchInsights()
  }, [])
  
  const fetchInsights = async () => {
    try {
      const response = await api.get('/api/insights')  // ✅ FIXED
      setInsights(response.data)
      setLoading(false)
    } catch (error) {
      console.error('Error fetching insights:', error)
      setLoading(false)
    }
  }
  
  const formatDate = (dateStr) => {
    const date = new Date(dateStr)
    const today = new Date()
    const yesterday = new Date(today)
    yesterday.setDate(yesterday.getDate() - 1)
    
    if (date.toDateString() === today.toDateString()) return 'Today'
    if (date.toDateString() === yesterday.toDateString()) return 'Yesterday'
    return date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
  }
  
  const getScoreColor = (score) => {
    if (score >= 80) return '#10b981'
    if (score >= 60) return '#00d4ff'
    if (score >= 40) return '#f59e0b'
    return '#ef4444'
  }
  
  const calculateAverage = (key) => {
    if (insights.length === 0) return 0
    const sum = insights.reduce((acc, day) => acc + day[key], 0)
    return Math.round(sum / insights.length)
  }
  
  const maxScore = Math.max(...insights.map(d => d.productivity_score), 100)
  
  if (loading) {
    return (
      <div className="flex items-center justify-center h-96">
        <div className="text-center">
          <div className="w-16 h-16 border-4 border-cyber-blue/30 border-t-cyber-blue rounded-full animate-spin mx-auto mb-4"></div>
          <p className="text-gray-400">Analyzing your productivity data...</p>
        </div>
      </div>
    )
  }
  
  return (
    <div className="animate-fade-in">
      <div className="glass-panel p-6 mb-8">
        <h2 className="text-3xl font-display font-bold mb-2">Productivity Insights</h2>
        <p className="text-gray-400">AI-powered analytics of your focus patterns and performance</p>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <div className="metric-card">
          <div className="flex items-center justify-between mb-3">
            <span className="text-3xl">📊</span>
            <div className="text-3xl font-display font-bold text-cyber-blue">
              {calculateAverage('productivity_score')}
            </div>
          </div>
          <div className="text-sm text-gray-400">Avg. Daily Score</div>
          <div className="mt-2 text-xs text-gray-500 font-mono">7-DAY AVERAGE</div>
        </div>
        
        <div className="metric-card">
          <div className="flex items-center justify-between mb-3">
            <span className="text-3xl">✓</span>
            <div className="text-3xl font-display font-bold text-success-green">
              {calculateAverage('tasks_completed')}
            </div>
          </div>
          <div className="text-sm text-gray-400">Avg. Tasks/Day</div>
          <div className="mt-2 text-xs text-gray-500 font-mono">7-DAY AVERAGE</div>
        </div>
        
        <div className="metric-card">
          <div className="flex items-center justify-between mb-3">
            <span className="text-3xl">⏱️</span>
            <div className="text-3xl font-display font-bold text-focus-purple">
              {calculateAverage('focus_minutes')}
            </div>
          </div>
          <div className="text-sm text-gray-400">Avg. Focus Minutes</div>
          <div className="mt-2 text-xs text-gray-500 font-mono">7-DAY AVERAGE</div>
        </div>
        
        <div className="metric-card">
          <div className="flex items-center justify-between mb-3">
            <span className="text-3xl">🎯</span>
            <div className="text-3xl font-display font-bold text-warning-amber">
              {calculateAverage('focus_sessions')}
            </div>
          </div>
          <div className="text-sm text-gray-400">Avg. Sessions/Day</div>
          <div className="mt-2 text-xs text-gray-500 font-mono">7-DAY AVERAGE</div>
        </div>
      </div>
      
      <div className="glass-panel p-8 mb-8">
        <div className="flex items-center justify-between mb-6">
          <h3 className="text-2xl font-display font-bold">Productivity Score Trend</h3>
          <div className="ai-badge">
            <span>🤖</span>
            <span>AI Calculated</span>
          </div>
        </div>
        
        <div className="space-y-4">
          {insights.map((day, index) => (
            <div 
              key={index} 
              className="animate-slide-up"
              style={{ animationDelay: `${index * 0.1}s` }}
            >
              <div className="flex items-center justify-between mb-2">
                <div className="flex items-center gap-4 flex-1">
                  <div className="w-24 text-sm font-semibold text-gray-400">
                    {formatDate(day.date)}
                  </div>
                  <div className="flex-1">
                    <div className="h-12 bg-slate-deep/40 rounded-xl overflow-hidden relative">
                      <div 
                        className="h-full rounded-xl transition-all duration-1000 flex items-center justify-end pr-4 font-display font-bold"
                        style={{ 
                          width: `${(day.productivity_score / maxScore) * 100}%`,
                          background: `linear-gradient(90deg, ${getScoreColor(day.productivity_score)}88, ${getScoreColor(day.productivity_score)})`,
                          boxShadow: `0 0 20px ${getScoreColor(day.productivity_score)}44`
                        }}
                      >
                        {day.productivity_score > 0 && (
                          <span className="text-white text-lg">{day.productivity_score}</span>
                        )}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              
              <div className="ml-28 flex gap-6 text-xs text-gray-500">
                <span>✓ {day.tasks_completed} tasks</span>
                <span>🎯 {day.focus_sessions} sessions</span>
                <span>⏱️ {day.focus_minutes}m focus</span>
                {day.distractions > 0 && (
                  <span className="text-danger-red">⚠️ {day.distractions} distractions</span>
                )}
              </div>
            </div>
          ))}
        </div>
        
        {insights.length === 0 && (
          <div className="text-center py-12 text-gray-500">
            <div className="text-6xl mb-4">📈</div>
            <p>No data yet. Start completing tasks and focus sessions to see insights!</p>
          </div>
        )}
      </div>
      
      {insights.length > 0 && (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <div className="glass-panel p-6">
            <h3 className="text-xl font-display font-bold mb-4">Tasks Completion</h3>
            <div className="space-y-3">
              {insights.map((day, index) => (
                <div key={index} className="flex items-center gap-4">
                  <div className="w-20 text-xs text-gray-500">{formatDate(day.date)}</div>
                  <div className="flex-1 bg-slate-deep/40 rounded-lg h-8 overflow-hidden">
                    <div 
                      className="h-full bg-gradient-to-r from-success-green to-success-green/60 flex items-center justify-end pr-3 text-white text-sm font-semibold transition-all duration-700"
                      style={{ width: `${(day.tasks_completed / Math.max(...insights.map(d => d.tasks_completed), 10)) * 100}%` }}
                    >
                      {day.tasks_completed > 0 && day.tasks_completed}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
          
          <div className="glass-panel p-6">
            <h3 className="text-xl font-display font-bold mb-4">Focus Time (minutes)</h3>
            <div className="space-y-3">
              {insights.map((day, index) => (
                <div key={index} className="flex items-center gap-4">
                  <div className="w-20 text-xs text-gray-500">{formatDate(day.date)}</div>
                  <div className="flex-1 bg-slate-deep/40 rounded-lg h-8 overflow-hidden">
                    <div 
                      className="h-full bg-gradient-to-r from-focus-purple to-focus-purple/60 flex items-center justify-end pr-3 text-white text-sm font-semibold transition-all duration-700"
                      style={{ width: `${(day.focus_minutes / Math.max(...insights.map(d => d.focus_minutes), 100)) * 100}%` }}
                    >
                      {day.focus_minutes > 0 && day.focus_minutes}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
      
      <div className="mt-8 glass-panel p-8">
        <div className="flex items-center gap-3 mb-6">
          <span className="text-3xl">🤖</span>
          <h3 className="text-2xl font-display font-bold">AI Analysis</h3>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="p-6 bg-slate-deep/40 rounded-xl border border-cyan-500/20">
            <div className="text-cyan-400 font-semibold mb-3">💪 Strengths</div>
            {insights.length > 3 ? (
              <ul className="text-sm text-gray-300 space-y-2">
                {calculateAverage('productivity_score') >= 60 && (
                  <li>• Consistent productivity levels maintained</li>
                )}
                {calculateAverage('focus_sessions') >= 2 && (
                  <li>• Strong focus session habit established</li>
                )}
                {calculateAverage('tasks_completed') >= 3 && (
                  <li>• High task completion rate</li>
                )}
                {insights.filter(d => d.productivity_score >= 70).length >= 3 && (
                  <li>• Multiple high-performance days achieved</li>
                )}
              </ul>
            ) : (
              <p className="text-sm text-gray-400">Complete more tasks and sessions for personalized insights</p>
            )}
          </div>
          
          <div className="p-6 bg-slate-deep/40 rounded-xl border border-purple-500/20">
            <div className="text-purple-400 font-semibold mb-3">🎯 Opportunities</div>
            {insights.length > 3 ? (
              <ul className="text-sm text-gray-300 space-y-2">
                {calculateAverage('focus_minutes') < 60 && (
                  <li>• Increase daily focus time for better results</li>
                )}
                {insights.some(d => d.distractions > 3) && (
                  <li>• Reduce distractions during focus sessions</li>
                )}
                {calculateAverage('tasks_completed') < 3 && (
                  <li>• Break large tasks into smaller chunks</li>
                )}
                {insights.filter(d => d.focus_sessions === 0).length > 2 && (
                  <li>• Schedule consistent focus sessions daily</li>
                )}
              </ul>
            ) : (
              <p className="text-sm text-gray-400">Keep tracking to receive improvement suggestions</p>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

export default Insights