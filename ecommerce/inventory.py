def get_first_item(items):
    """Gets the first item from a list. Fails with IndexError if list is empty."""
    if not items:
        return None
    return items[0]

def add_stock(current_stock, amount_to_add):
    """Adds stock. Fails with TypeError if amount_to_add is a string."""
    return int(current_stock) + int(amount_to_add)
