from functools import wraps

from flask import request
from werkzeug.exceptions import Unauthorized

from app.services import auth_service


def login_required():
    def _login_required(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            header = request.headers.get("Authorization")
            if header:
                prefix, token = header.split(" ")
                user_id = auth_service.check_token(token)
                kwargs.update({"auth_user_id": user_id})
                return func(*args, **kwargs)
            else:
                raise Unauthorized(description="Invalid token. Please log in again.")

        return wrapper

    return _login_required
