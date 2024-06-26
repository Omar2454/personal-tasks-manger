// src/App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css'; // Import the CSS file

const App = () => {
    const [tasks, setTasks] = useState([]);
    const [task, setTask] = useState({
        id: null,
        name: '',
        description: '',
        due_date: '',
        category: '',
        status: '',
        user_id: 1,
    });
    const [isEditing, setIsEditing] = useState(false);

    useEffect(() => {
        axios.get('http://127.0.0.1:5000/tasks')
            .then(response => {
                setTasks(response.data);
            })
            .catch(error => {
                console.error("There was an error fetching the tasks!", error);
            });
    }, []);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setTask({ ...task, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (isEditing) {
            axios.put(`http://127.0.0.1:5000/tasks/${task.id}`, task)
                .then(response => {
                    setTasks(tasks.map(t => t.id === task.id ? response.data : t));
                    setTask({ id: null, name: '', description: '', due_date: '', category: '', status: '', user_id: 1 });
                    setIsEditing(false);
                })
                .catch(error => {
                    console.error("There was an error updating the task!", error);
                });
        } else {
            axios.post('http://127.0.0.1:5000/tasks', task)
                .then(response => {
                    setTasks([...tasks, response.data]);
                    setTask({ name: '', description: '', due_date: '', category: '', status: '', user_id: 1 });
                })
                .catch(error => {
                    console.error("There was an error creating the task!", error);
                });
        }
    };

    const handleEdit = (task) => {
        setTask(task);
        setIsEditing(true);
    };

    const handleDelete = (id) => {
        axios.delete(`http://127.0.0.1:5000/tasks/${id}`)
            .then(() => {
                setTasks(tasks.filter(task => task.id !== id));
            })
            .catch(error => {
                console.error("There was an error deleting the task!", error);
            });
    };

    return (
        <div className="App">
            <h1>Personal Task Manager</h1>
            <form onSubmit={handleSubmit}>
                <input type="text" name="name" value={task.name} onChange={handleChange} placeholder="Task Name" required />
                <textarea name="description" value={task.description} onChange={handleChange} placeholder="Task Description"></textarea>
                <input type="text" name="due_date" value={task.due_date} onChange={handleChange} placeholder="Due Date" />
                <input type="text" name="category" value={task.category} onChange={handleChange} placeholder="Category" />
                <input type="text" name="status" value={task.status} onChange={handleChange} placeholder="Status" />
                <button type="submit">{isEditing ? 'Update Task' : 'Add Task'}</button>
            </form>
            <ul>
                {tasks.map(task => (
                    <li key={task.id}>
                        <div className="task-details">
                            <h2>{task.name}</h2>
                            <p>{task.description}</p>
                            <p>{task.due_date}</p>
                            <p>{task.category}</p>
                            <p>{task.status}</p>
                        </div>
                        <button className="edit-button" onClick={() => handleEdit(task)}>Edit</button>
                        <button className="delete-button" onClick={() => handleDelete(task.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default App;
