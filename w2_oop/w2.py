def foo(a, b, /, c, *, d=100, e=200):
    pass


"""Advanced circles analityc toolkit"""
import math


class Circle:
    """Represents a circle"""  # pisać docsa z bomby zamiast pass (no bo wtedy docsa masz od razu)

    version = "0.1"  # wersja klasy

    def __init__(
        self, radius
    ):  # init to nie do końca konstruktor bo jest wołany jak obiekt już istnieje,
        self.radius = radius  # tak naprawdę konstruktorem jest __new__ co rzeczywiście tworzy obiekt, init inicjalizuje obiekt, który już jest utworzony

    def area(self):
        # area has to be computed based on perimeter (new regulations)
        p = self.__perimeter()  #
        r = (
            p / math.pi / 2.0
        )  # niszczymy tak dziedziczenie - kod ziomków od opon (no bo oni sobie przeciążyli to)
        return math.pi * r**2.0

    def perimeter(self):
        return 2.0 * math.pi * self.radius

    __perimeter = perimeter

    @classmethod
    def from_bbd(
        cls, bbd
    ):  # przez konwencję cls zamiast self, jako domyślny argument wywołania wstrzykiwana jest cała klasa(tak jak self wstrzykuje instancję)
        radius = bbd / 2.0 / math.sqrt(2.0)  # compute the radius somehow
        return cls(
            radius
        )  # analogiczne do Circle(radius) aczkolwiek lepiej nie hardkodować nazwy klasy bo się wywali przy dziedziczeniu

    # to pozwala na wykorzystanie kilku konstruktorów (Circle.from_bbd(10))

    @staticmethod
    def angle_to_grade(
        angle,
    ):  # można dokleić metodę do klasy korzystając ze @staticmethod
        return math.tan(math.radians(angle) * 100)
