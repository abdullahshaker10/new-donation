from django.urls import path
from . import views

app_name = "cases"
urlpatterns = [
    path("", views.CasesAPIView.as_view(), name="donation_cases"),
]
