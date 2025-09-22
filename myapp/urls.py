from django.urls import path
from myapp import views

urlpatterns = [
    path("whatsapp-webhook/", views.whatsapp_webhook, name="whatsapp_webhook"),
]
