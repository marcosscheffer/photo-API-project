from .health_view import bp as health_bp
from .auth_view import bp as auth_bp

def register_blueprints(app):
    app.register_blueprint(health_bp, url_prefix="/api/v1")
    app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")