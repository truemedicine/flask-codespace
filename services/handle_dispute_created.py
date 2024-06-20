

def handle_dispute_created():
  """
  Webhook handler used to persist new dispute objects to the DB as they 
  are created. This handler is invoked by our payment gateway. 
  """
  print("New dispute created!")
  pass
