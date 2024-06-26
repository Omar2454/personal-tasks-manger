# app.py

from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    due_date = db.Column(db.String(20), nullable=True)
    category = db.Column(db.String(50), nullable=True)
    status = db.Column(db.String(20), nullable=True)
    user_id = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'due_date': self.due_date,
            'category': self.category,
            'status': self.status,
            'user_id': self.user_id
        }


@app.route('/')
def home():
    return "Welcome to the Personal Task Manager API"


@app.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        tasks = Task.query.all()
        return jsonify([task.serialize() for task in tasks])
    except Exception as e:
        logging.error("Error occurred while fetching tasks: %s", e)
        abort(500, description="Internal Server Error")


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    try:
        task = Task.query.get(task_id)
        if task is None:
            abort(404, description="Task not found")
        return jsonify(task.serialize())
    except Exception as e:
        logging.error("Error occurred while fetching task: %s", e)
        abort(500, description="Internal Server Error")


@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = request.get_json()
        new_task = Task(
            name=data['name'],
            description=data['description'],
            due_date=data['due_date'],
            category=data['category'],
            status=data['status'],
            user_id=data['user_id']
        )
        db.session.add(new_task)
        db.session.commit()
        return jsonify(new_task.serialize()), 201
    except Exception as e:
        logging.error("Error occurred while creating task: %s", e)
        abort(500, description="Internal Server Error")


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    try:
        data = request.get_json()
        task = Task.query.get(task_id)
        if task is None:
            abort(404, description="Task not found")
        task.name = data['name']
        task.description = data['description']
        task.due_date = data['due_date']
        task.category = data['category']
        task.status = data['status']
        db.session.commit()
        return jsonify(task.serialize())
    except Exception as e:
        logging.error("Error occurred while updating task: %s", e)
        abort(500, description="Internal Server Error")


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        task = Task.query.get(task_id)
        if task is None:
            abort(404, description="Task not found")
        db.session.delete(task)
        db.session.commit()
        return '', 204
    except Exception as e:
        logging.error("Error occurred while deleting task: %s", e)
        abort(500, description="Internal Server Error")


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
