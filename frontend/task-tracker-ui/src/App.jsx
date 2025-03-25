import { useState } from 'react'

import './App.css'
import Login from './pages/Login'
import { BrowserRouter as Router, Routes, Route, Link, Navigate } from "react-router-dom";
import Tasks from './components/Tasks';
import Register from './pages/Register';

const ProtectedRoute = ({isAuthenticated, children}) => {
  return isAuthenticated ? children : <Navigate to ="/login"/>
}

function App() {
  const [isAuthenticated,setIsAuthenticated] = useState(
    !!localStorage.getItem("accessToken") // check if token exists
  )
  const [count, setCount] = useState(0)

  return (
    <Router>
      {/* <nav className='navbar'>
        <ul>
          <li><Link to='/'>Login</Link></li>
          <li><Link to='/home'>Home</Link></li>
        </ul>
      </nav> */}

      <Routes>
        {/* PUBLIC ROUTES */}
        <Route path ='/login' element={<Login setIsAuthenticated = {setIsAuthenticated}/>} />
        <Route path ='/register' element={<Register setIsAuthenticated = {setIsAuthenticated}/>} />


        {/* Private ROUTES */}
        <Route
          path = "/tasks"
          element = {
            <ProtectedRoute isAuthenticated={isAuthenticated}>
              <Tasks/>
            </ProtectedRoute>
          }
        />
        {/* Redirect to Login by Default */}
        <Route path="*" element={<Navigate to="/login" />} />
      </Routes>

    </Router>
  )
}

export default App
