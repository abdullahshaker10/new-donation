from django.http import HttpResponse
from django.views.generic import View

from payments.models import Donation


class CheckoutView(View):
    def get(self, request, *args, **kwargs):
        donation = Donation.objects.create()
        return HttpResponse(f"Donation Initiated {donation.id}")


class DonationView(View):
    def get(self, request, id, *args, **kwargs):
        donation = Donation.objects.get(id=id)
        return HttpResponse(f"Donation status is {donation.status}")


class DonationUpdateView(View):
    def get(self, request, id, *args, **kwargs):
        Donation.objects.filter(id=id).update(status="PROCESSED")
        donation = Donation.objects.get(id=id)
        return HttpResponse(f"Donation status is {donation.status}")
