"""Example 9.7. vector2d_v4.py: implementation of hash"""

from array import array
import math


class Vector2d:
    typecode = "d"  # Used when converting Vector2d instances to/from bytes

    def __init__(self, x, y):
        self.__x = float(
            x
        )  # Use exactly two leading underscores to make attribute private
        self.__y = float(y)

    @property  # Marks the getter method of a property
    def x(self):
        return self.__x

    @property  # Marks the getter method of a property
    def y(self):
        return self.__y

    def __iter__(self):  # Makes Vector2d iterable, allows unpacking
        return (i for i in (self.x, self.y))

    # Hack to get examples in chapter 13 to work
    def __len__(self):
        return len((self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return "{}({!r}, {!r})".format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def angle(self):
        return math.atan2(self.y, self.x)

    def __format__(self, fmt_spec=""):
        if fmt_spec.endswith("p"):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = "<{}, {}>"
        else:
            coords = self
            outer_fmt = "({}, {})"
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
