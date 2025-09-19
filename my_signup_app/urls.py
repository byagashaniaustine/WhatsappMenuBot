from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    
    # Include app URLs (your bot webhook, signup, etc.)
    path('', include('myapp.urls')),
]
