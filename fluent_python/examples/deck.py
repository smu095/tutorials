# Implementing a simple card deck class
import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    """Card deck example from Chapter 1.

    Returns
    -------
    A full deck of cards (list of instances of the Card named tuple).
    """

    ranks = [str(i) for i in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
