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


# Note: No abstract class

# Concrete strategies
def fidelity_promo(order):
    """5% discount for customers with 1000 or more fidelity points."""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """10% discount for line orders with 20 or more units."""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def large_order_promo(order):
    "7% discount on orders with at least 10 distinct items."
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10 :
        return order.total() * .07
    else:
        return 0
