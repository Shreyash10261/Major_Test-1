def calculate_discount(price, discount_percent):
    """Calculates discounted price. Fails with ZeroDivisionError if discount is 100."""
    return price / (100 - discount_percent)

def process_order(order):
    """Processes an order dictionary. Fails with KeyError if 'status' is missing."""
    if order['status'] == 'shipped':
        return True
    return False
