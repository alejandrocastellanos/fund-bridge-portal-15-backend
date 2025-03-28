from django.urls import path
from .views import DonationCreateView

urlpatterns = [
    path('donate/', DonationCreateView.as_view(), name='donate'),
]
