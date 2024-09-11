from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate_db = Migrate()

def create_app(config_class :Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate_db.init_app(app, db)

    from .public import public_bp
    app.register_blueprint(public_bp)

    return app