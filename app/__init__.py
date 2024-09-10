from flask import Flask
<<<<<<< HEAD

def create_app(settings_module):
    app = Flask(__name__, instance_relative_config=True)
=======
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)
    migrate.init_app(app, db)

    from .public import public_bp
    app.register_blueprint(public_bp)
>>>>>>> 02204442b951446d6cb5401ade7015d89e25e12f
    return app