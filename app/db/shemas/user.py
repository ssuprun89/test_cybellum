import datetime

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    created_at: datetime.datetime
    username: str
    email: str


class UserCreateSchema(BaseModel):
    username: str
    password: str
    email: str
