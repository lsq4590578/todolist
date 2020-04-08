from flask import Blueprint, jsonify, request
from flask_login import current_user, login_user, logout_user
from backend.forms import RegisterForm,LoginForm
from backend.models import User, db

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
    user_data = request.get_json()
    form = RegisterForm(data=user_data)
    if form.validate():
        user = User(username=user_data['username'], password=user_data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error', 'message': form.errors}), 400


@bp.route('/login', methods=['POST'])
def login():
    user_data = request.get_json()
    form = LoginForm(data=user_data)
    if form.validate():
        user = form.get_user()
        login_user(user, remember=form.remember.data)
        return jsonify({'status': 'success', 'user': user.to_json()})
    return jsonify({'status': 'error', 'message': form.errors}), 403


@bp.route('/session')
def get_session():
    if not current_user.is_authenticated:
        return jsonify({'status': 'error'}), 401
    return jsonify({'status': 'success', 'user': current_user.to_json()})


@bp.route('/logout')
def logout():
    logout_user()
    return jsonify({'status': 'success'})
