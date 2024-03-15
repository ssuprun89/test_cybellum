from werkzeug.exceptions import NotFound

from app.config import get_settings
from app.db.models import Post, Comment
from app.db.shemas import (
    PostCreateSchema,
    PostSchema,
    CommentPostCreateSchema,
    CommentPostSchema,
)
from app.services.base import BaseService

settings = get_settings()


class PostService(BaseService):

    def create_post(self, data: PostCreateSchema, auth_user) -> PostSchema:
        data_dict = data.dict()
        data_dict["user_id"] = auth_user
        post = Post.objects.create(**data_dict)
        return PostSchema(**post.__dict__)

    def get_post(self, post_id: int) -> PostSchema:
        post = Post.objects.get_or_none(id=post_id)
        if not post:
            raise NotFound("Post not found")
        return PostSchema(**post.__dict__)

    def get_posts_by_criteria(self, **kwargs) -> list[dict]:
        list_posts = Post.objects.filter(**kwargs)
        return [PostSchema(**post.__dict__).dict() for post in list_posts]

    def create_comment_for_post(
        self, data: CommentPostCreateSchema, auth_user
    ) -> CommentPostSchema:
        data_dict = data.dict()
        data_dict["user_id"] = auth_user
        post = Comment.objects.create(**data_dict)
        return CommentPostSchema(**post.__dict__)

    def get_comments(self, post_id: int) -> list[dict]:
        list_comments = Comment.objects.filter(post_id=post_id)
        return [
            CommentPostSchema(**comment.__dict__).dict() for comment in list_comments
        ]
