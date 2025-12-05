import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET = os.getenv('JWT_SECRET', SECRET_KEY)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASS = os.getenv('MYSQL_PASS', '')
    MYSQL_HOST = os.getenv('MYSQL_HOST', '127.0.0.1')
    MYSQL_PORT = os.getenv('MYSQL_PORT', '3306')
    MYSQL_DB = os.getenv('MYSQL_DB', 'jwt_app')

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    )

    ACCESS_TOKEN_EXPIRES = int(os.getenv('ACCESS_TOKEN_EXPIRES_MIN', 15))  # minutes
    REFRESH_TOKEN_EXPIRES = int(os.getenv('REFRESH_TOKEN_EXPIRES_DAYS', 7))  # days

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
