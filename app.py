from flask import Flask, render_template
from services.generate_payments import generate_payments
import json

app = Flask(__name__)

"""
Build an internal API backing a merchant dashboard for viewing payments, initiating refunds, etc...


Features:
- Load payments in a table
- View details of a single payment including all info on the object, refunds, and disputes.
- Create refund for single payment (full or partial refund)
- Accept dispute simply sends a request to the gateway which will return a 2xx status code indicating success
- Submit evidence for dispute. Submitting evidence requires submitting PDF of documentation and a string containing the reason the merchant believes the payment was valid.


Assumptions:
- Total count of payments in the system is expected to exceed 1M. Payments will be in various states - in-progress, charged, failed, refunded, or disputed.
- Dashboard is used by finance & support teams consisting of ~1,000 people.


Data Model:

class Payment:
  id: str
  amount_cents: int
  user_id: str
  payment_method_id: str
  external_payment_id: str

class Dispute:
  id: str
  reason: "general" | "fraudulent" | "duplicate" | "unrecognized" | "bank_cannot_process" 
  status: "lost" | "needs_response" | "won" | "under_review"
  payment_id: str
  external_dispute_id: str

class DisputeEvidence:
  id: str
  dispute_id: str
  text: str
  # TODO - extend to support files for evidence

class Refund:
  id: str
  amount_cents: int
  payment_id: str
  reason: Optional[str]
  external_refund_id: str
"""

# Dummy payments generated at app start
payments = generate_payments()

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/payments", methods=['GET'])
def list_payments():
    """
    TODO: List all payments
    """
    return json.dumps([])

@app.route("/payments/<payment_id>", methods=['GET'])
def get_payment(payment_id):
    """
    TODO: Retrieve single payment by ID
    """
    pass

@app.route("/refunds/<payment_id>", methods=['GET'])
def get_refunds_for_payment(payment_id):
    pass

@app.route("/refunds", methods=['POST'])
def get_refunds():
    pass

@app.route("/disputes", methods=['GET'])
def get_disputes():
    pass

@app.route("/disputes/<dispute_id>/accept", methods=['POST'])
def accept_dispute():
    pass

@app.route("/disputes/<dispute_id>/submit_evidence", methods=['POST'])
def submit_evidence():
    pass