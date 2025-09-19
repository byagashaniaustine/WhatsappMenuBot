from django.urls import path
from .views import whatsapp_webhook

urlpatterns = [
    # This is the webhook URL Twilio will POST messages to
    path('whatsapp-webhook/', whatsapp_webhook, name='whatsapp_webhook'),
]
