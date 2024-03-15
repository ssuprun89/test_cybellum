from flask import Blueprint, request, jsonify

from app.db.shemas import LoginSchema
from app.services import auth_service


router = Blueprint("auths", __name__)


@router.post("/login/")
def login():
    login_data = LoginSchema.parse_raw(request.data)
    return jsonify(auth_service.login(login_data))
