from django.db import models


class Donation(models.Model):
    status = models.CharField(
        choices=[("INITIATED", "INITIATED"), ("PROCESSED", "PROCESSED")],
        default="INITIATED",
        max_length=200,
    )
