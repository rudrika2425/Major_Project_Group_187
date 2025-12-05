from flask import Blueprint, request, jsonify, current_app, make_response
from app.extensions import db
from app.models import User, RevokedToken
from .utils import create_access_token, create_refresh_token, decode_token

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json() or {}
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not (name and email and password):
        return jsonify({'message': 'Missing fields'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'User already exists'}), 400

    user = User(name=name, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created', 'public_id': user.public_id}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')

    if not (email and password):
        return jsonify({'message': 'Missing credentials'}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({'message': 'Invalid credentials'}), 401

    access_token, access_jti, access_exp = create_access_token(user.public_id)
    refresh_token, refresh_jti, refresh_exp = create_refresh_token(user.public_id)

    # Optional: persist refresh token jti to DB if you want to be able to revoke it separately.
    # For now we just return tokens; for logout we mark jti revoked.

    resp = make_response({
        'access_token': access_token,
        'refresh_token': refresh_token,
        'access_expires': access_exp.isoformat(),
        'refresh_expires': refresh_exp.isoformat()
    })
    # You can also set cookies (secure, httponly) if you prefer
    # resp.set_cookie('access_token', access_token, httponly=True, secure=True)
    return resp, 200

@bp.route('/refresh', methods=['POST'])
def refresh():
    data = request.get_json() or {}
    refresh_token = data.get('refresh_token') or request.cookies.get('refresh_token')
    if not refresh_token:
        return jsonify({'message': 'Refresh token missing'}), 401
    try:
        payload = decode_token(refresh_token)
        if payload.get('type') != 'refresh':
            return jsonify({'message': 'Invalid token type'}), 401
        # check if jti revoked
        if RevokedToken.is_jti_revoked(payload.get('jti')):
            return jsonify({'message': 'Token revoked'}), 401
        user = User.query.filter_by(public_id=payload['sub']).first()
        if not user:
            return jsonify({'message': 'User not found'}), 401

        access_token, access_jti, access_exp = create_access_token(user.public_id)
        return jsonify({'access_token': access_token, 'access_expires': access_exp.isoformat()}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Refresh token expired'}), 401
    except Exception:
        return jsonify({'message': 'Invalid token'}), 401

@bp.route('/logout', methods=['POST'])
def logout():
    # Expect access_token or refresh_token jti to revoke them
    data = request.get_json() or {}
    token = data.get('token')
    if not token:
        return jsonify({'message': 'Token required to revoke'}), 400
    try:
        payload = decode_token(token)
        jti = payload.get('jti')
        rt = RevokedToken(jti=jti)
        db.session.add(rt)
        db.session.commit()
        return jsonify({'message': 'Token revoked'}), 200
    except Exception:
        return jsonify({'message': 'Invalid token'}), 400
