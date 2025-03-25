import React from 'react'
import { useState } from 'react'

import '../styles/task.css'
import axios from 'axios'

const Task = ({task, updateUIOnDelete}) => {
    const accessToken = localStorage.getItem("accessToken")
    const [taskDone,setTaskDone] = useState(task.completed) // track task status based on check box
    
    const taskStatusHandler = async() => {
        try {
            // when invoked, we have flipped the checkbox value 
            const updatedStatus = !taskDone
            setTaskDone(updatedStatus)
            console.log(taskDone,' changed to ',updatedStatus)

            // PATCH request to update "completed" status
            const response = await axios.patch( 
                `http://127.0.0.1:8000/api/tasks/${task.id}/`,
                {completed: updatedStatus},
                {headers: {Authorization: `Bearer ${accessToken}` }}
            )
            console.log("Task Status updated", response.data)
        } catch (error) {
            console.error('Failed to update task status', error)
            // revert the state
            setTaskDone(task.completed)
            
        }
    }
    // DELETE request to server to delete task from databse 
    const deleteTask = async()=>{
        try {
            const taskID = task.id
            console.log('deleting', task.title)
            // delete on path param id to access specific task with id
            const response = await axios.delete(`http://127.0.0.1:8000/api/tasks/${taskID}/`, {
                headers: {'Authorization' : `Bearer ${accessToken}`}
            })
            console.log(response)
            // pass ID of task deleted to parent Task component to update UI 
            updateUIOnDelete(taskID)
            
        } catch (error) {
            console.error("Could not delete resource")
        }
    }

    return (
    <>
        <div className="task-item">
            <input 
                type="checkbox" 
                name="check-off" 
                checked={taskDone}
                onChange={taskStatusHandler} 
                className="check-off" />
            <div className="title">{task.title}</div>
            <div className="status">{task.completed ? "True": "False"}</div> 
            <div 
                className="delete"
                onClick={deleteTask}
            >
                ✖
            </div>

        </div>
        
    </>
    )
}

export default Task