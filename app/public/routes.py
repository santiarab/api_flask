from datetime import datetime
from flask import jsonify, request
from . import public_bp
from flask_login import login_required, current_user
from .models import Task

# POST /tasks: Crear una nueva tarea.
@public_bp.route('/tasks', methods=['POST'])
@login_required
def post_task():
    data = request.json
    title = data.get('title')
    description = data.get('description')
    due_date_str = data.get('due_date')
    try:
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d') if due_date_str else None
    except ValueError:
        return jsonify({'error': 'Invalid date format. Please use YYYY-MM-DD'}), 400

    if title:
        task = Task(title=title, user_id=current_user.id ,description=description, due_date=due_date)
        task.save()
        return jsonify({
            'status': 'success',
            'message': 'Post Creado'
        }),200
    else:
        return jsonify( {
            'status': 'error',
            'message': 'Falta titulo'
        }),400

# GET /tasks: Listar todas las tareas.
@public_bp.route('/tasks', methods=['GET'])
@login_required
def list_tasks():
    tasks = Task.get_all_by_user(current_user.id).all()
    tasks_list = [task.to_dict() for task in tasks]
    return jsonify({
        'status': 'success',
        'list_task': tasks_list
    }), 200

# GET /tasks/<id>: Obtener una tarea específica.
@public_bp.route('/tasks/<int:task_id>', methods=['GET'])
@login_required
def get_task(task_id):
    task = Task.get_by_id(current_user.id,task_id)
    if task:
        return jsonify({
            'status': 'success',
            'task': task.to_dict()
        }), 200
    else:
        return jsonify({
            'status': 'error',
            'message': 'Task not found'
        }), 404

# PUT /tasks/<id>: Actualizar una tarea.
@public_bp.route('/tasks/<int:task_id>', methods=['PUT'])
@login_required
def update_task(task_id):
    task = Task.get_by_id(current_user.id, task_id)
    if not task:
        return jsonify({'status': 'error', 'message': 'Task not found'}), 404
    data = request.json
    title = data.get('title')
    description = data.get('description')
    due_date_str = data.get('due_date')
    status = data.get('status')
    try:
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d') if due_date_str else None
    except ValueError:
        return jsonify({'error': 'Invalid date format. Please use YYYY-MM-DD'}), 400
    if status:
        if status.lower() == 'true':
            status = True
        elif status.lower() == 'false':
            status = False
        else:
            return jsonify({'error': "Invalid status value. Expected 'true' or 'false'."}), 400

    task.update(title=title,description=description,due_date=due_date, status=status)
    return jsonify({
        'status': 'success',
        'task': task.to_dict(),
        'message': 'Task Updated'
    }), 200

# DELETE /tasks/<id>: Eliminar una tarea.
@public_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
@login_required
def delete_task(task_id):
    task = Task.get_by_id(current_user.id, task_id)
    if not task:
        return jsonify({'status': 'error', 'message': 'Task not found'}), 404
    task.delete()
    return jsonify({
        'status': 'success',
        'task': task.to_dict(),
        'message': 'Task deleted'
    }), 200

