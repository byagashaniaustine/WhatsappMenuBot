# myapp/twilio.py

import os
from typing import cast
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Twilio credentials
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID") or ""
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN") or ""
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER") or ""

# Validate environment variables
if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER]):
    raise EnvironmentError(
        "Twilio credentials are missing. "
        "Please set TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and TWILIO_PHONE_NUMBER in .env"
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
    # Cast to str for Pylance type checking
    return cast(str, message.sid)
