import random
from enum import Enum

class PaymentStatuses(Enum):
    InProgress = "in-progress"
    Charged = "charged"
    Failed = "failed"
    Refunded = "refunded"
    Disputed = "disputed"

def get_payment_status(payment_intent_id: str):
    """
    Retrieves the status of the given payment intent specified by the ID.

    The possible statuses are:
    - in-progress
    - charged
    - failed
    - refunded
    - disputed
    """ 
    return random.choice(list(PaymentStatuses)).value
    