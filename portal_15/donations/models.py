import uuid
from django.db import models

class Donation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=250)
    donation_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_public = models.BooleanField(default=False)  # True = Public, False = Private
    is_approved = models.BooleanField(default=False)  # True = Public, False = Private

    def __str__(self):
        return f"{self.name} - ${self.donation_amount}"
