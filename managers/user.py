from app import db
from managers.manager import Manager
from models.user import User


class UserManager(Manager):
    _collection = db.users
    _model = User
