from ecommerce.shipping import calculate_shipping

def test_calculate_shipping():
    assert calculate_shipping(0) == 0
    assert calculate_shipping(3) == 5
    assert calculate_shipping(10) == 15
