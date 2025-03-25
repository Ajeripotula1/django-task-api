import React, { useState } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router'
import '../styles/login.css'
const Login = ({setIsAuthenticated}) => {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [error, setError] = useState("")

    const navigate = useNavigate()
    
    // navigate to register
    const goToRegister = () => {
        navigate('/register')
    }
    // handle log in feature 
    const login = async(event)=> {
        event.preventDefault()

        try {
            //  API Request
            const response = await axios.post('http://127.0.0.1:8000/api/user/login',
            {
                username,
                password,
            });
            // Destructure access and refresh tokens from response
            const {access,refresh} = response.data
            console.log(access,refresh)
            // Store Tokens in localStorage
            localStorage.setItem("accessToken", access)
            localStorage.setItem("refreshToken", refresh)
            
            setIsAuthenticated(true)
            navigate('/tasks')
        } catch (err){
            console.log(err)
            // Clear existing Tokens
            localStorage.removeItem("accessToken")
            localStorage.removeItem('refreshToken')
            setError("Invalid credentials, please try again.")
        }
    }

  return (
    <div className='login'>
        <h2 className="title">Log in</h2>

        <form onSubmit={login} className="login-form">
            <input
                type="text"
                value={username} 
                placeholder='username'
                onChange={(e)=>setUsername(e.target.value)}
                required   
            />

            <input 
                type="password" 
                placeholder='password'
                onChange={(e)=>setPassword(e.target.value)}
                required    
            />
            {error && <p style={{color:"red"}}>{error}</p>}
            <input className='submit-btn' type="submit" />
        </form>

            <p>Don't have an account?</p>
            <button onClick={goToRegister}>Register</button>

       
    </div>
  )
}

export default Login