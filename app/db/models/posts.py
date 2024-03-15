from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from .base import BaseModel, OrmManager


class Post(BaseModel, OrmManager):

    __tablename__ = "posts"

    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="posts")
    comments = relationship(
        "Comment", back_populates="post", uselist=False, lazy="joined"
    )


class Comment(BaseModel, OrmManager):

    __tablename__ = "comments"

    content = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    post = relationship("Post", back_populates="comments")
    user = relationship("User", back_populates="comments")
