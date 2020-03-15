from abc import ABC, abstractmethod
from dataclasses import dataclass
from collections import namedtuple

Customer = namedtuple("Customer", "name fidelity")

@dataclass
class LineItem:
    product: str
    quantity: int
    price: float

    def total(self):
        return self.price * self.quantity


# Context
class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, "__total"):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total # Note double leading underscore to prevent accidental modification

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = "<Order total: {:.2f} due {:.2f}"
        return fmt.format(self.total(), self.due())