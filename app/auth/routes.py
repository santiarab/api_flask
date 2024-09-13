from flask import request, jsonify, render_template, redirect, url_for
from . import auth_bp
from .form import SignupForm, LoginForm
from . models import User
from flask_login import current_user, login_user, logout_user
from app import login_manager
from urllib.parse import urlparse

@auth_bp.route('/signup', methods=["GET", "POST"])
def signup(next_page=None):
    if current_user.is_authenticated:
        return redirect(url_for('public.task'))
    form = SignupForm()
    error = None
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.get_by_username(username)
        if user is not None:
            error = f'Username already taken'
        else:
            user = User(username=username)
            user.set_password(password)
            user.save()
            login_user(user, remember=True)
            next_page = request.args.get('next', None)
            if not next_page or urlparse(next_page).netloc != '':
                next_page = url_for('public.task')
            return redirect(next_page)
    return render_template("signup_form.html", form=form, error=error)

@auth_bp.route('/signin', methods=["GET", "POST"])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('public.task'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_username(form.username.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('public.task')
            return redirect(next_page)
    return render_template('login_form.html', form=form)

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
    return redirect(url_for('public.index'))


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)
