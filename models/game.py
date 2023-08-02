import json
from dataclasses import dataclass, field

from bson import ObjectId

from models.model import Model


@dataclass(kw_only=True)
class Game(Model):
    name: str
    description: str
    developers: str = ''
    publisher: str = ''
    picture: str = ''
    votes: int = field(init=False, default=0)
    _ranking: int = field(init=False, default=0)
    comments: list[ObjectId] = field(default_factory=list)

    @property
    def ranking(self):
        return self._ranking

    @ranking.setter
    def ranking(self, value: int) -> None:
        self._ranking = min(max(0, value), 5)
