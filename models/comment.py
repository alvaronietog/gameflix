import json
from dataclasses import dataclass, field

from bson import ObjectId

from models.model import Model


@dataclass
class Comment(Model):
    user: ObjectId
    game: ObjectId
    _rate: int = 0
    comment: str = ''

    @property
    def rate(self):
        return self._rate

    @_rate.setter
    def rate(self, value: int) -> None:
        self._rate = min(max(0, value), 5)