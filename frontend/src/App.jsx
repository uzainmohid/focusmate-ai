// // // import { BrowserRouter as Router, Routes, Route, Link, useLocation } from 'react-router-dom'
// // // import { useState } from 'react'
// // // import Dashboard from './pages/Dashboard'
// // // import Tasks from './pages/Tasks'
// // // import FocusSession from './pages/FocusSession'
// // // import Insights from './pages/Insights'

// // // function Navigation() {
// // //   const location = useLocation()
// // //   const [open, setOpen] = useState(false)

// // //   const navItems = [
// // //     { path: '/', label: 'Dashboard', icon: '📊' },
// // //     { path: '/tasks', label: 'Tasks', icon: '✓' },
// // //     { path: '/focus', label: 'Focus', icon: '🎯' },
// // //     { path: '/insights', label: 'Insights', icon: '📈' },
// // //   ]

// // //   return (
// // //     <nav className="glass-panel px-4 sm:px-6 py-4 mb-6">
// // //       <div className="flex items-center justify-between">
// // //         {/* Logo */}
// // //         <div className="flex items-center gap-3">
// // //           <div className="w-10 h-10 bg-gradient-focus rounded-xl flex items-center justify-center text-xl">
// // //             🧠
// // //           </div>
// // //           <div className="leading-tight">
// // //             <h1 className="text-lg sm:text-2xl font-display font-bold text-gradient">
// // //               FocusMate AI
// // //             </h1>
// // //             <p className="text-[10px] sm:text-xs text-gray-400">
// // //               Smart Productivity Coach
// // //             </p>
// // //           </div>
// // //         </div>

// // //         {/* Desktop Nav */}
// // //         <div className="hidden md:flex gap-2">
// // //           {navItems.map((item) => (
// // //             <Link
// // //               key={item.path}
// // //               to={item.path}
// // //               className={`px-4 py-2 rounded-xl text-sm font-semibold transition ${
// // //                 location.pathname === item.path
// // //                   ? 'bg-gradient-focus text-white'
// // //                   : 'text-gray-300 hover:text-white hover:bg-slate-deep/60'
// // //               }`}
// // //             >
// // //               {item.icon} {item.label}
// // //             </Link>
// // //           ))}
// // //         </div>

// // //         {/* Mobile Toggle */}
// // //         <button
// // //           onClick={() => setOpen(!open)}
// // //           className="md:hidden text-2xl text-white"
// // //         >
// // //           ☰
// // //         </button>
// // //       </div>

// // //       {/* Mobile Menu */}
// // //       {open && (
// // //         <div className="md:hidden mt-4 flex flex-col gap-2">
// // //           {navItems.map((item) => (
// // //             <Link
// // //               key={item.path}
// // //               to={item.path}
// // //               onClick={() => setOpen(false)}
// // //               className={`px-4 py-3 rounded-xl text-sm font-semibold ${
// // //                 location.pathname === item.path
// // //                   ? 'bg-gradient-focus text-white'
// // //                   : 'bg-slate-deep/60 text-gray-300'
// // //               }`}
// // //             >
// // //               {item.icon} {item.label}
// // //             </Link>
// // //           ))}
// // //         </div>
// // //       )}
// // //     </nav>
// // //   )
// // // }

// // // function Footer() {
// // //   return (
// // //     <footer className="mt-10 py-6 text-center text-xs sm:text-sm text-gray-400">
// // //       © 2026 FocusMate AI · Developed by <span className="text-white font-semibold">Uzain Mohid</span>
// // //     </footer>
// // //   )
// // // }

// // // function App() {
// // //   return (
// // //     <Router>
// // //       <div className="min-h-screen px-3 sm:px-6">
// // //         <div className="max-w-7xl mx-auto">
// // //           <Navigation />
// // //           <Routes>
// // //             <Route path="/" element={<Dashboard />} />
// // //             <Route path="/tasks" element={<Tasks />} />
// // //             <Route path="/focus" element={<FocusSession />} />
// // //             <Route path="/insights" element={<Insights />} />
// // //           </Routes>
// // //           <Footer />
// // //         </div>
// // //       </div>
// // //     </Router>
// // //   )
// // // }

// // // export default App


// // import { BrowserRouter as Router, Routes, Route, Link, useLocation } from 'react-router-dom'
// // import Dashboard from './pages/Dashboard'
// // import Tasks from './pages/Tasks'
// // import FocusSession from './pages/FocusSession'
// // import Insights from './pages/Insights'
// // import { useState } from 'react'

// // /* ===================== NAVIGATION ===================== */
// // function Navigation() {
// //   const location = useLocation()
// //   const [mobileMenu, setMobileMenu] = useState(false)

// //   const navItems = [
// //     { path: '/', label: 'Dashboard', icon: '📊' },
// //     { path: '/tasks', label: 'Tasks', icon: '✓' },
// //     { path: '/focus', label: 'Focus', icon: '🎯' },
// //     { path: '/insights', label: 'Insights', icon: '📈' },
// //   ]

// //   return (
// //     <nav className="glass-panel px-4 sm:px-6 py-4 mb-8 fixed top-0 left-0 right-0 z-50 shadow-lg">
// //       <div className="max-w-7xl mx-auto flex items-center justify-between">
// //         {/* Brand */}
// //         <div className="flex items-center gap-3">
// //           <div className="w-10 h-10 bg-gradient-focus rounded-xl flex items-center justify-center text-2xl animate-pulse-slow">
// //             🧠
// //           </div>
// //           <div>
// //             <h1 className="text-2xl font-display font-bold text-gradient">FocusMate AI</h1>
// //             <p className="text-xs text-gray-400 font-mono">Smart Productivity Coach</p>
// //           </div>
// //         </div>

// //         {/* Desktop Menu */}
// //         <div className="hidden md:flex gap-2">
// //           {navItems.map((item) => (
// //             <Link
// //               key={item.path}
// //               to={item.path}
// //               className={`px-5 py-2.5 rounded-xl font-semibold transition-all duration-300 flex items-center gap-2 ${
// //                 location.pathname === item.path
// //                   ? 'bg-gradient-focus text-white shadow-lg shadow-cyber-blue/30'
// //                   : 'bg-slate-deep/60 text-gray-300 hover:bg-slate-deep hover:text-white'
// //               }`}
// //             >
// //               <span>{item.icon}</span>
// //               <span>{item.label}</span>
// //             </Link>
// //           ))}
// //         </div>

// //         {/* Mobile Hamburger */}
// //         <div className="md:hidden flex items-center">
// //           <button
// //             onClick={() => setMobileMenu(!mobileMenu)}
// //             className="text-white text-2xl p-2 rounded-md bg-slate-deep/50 hover:bg-slate-deep/70 transition"
// //           >
// //             {mobileMenu ? '✖️' : '☰'}
// //           </button>
// //         </div>
// //       </div>

// //       {/* Mobile Menu */}
// //       {mobileMenu && (
// //         <div className="md:hidden mt-4 flex flex-col gap-2 px-2">
// //           {navItems.map((item) => (
// //             <Link
// //               key={item.path}
// //               to={item.path}
// //               onClick={() => setMobileMenu(false)}
// //               className={`px-4 py-2 rounded-lg font-semibold transition-all duration-300 flex items-center gap-2 ${
// //                 location.pathname === item.path
// //                   ? 'bg-gradient-focus text-white shadow-lg shadow-cyber-blue/30'
// //                   : 'bg-slate-deep/60 text-gray-300 hover:bg-slate-deep hover:text-white'
// //               }`}
// //             >
// //               <span>{item.icon}</span>
// //               <span>{item.label}</span>
// //             </Link>
// //           ))}
// //         </div>
// //       )}
// //     </nav>
// //   )
// // }

// // /* ===================== FOOTER ===================== */
// // function Footer() {
// //   return (
// //     <footer className="mt-12 p-6 bg-slate-deep/60 text-gray-400 text-sm font-mono rounded-t-xl text-center">
// //       <p>© 2026 FocusMate AI. Developed by Uzain Mohid.</p>
// //     </footer>
// //   )
// // }

// // /* ===================== APP ===================== */
// // function App() {
// //   return (
// //     <Router>
// //       <div className="min-h-screen pt-28 p-4 sm:p-6 bg-slate-deep text-white">
// //         <div className="max-w-7xl mx-auto">
// //           <Navigation />
// //           <Routes>
// //             <Route path="/" element={<Dashboard />} />
// //             <Route path="/tasks" element={<Tasks />} />
// //             <Route path="/focus" element={<FocusSession />} />
// //             <Route path="/insights" element={<Insights />} />
// //           </Routes>
// //           <Footer />
// //         </div>
// //       </div>
// //     </Router>
// //   )
// // }

// // export default App


// import { BrowserRouter as Router, Routes, Route, Link, useLocation } from 'react-router-dom'
// import Dashboard from './pages/Dashboard'
// import Tasks from './pages/Tasks'
// import FocusSession from './pages/FocusSession'
// import Insights from './pages/Insights'
// import { useState } from 'react'

// /* ===================== NAVIGATION ===================== */
// function Navigation() {
//   const location = useLocation()
//   const [mobileMenu, setMobileMenu] = useState(false)

//   const navItems = [
//     { path: '/', label: 'Dashboard', icon: '📊' },
//     { path: '/tasks', label: 'Tasks', icon: '✓' },
//     { path: '/focus', label: 'Focus', icon: '🎯' },
//     { path: '/insights', label: 'Insights', icon: '📈' },
//   ]

//   return (
//     <nav className="glass-panel px-4 sm:px-6 py-4 mb-8 fixed top-0 left-0 right-0 z-50 shadow-lg">
//       <div className="max-w-7xl mx-auto flex items-center justify-between">
//         {/* Brand */}
//         <div className="flex items-center gap-3">
//           <div className="w-10 h-10 bg-gradient-focus rounded-xl flex items-center justify-center text-2xl animate-pulse-slow">
//             🧠
//           </div>
//           <div>
//             <h1 className="text-2xl font-display font-bold text-gradient">FocusMate AI</h1>
//             <p className="text-xs text-gray-400 font-mono">Smart Productivity Coach</p>
//           </div>
//         </div>

//         {/* Desktop Menu */}
//         <div className="hidden md:flex gap-2">
//           {navItems.map((item) => (
//             <Link
//               key={item.path}
//               to={item.path}
//               className={`px-5 py-2.5 rounded-xl font-semibold transition-all duration-300 flex items-center gap-2 ${
//                 location.pathname === item.path
//                   ? 'bg-gradient-focus text-white shadow-lg shadow-cyber-blue/30'
//                   : 'bg-slate-deep/60 text-gray-300 hover:bg-slate-deep hover:text-white'
//               }`}
//             >
//               <span>{item.icon}</span>
//               <span>{item.label}</span>
//             </Link>
//           ))}
//         </div>

//         {/* Mobile Hamburger */}
//         <div className="md:hidden flex items-center">
//           <button
//             onClick={() => setMobileMenu(!mobileMenu)}
//             className="text-white text-2xl p-2 rounded-md bg-slate-deep/50 hover:bg-slate-deep/70 transition"
//           >
//             {mobileMenu ? '✖️' : '☰'}
//           </button>
//         </div>
//       </div>

//       {/* Mobile Menu */}
//       {mobileMenu && (
//         <div className="md:hidden mt-4 flex flex-col gap-2 px-2">
//           {navItems.map((item) => (
//             <Link
//               key={item.path}
//               to={item.path}
//               onClick={() => setMobileMenu(false)}
//               className={`px-4 py-2 rounded-lg font-semibold transition-all duration-300 flex items-center gap-2 ${
//                 location.pathname === item.path
//                   ? 'bg-gradient-focus text-white shadow-lg shadow-cyber-blue/30'
//                   : 'bg-slate-deep/60 text-gray-300 hover:bg-slate-deep hover:text-white'
//               }`}
//             >
//               <span>{item.icon}</span>
//               <span>{item.label}</span>
//             </Link>
//           ))}
//         </div>
//       )}
//     </nav>
//   )
// }

// /* ===================== FOOTER ===================== */
// function Footer() {
//   return (
//     <footer className="mt-12 p-6 bg-slate-deep/60 text-gray-400 text-sm font-mono rounded-t-xl text-center">
//       <p>© 2026 FocusMate AI. Developed by Uzain Mohid.</p>
//     </footer>
//   )
// }

// /* ===================== APP ===================== */
// function App() {
//   return (
//     <Router>
//       <div className="min-h-screen pt-28 p-4 sm:p-6 bg-slate-deep text-white">
//         <div className="max-w-7xl mx-auto">
//           <Navigation />
//           <Routes>
//             <Route path="/" element={<Dashboard />} />
//             <Route path="/tasks" element={<Tasks />} />
//             <Route path="/focus" element={<FocusSession />} />
//             <Route path="/insights" element={<Insights />} />
//           </Routes>
//           <Footer />
//         </div>
//       </div>
//     </Router>
//   )
// }

// export default App


import { BrowserRouter as Router, Routes, Route, Link, useLocation } from 'react-router-dom'
import Dashboard from './pages/Dashboard'
import Tasks from './pages/Tasks'
import FocusSession from './pages/FocusSession'
import Insights from './pages/Insights'
import { useState } from 'react'

/* ===================== NAVIGATION ===================== */
function Navigation() {
  const location = useLocation()
  const [mobileMenu, setMobileMenu] = useState(false)

  const navItems = [
    { path: '/', label: 'Dashboard', icon: '📊' },
    { path: '/tasks', label: 'Tasks', icon: '✓' },
    { path: '/focus', label: 'Focus', icon: '🎯' },
    { path: '/insights', label: 'Insights', icon: '📈' },
  ]

  return (
    <nav className="glass-panel px-4 sm:px-6 py-4 fixed top-0 left-0 right-0 z-50 shadow-lg">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        {/* Brand */}
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 bg-gradient-focus rounded-xl flex items-center justify-center text-2xl animate-pulse-slow">
            🧠
          </div>
          <div>
            <h1 className="text-2xl font-display font-bold text-gradient">FocusMate AI</h1>
            <p className="text-xs text-gray-400 font-mono">Smart Productivity Coach</p>
          </div>
        </div>

        {/* Desktop Menu */}
        <div className="hidden md:flex gap-2">
          {navItems.map((item) => (
            <Link
              key={item.path}
              to={item.path}
              className={`px-5 py-2.5 rounded-xl font-semibold transition-all duration-300 flex items-center gap-2 ${
                location.pathname === item.path
                  ? 'bg-gradient-focus text-white shadow-lg shadow-cyber-blue/30'
                  : 'bg-slate-deep/60 text-gray-300 hover:bg-slate-deep hover:text-white'
              }`}
            >
              <span>{item.icon}</span>
              <span>{item.label}</span>
            </Link>
          ))}
        </div>

        {/* Mobile Hamburger */}
        <div className="md:hidden flex items-center">
          <button
            onClick={() => setMobileMenu(!mobileMenu)}
            className="text-white text-2xl p-2 rounded-md bg-slate-deep/50 hover:bg-slate-deep/70 transition"
          >
            {mobileMenu ? '✖️' : '☰'}
          </button>
        </div>
      </div>

      {/* Mobile Menu */}
      {mobileMenu && (
        <div className="md:hidden mt-4 flex flex-col gap-2 px-2 max-w-7xl mx-auto">
          {navItems.map((item) => (
            <Link
              key={item.path}
              to={item.path}
              onClick={() => setMobileMenu(false)}
              className={`px-4 py-2 rounded-lg font-semibold transition-all duration-300 flex items-center gap-2 ${
                location.pathname === item.path
                  ? 'bg-gradient-focus text-white shadow-lg shadow-cyber-blue/30'
                  : 'bg-slate-deep/60 text-gray-300 hover:bg-slate-deep hover:text-white'
              }`}
            >
              <span>{item.icon}</span>
              <span>{item.label}</span>
            </Link>
          ))}
        </div>
      )}
    </nav>
  )
}

/* ===================== FOOTER ===================== */
function Footer() {
  return (
    <footer className="mt-12 p-6 bg-slate-deep/60 text-gray-400 text-sm font-mono rounded-t-xl text-center">
      <p>© 2026 FocusMate AI. Developed by Uzain Mohid.</p>
    </footer>
  )
}

/* ===================== APP ===================== */
function App() {
  return (
    <Router>
      {/* NAVBAR MUST BE OUTSIDE CONTENT */}
      <Navigation />

      {/* MAIN CONTENT */}
      <div className="min-h-screen pt-28 px-4 sm:px-6 bg-slate-deep text-white">
        <div className="max-w-7xl mx-auto">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/tasks" element={<Tasks />} />
            <Route path="/focus" element={<FocusSession />} />
            <Route path="/insights" element={<Insights />} />
          </Routes>

          <Footer />
        </div>
      </div>
    </Router>
  )
}

export default App
