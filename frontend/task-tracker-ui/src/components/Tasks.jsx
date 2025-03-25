import React, { useEffect, useState } from 'react'
import '../styles/tasks.css'
import axios from 'axios'
import Task from './Task'
import { data } from 'react-router'

const Tasks = () => {
    // extract tokens 
    const accessToken = localStorage.getItem('accessToken')
    const refreshToken = localStorage.getItem('refreshToken')
    
    // Monitor tasks and new tasks
    const [tasks, setTasks] = useState([]) // track array of tasks
    const [newTask, setNewTask] = useState("") // track new tasks inputted by user
    
    // Function to fetch tasks from server 
    const fetchTasks = async() => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/tasks/',{
                    headers: {
                        'Authorization': `Bearer ${accessToken}`
                    }
                })
                    console.log(response.data)
                    // update tasks state for local UI usage
                    setTasks(response.data)
            } catch (error) {
                // handle refresh token logic 
                if(error.response && error.response.status ==401) {
                    console.log('Access Token expired, refreshing...')
                    await refreshAccessToken();
                    fetchTasks()
                } else {
                    console.error('Failed to Fetch Tasks', error.message)
                }
            }  
        }
    // Fetch tasks on Mount
    useEffect (()=>{
        fetchTasks()
    },[])

    // Handles post request to add new task
    const createTask = async()=> {
        // check for empty task
        if (!newTask.trim()) {
            console.error("Task cannot be empty")
            return;
        }
        // create new Task from newTask state variable 
        console.log('creating Task:', newTask)
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/tasks/', 
                {title:newTask},
                {headers: {'Authorization' : `Bearer ${accessToken}`}
            })
            console.log(response.data)
            // UPDATE tasks state to update the UI
            setTasks((prevTasks) => [...prevTasks,response.data])
            // clear new task
            setNewTask("")
            // fetch new data
            // await fetchTasks()
        } catch (error){
            // check for expired token and retry with refresh token
            if(error.response && error.response.status ==401) {
                console.log('Access Token expired, refreshing...')
                await refreshAccessToken();
                createTask()
            }
            else{
                console.error('Failed to Add Task',error.message)
            }
        }
    }
    //  Task component handles delete on database, update UI to render from tasks state variable
    const updateUIOnDelete = async (taskID) => {
        // update the task state to NOT include the id that was just deleted
        setTasks((prevTasks)=> prevTasks.filter((task)=>task.id!= taskID))
    }

    // Refresh Token by posting to /refresh endpoint with refresh token 
    const refreshAccessToken = async () =>  {
        try{
            const response = await axios.post('http://127.0.0.1:8000/api/user/refresh', {
                refresh:refreshToken
            })
            // extract new token and update local storage 
            const newAccessToken = response.data.access
            localStorage.setItem('accessToken', newAccessToken)
            console.log('Access Token Refreshsed')
        // on failure clear all tokens and redirect user to login
        } catch (error) {
            console.error('failed to refresh token')
            localStorage.removeItem('accessToken')
            localStorage.removeItem('refreshToken')
            window.location.href = '/login'
        }
    }
    const logout = () => {
        // remove/delete the access tokens
        localStorage.removeItem('accessToken');
        localStorage.removeItem('refreshToken');s
        window.location.href='/login'
        // route back to login 
    }
  return (
    <div className='task-container'>
        {/* header */}
        <h2 className='new-task-header'>Your To-Dos</h2>
        {/* add task bar */}
        <div className="new-task-container">
            <input
                type="text" 
                placeholder= "Add Task.." 
                name="new-task" 
                className="new-task-bar" 
                onChange = {(e)=>setNewTask(e.target.value)}
            />

            <input 
                type="button" 
                value="ADD" 
                className="add-btn" 
                onClick={createTask}
            />
        </div>
        {/* Task component */}

        {tasks.length >0 ? (tasks.map((task,index)=><Task key= {index} task = {task} updateUIOnDelete={updateUIOnDelete}/>)): <p className='empty'>No Tasks available</p>}
        <button className ='logout' onClick={logout}>Logout</button>
    </div>
  )
}

export default Tasks