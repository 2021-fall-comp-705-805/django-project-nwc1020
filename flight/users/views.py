from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
#from flight.users.models import Amadeus
from django.http import HttpResponse, request
from amadeus import Client, ResponseError
from django.conf import settings

User = get_user_model()
#AmadeusModel = Amadeus()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = ["defaultAirport"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        return self.request.user.get_absolute_url()  # type: ignore [union-attr]

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()

class AmadeusView():
    
    def AmadeusAPICall(dict):
        amadeus = Client(client_id= settings.AMADEUS_KEY,client_secret= settings.AMADEUS_SECRET)
        try:
            response = amadeus.shopping.flight_offers_search.get(
                originLocationCode=dict['Origin'],
                destinationLocationCode=dict['Dest'],
                departureDate=dict['startdate'],
                adults = 1,
                currencyCode = "USD"
                )
            mydata = response.data
            return(mydata)
        except ResponseError as error:
            return HttpResponse('Invalid Options please try again')
    
    def AmadeusPresent(request):
        if request.method == 'POST':
            myDict = request.POST.copy()
            myDict.pop('csrfmiddlewaretoken',None)
            test = AmadeusView.AmadeusAPICall(myDict)
            return HttpResponse(test)


