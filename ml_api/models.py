from django.db import models
from django.core.management.base import BaseCommand
from django.conf import settings
import os
import csv


# Create your models here.
class MlHome(models.Model):
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



class MlFarm(models.Model):
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
    
    


