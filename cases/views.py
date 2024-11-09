
from cases.models import Donation
from cases.serializers import DonationCasesSerializer
from rest_framework.generics import ListAPIView
from django.core.cache import cache

class CasesAPIView(ListAPIView):

    queryset = Donation.objects.all()
    serializer_class = DonationCasesSerializer
    def get_queryset(self):
        cache_key = 'all_cases'
        cases = cache.get(cache_key)
        if not cases:
            cases = Donation.objects.all()
            cache.set(cache_key, cases, timeout=60*60*24)  # Cache for 24 hours
        return cases