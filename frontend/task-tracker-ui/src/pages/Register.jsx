import React, { useState } from 'react'
import { useNavigate } from 'react-router'
import '../styles/register.css'
import axios from 'axios'
const Register = () => {
   
    const [userName,setUserName] = useState("")
    const [email,setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [error, setError] = useState("")
    const [successMessage, setSuccessMessage] = useState(false)
    const navigate = useNavigate()

     // route to login page
     const navigateToLogin = () => {
        navigate('/login')

     }
     // axios post request to /register endpoint
     const registerUser = async(e) => {
        e.preventDefault()

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/user/register',
                {
                    username:userName,
                    password:password,
                    email:email
                }
            )
            console.log('Registration successful', response.data)
            setSuccessMessage("Registration successful! You can now log in.") // Set success message
            setError("")


        } catch (error) {
             // Handle registration error
            console.error('Error registering user:', error)
            setSuccessMessage("Registration unsuccessful! Try Again.") // Set success message
            // setError('Registration failed. Please try again.')
            
        }

     }

  return (
    <div className='register'>
        <h2>Register</h2>
        <form onSubmit={registerUser} className="register-form">
            <input 
                type="email" 
                className="email" 
                placeholder='email' 
                onChange={(e)=>setEmail(e.target.value)}
                required
            />
            
            <input 
                type="username" 
                className="password" 
                placeholder='username'
                onChange={(e)=>setUserName(e.target.value)}
                required    
            />
            <input 
                type="password" 
                className="password" 
                placeholder='password' 
                onChange={(e)=>setPassword(e.target.value)}
                required
            />
            
            <input className='submit-btn' type="submit" /> 
        </form>
            <p>Already have an account?</p>
            <button onClick={navigateToLogin}>Login</button>  
            {error && <p style={{ color: "red" }}>{error}</p>}
            {successMessage && <p style={{ color: "green" }}>{successMessage}</p>} {/* Conditional rendering of success message */}      
            
    </div>
  )
}

export default Register