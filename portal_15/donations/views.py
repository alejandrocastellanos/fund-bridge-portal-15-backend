from django.db.models import Sum
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Donation
from .serializers import DonationSerializer, LastDonationsSerializer


class DonationCreateView(APIView):
    def post(self, request):
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TotalDonationAmountView(APIView):
    def get(self, request):
        total_amount = Donation.objects.aggregate(total=Sum('donation_amount'))['total'] or 0
        return Response({"total_donation_amount": total_amount}, status=status.HTTP_200_OK)

class LastFiveDonationsView(ListAPIView):
    queryset = Donation.objects.order_by('-created_at')[:5]  # Get the last 5 donations
    serializer_class = LastDonationsSerializer
