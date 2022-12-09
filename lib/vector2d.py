class Point:
    @classmethod
    def zero(cls):
        return Point(0, 0)

    @classmethod
    def from_tuple(self, t):
        return Point(t[0], t[1])

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(%s, %s)" % (self.x, self.y)

    def __str__(self):
        return "Point(%s, %s)" % (self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Point(self.x / other, self.y / other)

    def __floordiv__(self, other):
        return Point(self.x // other, self.y // other)

    def __mod__(self, other):
        return Point(self.x % other, self.y % other)

    def __divmod__(self, other):
        return Point(self.x / other, self.y / other)

    def __pow__(self, other):
        return Point(self.x ** other, self.y ** other)

    def __lshift__(self, other):
        return Point(self.x << other, self.y << other)

    def __rshift__(self, other):
        return Point(self.x >> other, self.y >> other)

    def __and__(self, other):
        return Point(self.x & other, self.y & other)

    def __xor__(self, other):
        return Point(self.x ^ other, self.y ^ other)

    def __or__(self, other):
        return Point(self.x | other, self.y | other)

    def __div__(self, other):
        return Point(self.x / other, self.y / other)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __pos__(self):
        return self

    def __abs__(self):
        return Point(abs(self.x), abs(self.y))
