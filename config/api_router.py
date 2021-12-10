from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from flight.Airports.views import RRViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("RecentRequests", RRViewSet)


app_name = "api"
urlpatterns = router.urls
