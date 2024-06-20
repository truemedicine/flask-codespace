from .get_payment_status import get_payment_status

def generate_payments():
  """
  Create new test payment objects

  Payments have the following shape: 

  class Payment:
    id: str
    amount_cents: int
    user_id: str
    payment_method_id: str
  """
  payments = []
  for i in range(0, 10):
      pi_id = f"pi_some_random_id_{i}"
      user_id = f"user_random_id_{i}"
      payment_method_id = f"pm_id_{i}"
      status = get_payment_status(pi_id)
      payments.append({ 
         "id": 1, 
         "intent_id": pi_id, 
         "status": status,
         "user_id": user_id,
         "payment_method_id": payment_method_id
      })
  return payments
