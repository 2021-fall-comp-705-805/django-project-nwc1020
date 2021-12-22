from django.contrib.auth.models import AbstractUser
#from django.db.models import CharField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import json





class User(AbstractUser):
    """Default user for Flight."""
    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
    
    with open('airportcodes.txt','r') as f:
        lines = f.read()
    test = json.loads(lines)
    Airport = list(test.items())
    defaultAirport = models.CharField(max_length=3, choices=Airport,default='BOS')
    first_name = None  # type: ignore
    last_name = None  # type: ignores



