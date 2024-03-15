import hashlib

from werkzeug.exceptions import NotFound

from app.config import get_settings
from app.db.models import User
from app.db.shemas import UserCreateSchema, UserSchema
from app.services.base import BaseService

settings = get_settings()


class UserService(BaseService):

    @staticmethod
    def hash_password(password: str) -> str:
        password = password + settings.SECRET_KEY
        return hashlib.sha256(password.encode()).hexdigest()

    def create_user(self, data: UserCreateSchema) -> UserSchema:
        data_dict = data.dict()
        data_dict["password_hash"] = self.hash_password(data_dict.pop("password"))
        user = User.objects.create(**data_dict)
        return UserSchema(**user.__dict__)

    def get_user_by_id(self, user_id: int) -> UserSchema:
        user = User.objects.get_or_none(id=user_id)
        if not user:
            raise NotFound(description="User not found")
        return UserSchema(**user.__dict__)
