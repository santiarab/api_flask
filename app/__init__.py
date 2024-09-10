from flask import Flask

def create_app(settings_module):
    app = Flask(__name__, instance_relative_config=True)
    return app