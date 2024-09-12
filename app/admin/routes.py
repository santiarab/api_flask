from flask import jsonify
from flask_login import login_required

from . import admin_bp
from app.auth.decorators import admin_required
from app.auth.models import User


@admin_bp.route("/admin/user/delete/<int:user_id>", methods=['DELETE'])
@login_required
@admin_required
def delete_user(user_id):
    user = User.get_by_id(user_id)
    if user is None:
        return jsonify({'status':"error", 'message': 'User not found'}), 404
    user.delete()
    return jsonify({'status': 'success', 'message': 'User was deleted'}), 200

@admin_bp.route("/admin/user/users", methods=['GET'])
@login_required
@admin_required
def list_users():
    users = User.get_all()
    users_list = [user.to_dict() for user in users]
    return jsonify({'status': 'success', 'list_users': users_list}), 200