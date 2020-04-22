from examples.tombola import Tombola
from examples.bingo import BingoCage


class AddableBingoCage(BingoCage):
    def __add__(self, other):
        if isinstance(other, Tombola):
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented  # noqa: F901

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other.inspect()
        else:
            try:
                other_iterable = iter(other)
            except TypeError:
                self_cls = type(self).__name__
                msg = f"right operand in += must be {self_cls!r} or an iterable"
                raise TypeError(msg)
        self.load(other_iterable)
        return self
