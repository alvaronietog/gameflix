from dataclasses import dataclass, asdict


@dataclass
class Model:
    def to_dict(self) -> dict:
        return asdict(self)

    def from_dict(self, instance: dict):
        return Model(**instance)