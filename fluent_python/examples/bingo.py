"""Example 11-12. BingoCage is a concrete subclass of Tombola."""
import random
from examples.tombola import Tombola


class BingoCage(Tombola):
    def __init__(self, items):
        self._randomiser = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomiser.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty BingoCage")

    def __call__(self):
        self.pick()
