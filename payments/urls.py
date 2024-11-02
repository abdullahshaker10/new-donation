from django.urls import path
from . import views

app_name = "payments"
urlpatterns = [
    path("checkout/", views.CheckoutView.as_view(), name="payments_checkout"),
    path("donation/<slug:id>/", views.DonationView.as_view(), name="donation_details"),
    path(
        "donation/update/<slug:id>/",
        views.DonationUpdateView.as_view(),
        name="donation_update",
    ),
]
