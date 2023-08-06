from src.dao.base import BaseDAO
from src.user.model import User


class UserDAO(BaseDAO):
    model = User
