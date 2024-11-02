from celery import shared_task


@shared_task
def make_report():
    return "report is done"
