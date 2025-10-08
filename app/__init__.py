from flask import Flask
from .extensions import init_extensions
from .config import config_map
from .views import register_blueprints

from .models.user_model import UserModel


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config_map[config_name])
    init_extensions(app)
    register_blueprints(app)
    return app