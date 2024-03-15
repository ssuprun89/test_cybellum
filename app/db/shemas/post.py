from pydantic import BaseModel


class PostCreateSchema(BaseModel):
    content: str
    title: str


class CommentPostCreateSchema(BaseModel):
    content: str
    post_id: int


class PostSchema(BaseModel):
    id: int
    content: str
    title: str
    user_id: int


class CommentPostSchema(BaseModel):
    id: int
    content: str
    post_id: int
    user_id: int
