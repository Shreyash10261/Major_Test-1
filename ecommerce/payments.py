class PaymentProcessor:
    def __init__(self, gateway_url):
        self.gateway_url = gateway_url

    def process(self, amount):
        raise NotImplementedError("Base class cannot process payments")

class StripeProcessor(PaymentProcessor):
    def process(self, amount):
        if amount <= 0:
            # Complex Bug 1: Raising a generic Exception instead of a specific ValueError 
            # that the test suite is strictly expecting.
            raise Exception("Amount must be greater than zero")
        return f"Processed ${amount} via Stripe"

def execute_batch_payments(processors, amounts):
    """
    Executes a batch of payments.
    """
    results = []
    # Complex Bug 2: Modifying a list while iterating over it causes the iterator to skip elements.
    for proc in processors:
        if not amounts:
            break
        amt = amounts.pop(0)
        results.append(proc.process(amt))
        if amt > 100:
            # Removing an item from the list we are currently iterating over
            processors.remove(proc) 
    return results
