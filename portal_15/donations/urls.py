from django.urls import path
from .views import DonationCreateView, TotalDonationAmountView, LastFiveDonationsView

urlpatterns = [
    path('donate/', DonationCreateView.as_view(), name='donate'),
    path('total-donations/', TotalDonationAmountView.as_view(), name='total_donations'),
    path('last-donations/', LastFiveDonationsView.as_view(), name='last_donations'),
]
