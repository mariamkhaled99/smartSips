from django.db import models
from django.core.management.base import BaseCommand
from django.conf import settings
import os
import csv
from django.utils import timezone
from user_api.models import Device


# Create your models here.
class MlHome(models.Model):
    temp=models.FloatField()
    tds=models.FloatField()
    pH=models.FloatField()
    sodium=models.FloatField()
    magnesium=models.FloatField()
    calcium=models.FloatField()
    chloride=models.FloatField()
    potassium=models.FloatField()
    carbonate=models.FloatField()
    sulphate=models.FloatField()
    eC=models.IntegerField()
    tH=models.IntegerField()
    wQI=models.FloatField()
    Potability=models.BooleanField()
    date = models.DateTimeField(default=timezone.now)
    device_home=models.ForeignKey(Device, on_delete=models.CASCADE)



class MlFarm(models.Model):
    temp=models.FloatField()
    tds=models.FloatField()
    rSC=models.FloatField()
    pI=models.FloatField()
    kr=models.FloatField()
    mH=models.FloatField()
    na=models.FloatField()
    sAR=models.FloatField()
    sSP=models.FloatField()
    eC=models.IntegerField()
    iWQI=models.IntegerField()
    USABLE= models.BooleanField()
    date = models.DateTimeField(default=timezone.now)
    device_home=models.ForeignKey(Device, on_delete=models.CASCADE)
    
    


