from flask import Flask
from app.api.blueprint import hello_route as hello


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(hello)

    return app
