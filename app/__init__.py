from flask import Flask, jsonify

from app.config import get_settings
from app.routes import user_router, auth_router, post_router

settings = get_settings()


def create_flask_app():

    app = Flask(__name__)
    app.register_blueprint(user_router, url_prefix="/api/users/")
    app.register_blueprint(auth_router, url_prefix="/api/auth/")
    app.register_blueprint(post_router, url_prefix="/api/posts/")

    @app.errorhandler(Exception)
    def handle_foo_exception(error):
        if hasattr(error, "description"):
            error, code = error.description, error.code
        elif hasattr(error, "orig"):
            error, code = error.orig.args, 500
        else:
            error, code = "Unknown error", 400
        response = jsonify({"derail": error})
        response.status_code = code
        return response

    return app
