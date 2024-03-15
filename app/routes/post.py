from flask import Blueprint, request, jsonify

from app.db.shemas import PostCreateSchema, CommentPostCreateSchema
from app.routes.base import login_required
from app.services import post_service

router = Blueprint("posts", __name__)


@router.post("/")
@login_required()
def create_posts(auth_user_id: int):
    post_request_data = PostCreateSchema.parse_raw(request.data)
    post = post_service.create_post(post_request_data, auth_user_id)
    return jsonify(post.dict())


@router.get("/")
@router.get("/<int:post_id>/")
def get_post_data(post_id: int = None):
    if post_id is None:
        return jsonify(post_service.get_posts_by_criteria())
    else:
        return jsonify(post_service.get_post(post_id).dict())


@router.post("/comments/")
@login_required()
def create_comments(auth_user_id: int):
    comment_request_data = CommentPostCreateSchema.parse_raw(request.data)
    comment = post_service.create_comment_for_post(comment_request_data, auth_user_id)
    return jsonify(comment.dict())


@router.get("/comments/<int:post_id>/")
def get_comments_for_post(post_id: int):
    return jsonify(post_service.get_comments(post_id))
