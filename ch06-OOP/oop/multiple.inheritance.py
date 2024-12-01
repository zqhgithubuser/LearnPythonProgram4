class Shape:
    geometric_type = "Generic Shape"

    def area(self):
        raise NotImplemented

    def get_geometric_type(self):
        return self.geometric_type


class Plotter:
    def plot(self, ratio, top_left):
        print("Plotting at {}, ratio {}.".format(top_left, ratio))


class Polygon(Shape, Plotter):
    geometric_type = "Polygon"


class RegularPolygon(Polygon):  # Is A Polygon
    geometric_type = "Regular Polygon"

    def __init__(self, side):
        self.side = side


class RegularHexagon(RegularPolygon):  # Is A RegularPolygon
    geometric_type = "RegularHexagon"

    def area(self):
        return 1.5 * (3**0.5 * self.side**2)


class Square(RegularPolygon):  # Is A RegularPolygon
    geometric_type = "Square"

    def area(self):
        return self.side * self.side


hexagon = RegularHexagon(10)
print(hexagon.area())
print(hexagon.get_geometric_type())
hexagon.plot(0.8, (75, 77))

square = Square(12)
print(square.area())
print(square.get_geometric_type())  # Square
square.plot(0.93, (74, 75))  # Plotting at (74, 75), ratio 0.93.
print(square.__class__.__mro__)
# (<class '__main__.Square'>, <class '__main__.RegularPolygon'>,
# <class '__main__.Polygon'>, <class '__main__.Shape'>,
# <class '__main__.Plotter'>, <class 'object'>)
