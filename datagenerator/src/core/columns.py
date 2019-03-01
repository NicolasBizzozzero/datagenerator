import random
import math
from typing import Union, List


DEFAULT_FORMAT_LABEL = r"{class_name}"

Number = Union[float, int]


class Column:
    def __init__(self, label: str = None,
                 missing_value_probability: float = 0.,
                 missing_value=math.nan):
        self.label = label
        self.missing_value_probability = missing_value_probability
        self.missing_value = missing_value

    def get_label(self) -> int:
        global DEFAULT_FORMAT_LABEL

        if self.label is None:
            return DEFAULT_FORMAT_LABEL.format(
                class_name=self.__class__.__name__
            )
        else:
            return self.label

    def _is_missing_value(self):
        return random.uniform(0, 1) < self.missing_value_probability


class RandomInteger(Column):
    def __init__(self, floor: int, ceil: int, *args,
                 **kwaargs):
        super().__init__(*args, **kwaargs)
        self.floor = floor
        self.ceil = ceil

    def compute_value(self) -> int:
        return self.missing_value if super()._is_missing_value() else \
            random.randint(self.floor, self.ceil)


class RandomFloat(Column):
    def __init__(self, floor: Number, ceil: Number, *args, **kwaargs):
        super().__init__(*args, **kwaargs)
        self.floor = floor
        self.ceil = ceil

    def compute_value(self) -> float:
        return self.missing_value if super()._is_missing_value() else \
            random.uniform(self.floor, self.ceil)


class Constant(Column):
    def __init__(self, value: object, *args, **kwaargs):
        super().__init__(*args, **kwaargs)
        self.value = value

    def compute_value(self) -> object:
        return self.missing_value if super()._is_missing_value() else \
            self.value


class Identifier(Column):
    def __init__(self, start: int, *args, **kwaargs):
        super().__init__(*args, **kwaargs)
        self.start = start
        self.current_value = start

    def compute_value(self) -> int:
        self.current_value += 1
        return self.missing_value if super()._is_missing_value() else \
            self.current_value - 1


class Choice(Column):
    def __init__(self, choices: List[object], *args, **kwaargs):
        super().__init__(*args, **kwaargs)
        self.choices = choices

    def compute_value(self) -> object:
        return self.missing_value if super()._is_missing_value() else \
            random.choice(self.choices)


class NaN(Column):
    def __init__(self, *args, **kwaargs):
        super().__init__(*args, **kwaargs)

    def compute_value(self) -> math.nan:
        return self.missing_value if super()._is_missing_value() else \
            math.nan


if __name__ == '__main__':
    pass
