from dataclasses import dataclass, field

from bson import ObjectId


class Operator:
    equal = '$eq'
    not_equal = '$neq'
    greater = '$gt'
    greater_equal = '$gte'
    less = '$lt'
    less_equal = '$lte'
    inside = '$in'


@dataclass(kw_only=True)
class Filter:
    field: str
    operator: Operator
    value: str | ObjectId | list[ObjectId]
    formatted_filter: dict = field(init=False)

    def __post_init__(self):
        self.formatted_filter = {
            self.field: {self.operator: self.value}
        }
