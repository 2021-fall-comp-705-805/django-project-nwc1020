from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
#import requests, lxml.html as lh, pandas as pd,json


class AirportsConfig(AppConfig):
    name = 'flight.Airports'
    verbose_name = _("Airports")


