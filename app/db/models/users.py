from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import BaseModel, OrmManager


class User(BaseModel, OrmManager):

    __tablename__ = "users"

    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    posts = relationship("Post", back_populates="user", uselist=False, lazy="joined")
    comments = relationship(
        "Comment", back_populates="user", uselist=False, lazy="joined"
    )
