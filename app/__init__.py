from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager


login_manager = LoginManager()
db = SQLAlchemy()
migrate_db = Migrate()

def create_app(config_class :Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate_db.init_app(app, db)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    from .public import public_bp
    app.register_blueprint(public_bp)

    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    return app