from app import db
from managers.manager import Manager
from models.game import Game


class GameManager(Manager):
    _collection = db.games
    _model = Game
