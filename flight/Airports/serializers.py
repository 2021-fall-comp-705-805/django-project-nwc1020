from .models import RecentRequest
from rest_framework import serializers

class RRSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecentRequest
        fields = ['flightOffer','indivFlightID','carrierCode','flightNum','departureAirport','arrivalAirport','aircraftCode','numOfBookableSeats','lastTicketingDate','departureDate','departureTime','arrivalDate','arrivalTime','basePrice','totalPrice']