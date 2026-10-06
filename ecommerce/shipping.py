def calculate_shipping(weight):
    """Calculates shipping cost based on weight."""
    if weight <= 0:
        return 0
    elif weight < 5:
        return 5
    return 15
