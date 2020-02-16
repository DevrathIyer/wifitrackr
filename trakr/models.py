from django.db import models

# Create your models here.

class AP(models.Model):
    BSSID = models.CharField(max_length = 18)
    RSSI = models.IntegerField(blank=True,null=True)