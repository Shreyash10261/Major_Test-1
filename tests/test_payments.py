import pytest
from ecommerce.payments import PaymentProcessor, StripeProcessor, execute_batch_payments

def test_base_processor():
    proc = PaymentProcessor("http://mock.com")
    with pytest.raises(NotImplementedError):
        proc.process(50)

def test_stripe_processor_negative():
    proc = StripeProcessor("http://stripe.com")
    # This will fail because StripeProcessor raises a base Exception, not a ValueError
    with pytest.raises(ValueError):
        proc.process(-10)

def test_execute_batch_payments():
    processors = [
        StripeProcessor("url1"), 
        StripeProcessor("url2"), 
        StripeProcessor("url3")
    ]
    amounts = [150, 50, 200]
    
    results = execute_batch_payments(processors, amounts)
    
    # This will fail with an AssertionError.
    # Because execute_batch_payments removes elements during iteration, it will skip processing the second item entirely,
    # resulting in only 2 processed payments instead of 3.
    assert len(results) == 3
