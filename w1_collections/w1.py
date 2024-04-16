data = ["as", 50, 1.2, (2023, 9, 10)]
_, shares, price, _ = data
print(shares, price)

record = ("a", "b", "c", "d")
a, b, *rest = record
print(rest)

nums = [1, 2, 3, 4, 5]


class Node:
    def __init__(self, value) -> None:
        self._value = value
        self._children = []

    def __repr__(
        self,
    ):  # tak się definiuje zazwyczaj repr w klasach, repr powinien zwracać coś, co wrzucone w interpreter stworzy instancję klasy
        return f"{self.__class__.__name__}({self._value})"

    def add_child(self, node):
        self._children.append(node)


a = {"a": 1, "b": 2}

from collections import Counter

from collections import defaultdict

d = defaultdict(list)
d["a"]
print(d)
