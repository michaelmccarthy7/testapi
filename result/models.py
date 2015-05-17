from django.db import models

# Create your models here.
class Result(models.Model):
    pps = models.CharField(max_length=100)
    minor_code = models.CharField(max_length=100)
    award_code = models.CharField(max_length=100)
    class_code = models.CharField(max_length=100)
    award = models.CharField(max_length=100)
