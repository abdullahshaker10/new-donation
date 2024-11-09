from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("cases/", views.CasesAPIView.as_view(), name="donation_cases"),
]
