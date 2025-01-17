
# Personal Task Manager

## Overview
Personal Task Manager is a web-based application to manage personal tasks with features to create, edit, delete, categorize, and complete tasks. The backend is built with Flask and the frontend with React.

## Project Structure
- \`backend/\`: Contains the Flask backend application.
- \`frontend/\`: Contains the React frontend application.

## Setup

### Prerequisites
- Python 3.7+
- Node.js 14+
- npm 6+

### Cloning the Repository
1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/Omar2454/personal-task-manager.git
   cd personal-task-manager
   \`\`\`

### Backend Setup

1. Navigate to the backend directory:
   \`\`\`bash
   cd backend
   \`\`\`

2. Create and activate a virtual environment:
   \`\`\`bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   \`\`\`

3. Install the required packages:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. Initialize the database:
   \`\`\`bash
   python init_db.py
   \`\`\`

5. Run the backend server:
   \`\`\`bash
   python -m flask run
   \`\`\`

### Frontend Setup

1. Navigate to the frontend directory:
   \`\`\`bash
   cd ../frontend
   \`\`\`

2. Install the dependencies:
   \`\`\`bash
   npm install
   \`\`\`

3. Start the React application:
   \`\`\`bash
   npm start
   \`\`\`

### API Endpoints
- \`GET /tasks\`: Retrieve all tasks
- \`GET /tasks/<task_id>\`: Retrieve a specific task
- \`POST /tasks\`: Create a new task
- \`PUT /tasks/<task_id>\`: Update a task
- \`DELETE /tasks/<task_id>\`: Delete a task

### Technologies Used
- **Backend**: Flask, SQLAlchemy, SQLite
- **Frontend**: React, Axios

## Usage
1. Open your browser and go to \`http://localhost:3000\` to access the React frontend.
2. Use the interface to add, edit, and delete tasks. The tasks will be managed by the Flask backend.

## Screenshots
SS

![Screenshot1](image.png)
![Screenshot2](Add.jpg)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- React: [https://reactjs.org/](https://reactjs.org/)
- SQLAlchemy: [https://www.sqlalchemy.org/](https://www.sqlalchemy.org/)
EOL
