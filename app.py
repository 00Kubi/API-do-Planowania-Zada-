from flask import Flask, request, jsonify
from models import Task

app = Flask(__name__)

tasks = {}
task_counter = 1

@app.route('/')
def home():
    return jsonify({'message': 'Witaj w API do planowania zadań!'})

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_counter
    data = request.json
    title = data.get('title')
    description = data.get('description')
    dependencies = data.get('dependencies', [])
    interval = data.get('interval')

    if not title:
        return jsonify({'message': 'Tytuł jest wymagany!'}), 400

    task = Task(task_counter, title, description, dependencies, interval)
    tasks[task_counter] = task
    task_counter += 1
    return jsonify({'task_id': task.task_id}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [
        {
            'task_id': task.task_id,
            'title': task.title,
            'description': task.description,
            'dependencies': task.dependencies,
            'interval': task.interval,
            'created_at': task.created_at.isoformat()
        }
        for task in tasks.values()
    ]
    return jsonify(task_list), 200

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = tasks.get(task_id)
    if not task:
        return jsonify({'message': 'Zadanie nie zostało znalezione!'}), 404
    
    return jsonify({
        'task_id': task.task_id,
        'title': task.title,
        'description': task.description,
        'dependencies': task.dependencies,
        'interval': task.interval,
        'created_at': task.created_at.isoformat()
    }), 200

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = tasks.get(task_id)
    if not task:
        return jsonify({'message': 'Zadanie nie zostało znalezione!'}), 404

    data = request.json
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.dependencies = data.get('dependencies', task.dependencies)
    task.interval = data.get('interval', task.interval)

    return jsonify({'message': 'Zadanie zaktualizowane!'}), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id not in tasks:
        return jsonify({'message': 'Zadanie nie zostało znalezione!'}), 404
    
    del tasks[task_id]
    return jsonify({'message': 'Zadanie usunięte!'}), 204

@app.route('/tasks/due', methods=['GET'])
def get_due_tasks():
    due_tasks = [task for task in tasks.values() if task.is_due()]
    return jsonify([{'task_id': task.task_id, 'title': task.title} for task in due_tasks]), 200

if __name__ == '__main__':
    app.run(debug=True)
