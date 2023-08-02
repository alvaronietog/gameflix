import json
from dataclasses import dataclass


@dataclass
class Model:
    def to_dict(self) -> dict:
        return json.loads(self.to_json())

    def to_json(self) -> str:
        return json.dumps(self.__dict__)
