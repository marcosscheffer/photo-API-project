from .health_view import bp as health_bp

def register_blueprints(app):
    app.register_blueprint(health_bp)