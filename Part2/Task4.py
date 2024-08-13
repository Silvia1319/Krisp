import io


# This is a library function, you can't modify it.
def stream_payments(callback_fn):
    """
    Reads payments from a payment processor and calls `callback_fn(amount)`
    for each payment.
    Returns when there is no more payments.
    """
    # Sample implementation to make the code run in coderpad.
    # Do not rely on this exact implementation.
    for i in range(10):
        callback_fn(i)


def store_payments(amount_iterator):
    """
        Iterates over the payment amounts from amount_iterator
        and stores them to a remote system.
        """
    # Sample implementation to make the code run in coderpad.
    # Do not rely on this exact implementation.
    for i in amount_iterator:
        print(i)


def process_payments_2():
    def payment_generator():
        # Use a list to capture the payments because they need to be yielded.
        payments_collected = []

        # Collector function to accept payments from stream_payments
        def collect_payment(amount):
            payments_collected.append(amount)

        # Call stream_payments with collect_payment which stores each payment into the list
        stream_payments(collect_payment)

        # Yield each collected payment one by one
        for payment in payments_collected:
            yield payment

    # Now, we can pass the generator to the store_payments function.
    store_payments(payment_generator())


process_payments_2()
