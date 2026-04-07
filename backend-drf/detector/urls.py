from django.urls import path
from .views import detect_email, history, stats, check_url

urlpatterns = [
    path('detect/', detect_email),
    path('history/', history),
    path('stats/', stats),
    path('check-url/', check_url),
]