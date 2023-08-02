import json
from dataclasses import dataclass, field

from bson import ObjectId

from models.model import Model


@dataclass(kw_only=True)
class User(Model):
    name: str
    last_name: str
    address: str
    email: str
    _ranking: int = 0
    picture: str = ''
    comments: list[ObjectId] = field(default_factory=list)
    admin: bool = False

    @property
    def ranking(self):
        return self._ranking

    @ranking.setter
    def ranking(self, value: int) -> None:
        self._ranking = min(max(0, value), 5)
