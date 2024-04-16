from typing import NamedTuple


class Color(NamedTuple):
    hue: int
    saturation: float
    lightness: float = 0.5


c = Color(33, 1.0)
c._replace(hue=120)
c._asdict()
c._asdict()
tuple(c)
Color.__annotations__

hue, saturation, lightness = c
