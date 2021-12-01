from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
#from django.db import models




class User(AbstractUser):
    """Default user for Flight."""
    Airport = [
    ('ATL', 'Hartsfield-Jackson International Airport'),
    ('LAX', 'Los Angeles International Airport'),
    ('JFK', 'John F. Kennedy International Airport'),
    ('BOS', 'Logan International Airport'),
    ('MCO', 'Orlando International Airport'),
    ]
    defaultAirport = CharField(max_length=3, choices=Airport, default='BOS')
    first_name = None  # type: ignore
    last_name = None  # type: ignores

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


# class Amadeus(models.Model):
#     Origin = models.CharField(max_length=3)
#     Dest = models.CharField(max_length=3)
#     Startdate = models.DateField()
#     Returndate = models.DateField()

