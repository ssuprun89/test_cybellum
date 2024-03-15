from .user import UserService
from .auth import AuthService
from .post import PostService

user_service = UserService.get_service()
auth_service = AuthService.get_service()
post_service = PostService.get_service()
