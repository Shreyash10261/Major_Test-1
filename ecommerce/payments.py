class PaymentProcessor:
    def __init__(self, gateway_url):
        self.gateway_url = gateway_url

    def process(self, amount):
        raise NotImplementedError("Base class cannot process payments")

class StripeProcessor(PaymentProcessor):
    def process(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        return f"Processed ${amount} via Stripe"

def execute_batch_payments(processors, amounts):
    """
    Executes a batch of payments.
    """
    results = []
    # Iterating over a copy of processors to safely remove items from the original list
    for proc in processors[:]:
        if not amounts:
            break
        amt = amounts.pop(0)
        results.append(proc.process(amt))
        if amt > 100:
            processors.remove(proc) 
    return results
