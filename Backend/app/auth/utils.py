import jwt
import uuid
from datetime import datetime, timedelta, timezone
from functools import wraps
from flask import current_app, request, jsonify
from app.extensions import db
from app.models import User, RevokedToken

def _now_utc():
    return datetime.now(timezone.utc)

def create_access_token(user_public_id):
    secret = current_app.config['JWT_SECRET']
    exp = _now_utc() + timedelta(minutes=current_app.config['ACCESS_TOKEN_EXPIRES'])
    jti = str(uuid.uuid4())
    payload = {
        'sub': user_public_id,
        'jti': jti,
        'type': 'access',
        'iat': _now_utc().timestamp(),
        'exp': exp.timestamp()
    }
    token = jwt.encode(payload, secret, algorithm='HS256')
    return token, jti, exp

def create_refresh_token(user_public_id):
    secret = current_app.config['JWT_SECRET']
    exp = _now_utc() + timedelta(days=current_app.config['REFRESH_TOKEN_EXPIRES'])
    jti = str(uuid.uuid4())
    payload = {
        'sub': user_public_id,
        'jti': jti,
        'type': 'refresh',
        'iat': _now_utc().timestamp(),
        'exp': exp.timestamp()
    }
    token = jwt.encode(payload, secret, algorithm='HS256')
    return token, jti, exp

def decode_token(token):
    secret = current_app.config['JWT_SECRET']
    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise
    except Exception:
        raise

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization', None)
        token = None

        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
        else:
            # fallback to cookie if needed
            token = request.cookies.get('access_token')

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            payload = decode_token(token)
            if payload.get('type') != 'access':
                return jsonify({'message': 'Invalid token type'}), 401

            jti = payload.get('jti')
            if RevokedToken.is_jti_revoked(jti):
                return jsonify({'message': 'Token has been revoked'}), 401

            user = User.query.filter_by(public_id=payload['sub']).first()
            if not user:
                return jsonify({'message': 'User not found'}), 401

        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expired'}), 401
        except Exception:
            return jsonify({'message': 'Token invalid'}), 401

        return f(current_user=user, *args, **kwargs)
    return decorated
