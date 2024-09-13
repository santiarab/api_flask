from calendar import error
from datetime import datetime
from flask import jsonify, request, current_app, render_template, url_for, redirect
from . import public_bp
from flask_login import login_required, current_user
from .form import CreateTask, GetTaskByTitle, GetTaskById, UpdateTask
from .models import Task
from urllib.parse import urlparse

@public_bp.route("/")
def index():
    return render_template("index.html")

@public_bp.route("/task")
def task():
    return render_template("task.html")

# POST /tasks: Crear una nueva tarea.
@public_bp.route('/task/create', methods=['GET','POST'])
@login_required
def post_task():
    form = CreateTask()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        due_date = form.due_date.data
        print("Title:", title)
        print("Description:", description)
        print("Due Date:", due_date)
        task = Task(title=title, user_id=current_user.id ,description=description, due_date=due_date)
        task.save()
        next_page = request.args.get('next', None)
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('public.task')
        return redirect(next_page)
    return render_template("create_task.html", form=form)



# GET /tasks: Listar todas las tareas.
@public_bp.route('/task/list', methods=['GET'])
@login_required
def list_tasks():
    tasks = Task.get_all_by_user(current_user.id).all()
    tasks_list = [task.to_dict() for task in tasks]
    return jsonify({
        'status': 'success',
        'list_task': tasks_list
    }), 200

# GET /tasks/<id>: Obtener una tarea específica.
@public_bp.route('/task/get', methods=['GET','POST'])
@login_required
def get_task():
    form = GetTaskByTitle()
    if form.validate_on_submit():
        tasks = Task.get_by_title(form.title.data)
        tasks_list = [task.to_dict() for task in tasks]
        return render_template("list_task.html", tasks=tasks_list)
    return render_template("get_task.html", form=form)

@public_bp.route('/task/update/<int:task_id>', methods=['GET','POST'])
@login_required
def update_task(task_id:int):
    form_update = UpdateTask()
    if form_update.validate_on_submit():
        title = form_update.title.data
        description = form_update.description.data
        due_date = form_update.due_date.data
        status = form_update.status.data
        task = Task.get_by_id(user_id= current_user.id,id= task_id )
        task.update(title=title, description=description, due_date=due_date, status=status)
        next_page = request.args.get('next', None)
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('public.task')
        return redirect(next_page)
    return render_template("update_task.html", form=form_update)

# PUT /tasks/<id>: Actualizar una tarea.
@public_bp.route('/task/update', methods=['GET','POST'])
@login_required
def get_task_by_id():
    form_task = GetTaskById()
    error = None
    if form_task.validate_on_submit():
        task = Task.get_by_id(user_id= current_user.id,id= form_task.id.data )
        if task is None:
            error = "Task not found"
        else:
            next_page = request.args.get('next', None)
            if not next_page or urlparse(next_page).netloc != '':
                next_page = url_for('public.update_task', task_id=task.id)
            return redirect(next_page)
    return render_template("get_task_id.html", form=form_task, error=error)

# DELETE /tasks/<id>: Eliminar una tarea.
@public_bp.route('/task/delete', methods=['DELETE'])
@login_required
def delete_task():
    return True

