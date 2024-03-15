from flask import Blueprint, request, jsonify

from app.db.shemas import UserCreateSchema
from app.services import user_service

router = Blueprint("users", __name__)


@router.post("/")
def create_user():
    user_request_data = UserCreateSchema.parse_raw(request.data)
    user = user_service.create_user(user_request_data)
    return jsonify(user.dict())


@router.get("/<int:user_id>/")
def get_user(user_id: int):
    user = user_service.get_user_by_id(user_id)
    return jsonify(user.dict())
