import datetime

from werkzeug.exceptions import NotFound, Unauthorized

import jwt

from app.config import get_settings
from app.db.models import User
from app.db.shemas import LoginSchema
from app.services.user import UserService
from app.services.base import BaseService

settings = get_settings()


class AuthService(BaseService):

    @staticmethod
    def generate_payload(user):
        return {
            "exp": datetime.datetime.utcnow()
            + datetime.timedelta(hours=settings.JWT_EXPIRATION_HOURS),
            "iat": datetime.datetime.utcnow(),
            "user_id": user.id,
        }

    def login(self, data: LoginSchema) -> dict:
        password_hash = UserService.hash_password(data.password)
        user = User.objects.get_or_none(email=data.email, password_hash=password_hash)
        if not user:
            raise NotFound(description="User not found")
        return {
            "access_token": jwt.encode(
                self.generate_payload(user), settings.SECRET_KEY, algorithm="HS256"
            )
        }

    def check_token(self, token) -> int:
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return payload["user_id"]
        except jwt.ExpiredSignatureError:
            raise Unauthorized(description="Signature expired. Please log in again.")
        except jwt.InvalidTokenError:
            raise Unauthorized(description="Invalid token. Please log in again.")
