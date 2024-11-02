from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("reports/", views.ReportView.as_view(), name="users_reports"),
]
