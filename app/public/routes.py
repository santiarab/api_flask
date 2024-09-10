from flask import jsonify
from . import public_bp



# POST /tasks: Crear una nueva tarea.
# GET /tasks: Listar todas las tareas.
# GET /tasks/<id>: Obtener una tarea específica.
# PUT /tasks/<id>: Actualizar una tarea.
# DELETE /tasks/<id>: Eliminar una tarea.



@public_bp.route('/tasks', methods=['POST'])
def hello():
    return jsonify({"message": "Hello, World!"})