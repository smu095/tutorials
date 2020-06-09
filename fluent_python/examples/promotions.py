"""Functions gathering promotional discounts."""


def fidelity_promo(order):
    """5% discount for customers with 1000 or more fidelity points."""
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """10% discount for line orders with 20 or more units."""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


def large_order_promo(order):
    "7% discount on orders with at least 10 distinct items."
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    else:
        return 0
