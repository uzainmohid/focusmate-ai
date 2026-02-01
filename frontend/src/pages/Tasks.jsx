// import { useState, useEffect } from 'react'
// import axios from 'axios'

// function Tasks() {
//   const [tasks, setTasks] = useState([])
//   const [showAddModal, setShowAddModal] = useState(false)
//   const [newTask, setNewTask] = useState({
//     title: '',
//     urgency: 3,
//     effort: 3,
//     deadline: ''
//   })
  
//   useEffect(() => {
//     fetchTasks()
//   }, [])
  
//   const fetchTasks = async () => {
//     try {
//       const response = await axios.get('/api/tasks')
//       setTasks(response.data)
//     } catch (error) {
//       console.error('Error fetching tasks:', error)
//     }
//   }
  
//   const addTask = async () => {
//     if (!newTask.title.trim()) return
    
//     try {
//       await axios.post('/api/tasks', newTask)
//       setNewTask({ title: '', urgency: 3, effort: 3, deadline: '' })
//       setShowAddModal(false)
//       fetchTasks()
//     } catch (error) {
//       console.error('Error adding task:', error)
//     }
//   }
  
//   const toggleTask = async (taskId, completed) => {
//     try {
//       await axios.put(`/api/tasks/${taskId}`, { completed: !completed })
//       fetchTasks()
//     } catch (error) {
//       console.error('Error updating task:', error)
//     }
//   }
  
//   const deleteTask = async (taskId) => {
//     try {
//       await axios.delete(`/api/tasks/${taskId}`)
//       fetchTasks()
//     } catch (error) {
//       console.error('Error deleting task:', error)
//     }
//   }
  
//   const getPriorityBadge = (score) => {
//     if (score >= 40) return <span className="priority-badge-high">High Priority</span>
//     if (score >= 25) return <span className="priority-badge-medium">Medium</span>
//     return <span className="priority-badge-low">Low</span>
//   }
  
//   const pendingTasks = tasks.filter(t => !t.completed)
//   const completedTasks = tasks.filter(t => t.completed)
  
//   return (
//     <div className="animate-fade-in">
//       {/* Header */}
//       <div className="glass-panel p-6 mb-8">
//         <div className="flex items-center justify-between">
//           <div>
//             <h2 className="text-3xl font-display font-bold mb-2">Smart Task Manager</h2>
//             <p className="text-gray-400">AI-powered task prioritization & management</p>
//           </div>
//           <button onClick={() => setShowAddModal(true)} className="btn-primary">
//             <span className="text-xl mr-2">+</span> Add Task
//           </button>
//         </div>
//       </div>
      
//       {/* Stats Bar */}
//       <div className="grid grid-cols-3 gap-4 mb-8">
//         <div className="glass-panel p-4">
//           <div className="text-3xl font-display font-bold text-cyber-blue">
//             {pendingTasks.length}
//           </div>
//           <div className="text-sm text-gray-400">Pending Tasks</div>
//         </div>
//         <div className="glass-panel p-4">
//           <div className="text-3xl font-display font-bold text-success-green">
//             {completedTasks.length}
//           </div>
//           <div className="text-sm text-gray-400">Completed</div>
//         </div>
//         <div className="glass-panel p-4">
//           <div className="text-3xl font-display font-bold text-focus-purple">
//             {tasks.length > 0 ? Math.round((completedTasks.length / tasks.length) * 100) : 0}%
//           </div>
//           <div className="text-sm text-gray-400">Completion Rate</div>
//         </div>
//       </div>
      
//       {/* Pending Tasks */}
//       {pendingTasks.length > 0 && (
//         <div className="mb-8">
//           <div className="flex items-center gap-3 mb-4">
//             <h3 className="text-xl font-display font-bold">Active Tasks</h3>
//             <div className="ai-badge">
//               <span>🤖</span>
//               <span>AI Sorted by Priority</span>
//             </div>
//           </div>
//           <div className="space-y-3">
//             {pendingTasks.map((task, index) => (
//               <div
//                 key={task.id}
//                 className="task-item animate-slide-up"
//                 style={{ animationDelay: `${index * 0.05}s` }}
//               >
//                 <div className="flex items-start gap-4">
//                   <button
//                     onClick={() => toggleTask(task.id, task.completed)}
//                     className="w-6 h-6 rounded-lg border-2 border-cyber-blue/50 flex items-center justify-center
//                                transition-all duration-300 hover:bg-cyber-blue/20 hover:scale-110 flex-shrink-0 mt-1"
//                   >
//                     {task.completed && <span className="text-cyber-blue">✓</span>}
//                   </button>
                  
//                   <div className="flex-1">
//                     <div className="flex items-start justify-between mb-3">
//                       <div className="flex-1">
//                         <h4 className="text-lg font-semibold text-white mb-2">{task.title}</h4>
//                         <div className="flex flex-wrap items-center gap-3">
//                           {getPriorityBadge(task.ai_priority_score)}
//                           <span className="text-xs text-gray-500 font-mono">
//                             AI Score: {task.ai_priority_score}
//                           </span>
//                           <span className="text-xs text-gray-500">
//                             Urgency: {task.urgency}/5
//                           </span>
//                           <span className="text-xs text-gray-500">
//                             Effort: {task.effort}/5
//                           </span>
//                           {task.deadline && (
//                             <span className="text-xs text-warning-amber">
//                               Due: {new Date(task.deadline).toLocaleDateString()}
//                             </span>
//                           )}
//                         </div>
//                       </div>
//                       <button
//                         onClick={() => deleteTask(task.id)}
//                         className="text-danger-red hover:text-red-400 transition-colors px-3 py-1 rounded-lg
//                                  hover:bg-danger-red/10"
//                       >
//                         ✕
//                       </button>
//                     </div>
//                   </div>
//                 </div>
//               </div>
//             ))}
//           </div>
//         </div>
//       )}
      
//       {/* Completed Tasks */}
//       {completedTasks.length > 0 && (
//         <div>
//           <h3 className="text-xl font-display font-bold mb-4 text-success-green">
//             ✓ Completed Tasks ({completedTasks.length})
//           </h3>
//           <div className="space-y-3">
//             {completedTasks.map((task) => (
//               <div key={task.id} className="task-item opacity-60">
//                 <div className="flex items-start gap-4">
//                   <button
//                     onClick={() => toggleTask(task.id, task.completed)}
//                     className="w-6 h-6 rounded-lg bg-success-green/20 border-2 border-success-green flex items-center justify-center
//                                transition-all duration-300 hover:scale-110 flex-shrink-0 mt-1"
//                   >
//                     <span className="text-success-green">✓</span>
//                   </button>
                  
//                   <div className="flex-1">
//                     <div className="flex items-center justify-between">
//                       <h4 className="text-lg font-semibold line-through text-gray-500">{task.title}</h4>
//                       <button
//                         onClick={() => deleteTask(task.id)}
//                         className="text-gray-600 hover:text-danger-red transition-colors px-3 py-1"
//                       >
//                         ✕
//                       </button>
//                     </div>
//                     {task.completed_at && (
//                       <p className="text-xs text-gray-600 mt-1">
//                         Completed {new Date(task.completed_at).toLocaleString()}
//                       </p>
//                     )}
//                   </div>
//                 </div>
//               </div>
//             ))}
//           </div>
//         </div>
//       )}
      
//       {/* Empty State */}
//       {tasks.length === 0 && (
//         <div className="glass-panel p-12 text-center">
//           <div className="text-8xl mb-6">📝</div>
//           <h3 className="text-2xl font-display font-bold mb-3">No tasks yet</h3>
//           <p className="text-gray-400 mb-6">Start by adding your first task and let AI help you prioritize!</p>
//           <button onClick={() => setShowAddModal(true)} className="btn-primary">
//             Add Your First Task
//           </button>
//         </div>
//       )}
      
//       {/* Add Task Modal */}
//       {showAddModal && (
//         <div className="fixed inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center z-50 p-4">
//           <div className="glass-panel p-8 max-w-2xl w-full animate-slide-up">
//             <div className="flex items-center justify-between mb-6">
//               <h3 className="text-2xl font-display font-bold">Add New Task</h3>
//               <button
//                 onClick={() => setShowAddModal(false)}
//                 className="text-gray-400 hover:text-white text-2xl"
//               >
//                 ✕
//               </button>
//             </div>
            
//             <div className="space-y-4">
//               <div>
//                 <label className="block text-sm font-semibold text-gray-400 mb-2">Task Title</label>
//                 <input
//                   type="text"
//                   value={newTask.title}
//                   onChange={(e) => setNewTask({ ...newTask, title: e.target.value })}
//                   className="input-field"
//                   placeholder="What needs to be done?"
//                   autoFocus
//                 />
//               </div>
              
//               <div className="grid grid-cols-2 gap-4">
//                 <div>
//                   <label className="block text-sm font-semibold text-gray-400 mb-2">
//                     Urgency (1-5)
//                   </label>
//                   <input
//                     type="range"
//                     min="1"
//                     max="5"
//                     value={newTask.urgency}
//                     onChange={(e) => setNewTask({ ...newTask, urgency: parseInt(e.target.value) })}
//                     className="w-full"
//                   />
//                   <div className="flex justify-between text-xs text-gray-500 mt-1">
//                     <span>Low</span>
//                     <span className="font-bold text-cyber-blue">{newTask.urgency}</span>
//                     <span>High</span>
//                   </div>
//                 </div>
                
//                 <div>
//                   <label className="block text-sm font-semibold text-gray-400 mb-2">
//                     Effort (1-5)
//                   </label>
//                   <input
//                     type="range"
//                     min="1"
//                     max="5"
//                     value={newTask.effort}
//                     onChange={(e) => setNewTask({ ...newTask, effort: parseInt(e.target.value) })}
//                     className="w-full"
//                   />
//                   <div className="flex justify-between text-xs text-gray-500 mt-1">
//                     <span>Easy</span>
//                     <span className="font-bold text-focus-purple">{newTask.effort}</span>
//                     <span>Hard</span>
//                   </div>
//                 </div>
//               </div>
              
//               <div>
//                 <label className="block text-sm font-semibold text-gray-400 mb-2">
//                   Deadline (Optional)
//                 </label>
//                 <input
//                   type="datetime-local"
//                   value={newTask.deadline}
//                   onChange={(e) => setNewTask({ ...newTask, deadline: e.target.value })}
//                   className="input-field"
//                 />
//               </div>
              
//               <div className="p-4 bg-slate-deep/40 rounded-xl border border-cyber-blue/20">
//                 <div className="flex items-start gap-3">
//                   <span className="text-2xl">🤖</span>
//                   <div>
//                     <div className="font-semibold text-cyber-blue mb-1">AI Will Help You</div>
//                     <p className="text-sm text-gray-400">
//                       Based on urgency, effort, and deadline, AI will calculate an optimal priority score 
//                       and rank your tasks automatically.
//                     </p>
//                   </div>
//                 </div>
//               </div>
//             </div>
            
//             <div className="flex gap-3 mt-6">
//               <button onClick={() => setShowAddModal(false)} className="btn-secondary flex-1">
//                 Cancel
//               </button>
//               <button onClick={addTask} className="btn-primary flex-1">
//                 Add Task
//               </button>
//             </div>
//           </div>
//         </div>
//       )}
//     </div>
//   )
// }

// export default Tasks

import { useState, useEffect } from 'react'
import { api } from '../api'  // ✅ FIXED

function Tasks() {
  const [tasks, setTasks] = useState([])
  const [showAddModal, setShowAddModal] = useState(false)
  const [newTask, setNewTask] = useState({
    title: '',
    urgency: 3,
    effort: 3,
    deadline: ''
  })
  
  useEffect(() => {
    fetchTasks()
  }, [])
  
  const fetchTasks = async () => {
    try {
      const response = await api.get('/api/tasks')  // ✅ FIXED
      setTasks(response.data)
    } catch (error) {
      console.error('Error fetching tasks:', error)
    }
  }
  
  const addTask = async () => {
    if (!newTask.title.trim()) return
    
    try {
      await api.post('/api/tasks', newTask)  // ✅ FIXED
      setNewTask({ title: '', urgency: 3, effort: 3, deadline: '' })
      setShowAddModal(false)
      fetchTasks()
    } catch (error) {
      console.error('Error adding task:', error)
    }
  }
  
  const toggleTask = async (taskId, completed) => {
    try {
      await api.put(`/api/tasks/${taskId}`, { completed: !completed })  // ✅ FIXED
      fetchTasks()
    } catch (error) {
      console.error('Error updating task:', error)
    }
  }
  
  const deleteTask = async (taskId) => {
    try {
      await api.delete(`/api/tasks/${taskId}`)  // ✅ FIXED
      fetchTasks()
    } catch (error) {
      console.error('Error deleting task:', error)
    }
  }
  
  const getPriorityBadge = (score) => {
    if (score >= 40) return <span className="priority-badge-high">High Priority</span>
    if (score >= 25) return <span className="priority-badge-medium">Medium</span>
    return <span className="priority-badge-low">Low</span>
  }
  
  const pendingTasks = tasks.filter(t => !t.completed)
  const completedTasks = tasks.filter(t => t.completed)
  
  return (
    <div className="animate-fade-in">
      <div className="glass-panel p-6 mb-8">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-3xl font-display font-bold mb-2">Smart Task Manager</h2>
            <p className="text-gray-400">AI-powered task prioritization & management</p>
          </div>
          <button onClick={() => setShowAddModal(true)} className="btn-primary">
            <span className="text-xl mr-2">+</span> Add Task
          </button>
        </div>
      </div>
      
      <div className="grid grid-cols-3 gap-4 mb-8">
        <div className="glass-panel p-4">
          <div className="text-3xl font-display font-bold text-cyber-blue">
            {pendingTasks.length}
          </div>
          <div className="text-sm text-gray-400">Pending Tasks</div>
        </div>
        <div className="glass-panel p-4">
          <div className="text-3xl font-display font-bold text-success-green">
            {completedTasks.length}
          </div>
          <div className="text-sm text-gray-400">Completed</div>
        </div>
        <div className="glass-panel p-4">
          <div className="text-3xl font-display font-bold text-focus-purple">
            {tasks.length > 0 ? Math.round((completedTasks.length / tasks.length) * 100) : 0}%
          </div>
          <div className="text-sm text-gray-400">Completion Rate</div>
        </div>
      </div>
      
      {pendingTasks.length > 0 && (
        <div className="mb-8">
          <div className="flex items-center gap-3 mb-4">
            <h3 className="text-xl font-display font-bold">Active Tasks</h3>
            <div className="ai-badge">
              <span>🤖</span>
              <span>AI Sorted by Priority</span>
            </div>
          </div>
          <div className="space-y-3">
            {pendingTasks.map((task, index) => (
              <div
                key={task.id}
                className="task-item animate-slide-up"
                style={{ animationDelay: `${index * 0.05}s` }}
              >
                <div className="flex items-start gap-4">
                  <button
                    onClick={() => toggleTask(task.id, task.completed)}
                    className="w-6 h-6 rounded-lg border-2 border-cyber-blue/50 flex items-center justify-center
                               transition-all duration-300 hover:bg-cyber-blue/20 hover:scale-110 flex-shrink-0 mt-1"
                  >
                    {task.completed && <span className="text-cyber-blue">✓</span>}
                  </button>
                  
                  <div className="flex-1">
                    <div className="flex items-start justify-between mb-3">
                      <div className="flex-1">
                        <h4 className="text-lg font-semibold text-white mb-2">{task.title}</h4>
                        <div className="flex flex-wrap items-center gap-3">
                          {getPriorityBadge(task.ai_priority_score)}
                          <span className="text-xs text-gray-500 font-mono">
                            AI Score: {task.ai_priority_score}
                          </span>
                          <span className="text-xs text-gray-500">
                            Urgency: {task.urgency}/5
                          </span>
                          <span className="text-xs text-gray-500">
                            Effort: {task.effort}/5
                          </span>
                          {task.deadline && (
                            <span className="text-xs text-warning-amber">
                              Due: {new Date(task.deadline).toLocaleDateString()}
                            </span>
                          )}
                        </div>
                      </div>
                      <button
                        onClick={() => deleteTask(task.id)}
                        className="text-danger-red hover:text-red-400 transition-colors px-3 py-1 rounded-lg
                                 hover:bg-danger-red/10"
                      >
                        ✕
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
      
      {completedTasks.length > 0 && (
        <div>
          <h3 className="text-xl font-display font-bold mb-4 text-success-green">
            ✓ Completed Tasks ({completedTasks.length})
          </h3>
          <div className="space-y-3">
            {completedTasks.map((task) => (
              <div key={task.id} className="task-item opacity-60">
                <div className="flex items-start gap-4">
                  <button
                    onClick={() => toggleTask(task.id, task.completed)}
                    className="w-6 h-6 rounded-lg bg-success-green/20 border-2 border-success-green flex items-center justify-center
                               transition-all duration-300 hover:scale-110 flex-shrink-0 mt-1"
                  >
                    <span className="text-success-green">✓</span>
                  </button>
                  
                  <div className="flex-1">
                    <div className="flex items-center justify-between">
                      <h4 className="text-lg font-semibold line-through text-gray-500">{task.title}</h4>
                      <button
                        onClick={() => deleteTask(task.id)}
                        className="text-gray-600 hover:text-danger-red transition-colors px-3 py-1"
                      >
                        ✕
                      </button>
                    </div>
                    {task.completed_at && (
                      <p className="text-xs text-gray-600 mt-1">
                        Completed {new Date(task.completed_at).toLocaleString()}
                      </p>
                    )}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
      
      {tasks.length === 0 && (
        <div className="glass-panel p-12 text-center">
          <div className="text-8xl mb-6">📝</div>
          <h3 className="text-2xl font-display font-bold mb-3">No tasks yet</h3>
          <p className="text-gray-400 mb-6">Start by adding your first task and let AI help you prioritize!</p>
          <button onClick={() => setShowAddModal(true)} className="btn-primary">
            Add Your First Task
          </button>
        </div>
      )}
      
      {showAddModal && (
        <div className="fixed inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center z-50 p-4">
          <div className="glass-panel p-8 max-w-2xl w-full animate-slide-up">
            <div className="flex items-center justify-between mb-6">
              <h3 className="text-2xl font-display font-bold">Add New Task</h3>
              <button
                onClick={() => setShowAddModal(false)}
                className="text-gray-400 hover:text-white text-2xl"
              >
                ✕
              </button>
            </div>
            
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-semibold text-gray-400 mb-2">Task Title</label>
                <input
                  type="text"
                  value={newTask.title}
                  onChange={(e) => setNewTask({ ...newTask, title: e.target.value })}
                  className="input-field"
                  placeholder="What needs to be done?"
                  autoFocus
                />
              </div>
              
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-semibold text-gray-400 mb-2">
                    Urgency (1-5)
                  </label>
                  <input
                    type="range"
                    min="1"
                    max="5"
                    value={newTask.urgency}
                    onChange={(e) => setNewTask({ ...newTask, urgency: parseInt(e.target.value) })}
                    className="w-full"
                  />
                  <div className="flex justify-between text-xs text-gray-500 mt-1">
                    <span>Low</span>
                    <span className="font-bold text-cyber-blue">{newTask.urgency}</span>
                    <span>High</span>
                  </div>
                </div>
                
                <div>
                  <label className="block text-sm font-semibold text-gray-400 mb-2">
                    Effort (1-5)
                  </label>
                  <input
                    type="range"
                    min="1"
                    max="5"
                    value={newTask.effort}
                    onChange={(e) => setNewTask({ ...newTask, effort: parseInt(e.target.value) })}
                    className="w-full"
                  />
                  <div className="flex justify-between text-xs text-gray-500 mt-1">
                    <span>Easy</span>
                    <span className="font-bold text-focus-purple">{newTask.effort}</span>
                    <span>Hard</span>
                  </div>
                </div>
              </div>
              
              <div>
                <label className="block text-sm font-semibold text-gray-400 mb-2">
                  Deadline (Optional)
                </label>
                <input
                  type="datetime-local"
                  value={newTask.deadline}
                  onChange={(e) => setNewTask({ ...newTask, deadline: e.target.value })}
                  className="input-field"
                />
              </div>
              
              <div className="p-4 bg-slate-deep/40 rounded-xl border border-cyber-blue/20">
                <div className="flex items-start gap-3">
                  <span className="text-2xl">🤖</span>
                  <div>
                    <div className="font-semibold text-cyber-blue mb-1">AI Will Help You</div>
                    <p className="text-sm text-gray-400">
                      Based on urgency, effort, and deadline, AI will calculate an optimal priority score 
                      and rank your tasks automatically.
                    </p>
                  </div>
                </div>
              </div>
            </div>
            
            <div className="flex gap-3 mt-6">
              <button onClick={() => setShowAddModal(false)} className="btn-secondary flex-1">
                Cancel
              </button>
              <button onClick={addTask} className="btn-primary flex-1">
                Add Task
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default Tasks