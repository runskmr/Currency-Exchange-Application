from django.db import models

# Create your models here.
class Currencyvalue(models.Model):
    usd = models.CharField(max_length=30)
    inr = models.CharField(max_length=30)
    cad = models.CharField(max_length=30)
    usinr = models.CharField(max_length=30)