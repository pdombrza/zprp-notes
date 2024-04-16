# Nowe obostrzenie do Circle - nie możemy przechowywać promienia wgl, tylko średnice. Bez getterów i setterów w Javie/C++ nie da się
import math


class Circle:
    """Represents a Circle"""

    def __init__(self, radius):
        self.radius = radius

    # gettery i settery w pythonie - pythoniczny sposób (pojebana akcja). api jest takie same - można dobierać się do promienia, ale nie jest on przechowywany
    @property
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0
