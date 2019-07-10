from django.db import models

# Create your models here.

class Log(models.Model):
    strategy = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    current_date = models.CharField(max_length=255, default="")
    quantity = models.CharField(max_length=255)
    entry = models.CharField(max_length=255)
    last_price = models.CharField(blank=True, max_length=255)
    buy_or_sell = models.CharField(max_length=255)
    returns = models.CharField(blank=True, max_length=255)
    equity = models.CharField(max_length=255)

class MonthlyLog(models.Model):
    strategy = models.CharField(default="", max_length=255)
    month = models.CharField(max_length=255)
    returns = models.CharField(blank=True, max_length=255)