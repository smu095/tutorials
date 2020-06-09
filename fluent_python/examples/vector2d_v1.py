"""vector2d_v1.py: Implementation of Vector2d allowing conversions from bytes to Vector2d instance."""

from array import array
import math

class Vector2d:
    typecode = "d" # Used when converting Vector2d instances to/from bytes

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self): # Makes Vector2d iterable, allows unpacking
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return "{}({!r}, {!r})".format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

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
