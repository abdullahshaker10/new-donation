from cases.models import Donation
from rest_framework import serializers

class DonationCasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'