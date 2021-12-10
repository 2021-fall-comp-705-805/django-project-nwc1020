from django.db import models

class Airports(models.Model):
    IATAcode = models.CharField(max_length=3,default='BOS')
    Airportname = models.CharField(max_length=255,default='Gen. Edward Lawrence Logan International Airport')

class RecentRequest(models.Model):
    flightOffer = models.IntegerField()
    indivFlightID = models.IntegerField()
    carrierCode = models.CharField(max_length=255)

