from flask import Blueprint, jsonify
from app.auth.utils import token_required

bp = Blueprint('main', __name__)

@bp.route('/ping', methods=['GET'])
def public():
    return jsonify({'message': 'Successful'})

@bp.route('/dashboard', methods=['GET'])
@token_required
def dashboard(current_user):
    return jsonify({'message': f'Welcome {current_user.name}', 'email': current_user.email})
