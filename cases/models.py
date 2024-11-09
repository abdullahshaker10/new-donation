from django.db import models

class Donation(models.Model):
    name =models.CharField(max_length=100)
    details = models.TextField()