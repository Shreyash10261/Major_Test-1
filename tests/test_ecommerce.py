import pytest
from ecommerce.orders import calculate_discount, process_order
from ecommerce.inventory import get_first_item, add_stock
from ecommerce.users import parse_age, get_user_email

class MockUser:
    def __init__(self, email):
        self.email = email

def test_calculate_discount():
    # This will crash with ZeroDivisionError because 100 - 100 = 0
    assert calculate_discount(100, 100) == 0

def test_process_order():
    # This will crash with KeyError because 'status' is missing
    assert process_order({"id": 123}) == False

def test_get_first_item():
    # This will crash with IndexError because list is empty
    assert get_first_item([]) is None

def test_add_stock():
    # This will crash with TypeError because we are adding int and str
    assert add_stock(50, "10") == 60

def test_parse_age():
    # This will crash with ValueError because "twenty" is not a number
    assert parse_age("twenty") == 20

def test_get_user_email():
    # This will crash with AttributeError because None has no .email attribute
    assert get_user_email(None) == ""
