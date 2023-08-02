from main import db
from models.game import Game


class GameManager:
    __collection = 'game'
    __model = Game

    def create(self, **kwargs):
        collection = db[self.__collection]
        print(kwargs)
