from flask import jsonify
from . import public_bp



# POST /tasks: Crear una nueva tarea.
# GET /tasks: Listar todas las tareas.
# GET /tasks/<id>: Obtener una tarea específica.
# PUT /tasks/<id>: Actualizar una tarea.
# DELETE /tasks/<id>: Eliminar una tarea.


# POST /tasks: Crear una nueva tarea.
@public_bp.route('/tasks', methods=['POST'])
def post_task():
    return "Esto es la raiz"

# GET /tasks: Listar todas las tareas.
@public_bp.route('/tasks', methods=['GET'])
def list_tasks():
    return "Esto es la raiz"

# GET /tasks/<id>: Obtener una tarea específica.
@public_bp.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    return "Esto es la raiz"

# PUT /tasks/<id>: Actualizar una tarea.
@public_bp.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    return "Esto es la raiz"

# DELETE /tasks/<id>: Eliminar una tarea.
@public_bp.route('/', methods=['GET'])
def delete_task():
    return "Esto es la raiz"

