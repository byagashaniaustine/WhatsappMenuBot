import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

if not ACCOUNT_SID or not AUTH_TOKEN or not TWILIO_WHATSAPP_NUMBER:
    raise ValueError(
        "Twilio credentials are missing. Please set TWILIO_ACCOUNT_SID, "
        "TWILIO_AUTH_TOKEN, and TWILIO_WHATSAPP_NUMBER in your .env file."
    )

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_whatsapp_message(to: str, body: str) -> str:
    """
    Send a WhatsApp message using Twilio.
    Raises ValueError if `to` does not start with 'whatsapp:'.
    Returns message SID (string).
    """
    if not to.startswith("whatsapp:"):
        raise ValueError("Recipient number must start with 'whatsapp:'")

    message = client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        body=body,
        to=to
    )
    assert message.sid is not None, "Twilio did not return a SID"  # helps Pylance
    return message.sid
