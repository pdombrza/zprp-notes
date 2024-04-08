import pytest
from typing import NamedTuple

class Case(NamedTuple):
    input_n: int
    expected: int


def square(n: float) -> float:
    return n ** 2


@pytest.mark.parametrize(
    ("input_n", "expected"),
    [
        (1, 1),
        (-1, 1),
        (2, 4),
        pytest.param(-2, 4, id="negative case"), # w parametryzacji można dodawać nazwy
        Case(input_n=0, expected=0),
        ]
)
def test_square_integers(input_n, expected):
    assert square(input_n) == expected


@pytest.mark.parametrize(
    "input_n",
    [
        "a",
        {},
        [],
    ]
)
def test_square_error(input_n):
    with pytest.raises(TypeError):
        square(input_n)