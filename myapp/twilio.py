# myapp/twilio.py
import os
from typing import cast
from twilio.rest import Client

# Read from environment (Railway will inject these at runtime)
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")

# Validate environment variables
missing = [k for k, v in {
    "TWILIO_ACCOUNT_SID": TWILIO_ACCOUNT_SID,
    "TWILIO_AUTH_TOKEN": TWILIO_AUTH_TOKEN,
    "TWILIO_PHONE_NUMBER": TWILIO_PHONE_NUMBER,
}.items() if not v]

if missing:
    raise EnvironmentError(
        f"Twilio credentials missing: {', '.join(missing)}. "
        f"Ensure they are set as Railway environment variables."
    )

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(to: str, body: str) -> str:
    """
    Send a WhatsApp message using Twilio.

    :param to: WhatsApp number of recipient (format: whatsapp:+255XXXXXXXXX)
    :param body: Message text
    :return: Twilio message SID (str)
    """
    message = client.messages.create(
        from_=TWILIO_PHONE_NUMBER,
        body=body,
        to=to
    )
    return cast(str, message.sid)
