from rest_framework import serializers
from .models import Donation


class DonationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donation
        fields = '__all__'


class LastDonationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donation
        fields = ['name', 'donation_amount', 'created_at']
