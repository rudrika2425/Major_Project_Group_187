from flask import Flask
from config import DevelopmentConfig
from .extensions import db, migrate
from .auth.routes import bp as auth_bp
from .main.routes import bp as main_bp

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app
