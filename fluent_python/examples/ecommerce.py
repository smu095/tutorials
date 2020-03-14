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
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, "__total"):
            self.__total = sum(item.total() for item in self.cart())
        return (
            self.__total()
        )  # Note double leading underscore to prevent accidental modification

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() * discount

    def __repr__(self):
        fmt = "<Order total: {:.2f} due {.:2f}"
        return fmt.format(self.total(), self.due())


# Strategy
class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        """Return discount as positive dollar amount."""


# Concrete strategies
class FidelityPromo(Promotion):
    def discount(self, order):
        """5% discount for customers with 1000 or more fidelity points."""
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    def discount(self, order):
        """10% discount for line orders with 20 or more units."""
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount


class LargeOrderPromo(Promotion):
    def discount(self, order):
        "7% discount on orders with at least 10 distinct items."
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        else:
            return 0
