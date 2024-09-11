from flask import request,jsonify
from . import auth_bp
from . models import User


@auth_bp.route('/signup', methods=['POST'])
def login():
    username  = request.args.get('username')
    password = request.args.get('password')

    if username and password:

        if User.get_by_username(username) is None:
            user = User(username=username)
            user.set_password(password)
            user.save()
            response = {
                'status': 'success',
                'message': 'Usuario creado'
            }
        else:
            response = {
                'status': 'success',
                'message': 'Usuario ya existe'
            }
    else:
        response = {
            'status': 'error',
            'message': 'Faltan parámetros'
        }
    return jsonify(response)