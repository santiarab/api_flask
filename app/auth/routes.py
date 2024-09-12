from flask import request,jsonify
from . import auth_bp
from . models import User
from flask_login import current_user, login_user, logout_user
from app import login_manager

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username  = data.get('username')
    password = data.get('password')

    if username and password:
        if User.get_by_username(username) is None:
            user = User(username=username)
            user.set_password(password)
            user.save()
            login_user(user,remember=True)
            return jsonify(response = {
                'status': 'success',
                'message': 'User created successfully'
            }),200
        else:
            return jsonify({
                'status': 'success',
                'message': 'User already exists'
            }),200
    else:
        return jsonify({
            'status': 'error',
            'message': 'Parameter username and password are required'
        }),200

@auth_bp.route('/signin', methods=['POST'])
def signin():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username and password:
        user = User.get_by_username(username)
        if user is None:
            return jsonify({
                'status': 'Error',
                'message': 'User not found'
            }),200
        else:
            if user.check_password(password):
                login_user(user,remember=True)
                return jsonify({
                    'status': 'success',
                    'message': 'User logged in'
                }),200
            else:
                return jsonify( {
                    'status': 'error',
                    'message': 'Password is incorrect'
                }),200
    else:
        return jsonify({
            'status': 'error',
            'message': 'Parameter username and password are required'
        }),400


@auth_bp.route('/login', methods=['GET'])
def login():
    if current_user.is_authenticated:
        return jsonify({
            'status': 'success',
            'message': f"User: '{current_user.username}' is already logged in!"
        }),200
    else:
        return jsonify( {
            'status': 'success',
            'message': 'Do not login yet!'
        }),200

@auth_bp.route('/logout')
def logout():
    logout_user()
    return jsonify({"status": "success"}),200


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)
