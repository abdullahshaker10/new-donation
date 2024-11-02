from django.http import HttpResponse
from django.views.generic import View

from users.tasks import make_report


class ReportView(View):
    def get(self, request, *args, **kwargs):
        # search for the most poor person that needs my donation
        make_report.delay()  # Call the task asynchronously
        return HttpResponse("Report")
