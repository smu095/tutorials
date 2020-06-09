"""Example 11-8. frenchdeck2.py: FrenchDeck2, a subclass of collections.MutableSequence"""

import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in suits for rank in ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    # Implemented to allow shuffling
    def __setitem__(self, position, value):
        self._cards[position] = value

    # Enforced by collections.MutableSequence
    def __delitem__(self, position):
        del self._cards[position]

    # Enforced by collections.MutableSequence
    def insert(self, position, value):
        self._cards.insert(position, value)
