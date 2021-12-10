from django.db import models

class Airports(models.Model):
    IATAcode = models.CharField(max_length=3,default='BOS')
    Airportname = models.CharField(max_length=255,default='Gen. Edward Lawrence Logan International Airport')

class RecentRequest(models.Model):
    flightOffer = models.IntegerField(default=None)
    indivFlightID = models.IntegerField(default=None,primary_key=True)
    carrierCode = models.CharField(max_length=255,default=None)
    flightNum = models.IntegerField(default=None)
    departureAirport = models.CharField(max_length=3,default=None)
    arrivalAirport = models.CharField(max_length=3,default=None)
    aircraftCode = models.CharField(max_length=3,default=None)
    numOfBookableSeats = models.IntegerField(default=None)
    lastTicketingDate = models.DateTimeField(default=None)
    departureDate = models.DateTimeField(default=None)
    departureTime = models.TimeField(default=None)
    arrivalDate = models.DateTimeField(default=None)
    arrivalTime = models.TimeField(default=None)
    basePrice = models.FloatField(default=None)
    totalPrice = models.FloatField(default=None)
    # class Meta:
    #     indexes: models.Index(fields=['flightOffer','indivFlightID'])
