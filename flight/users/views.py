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
    
    def AmadeusAPICall(self):
        #if(request.GET.get('mybtn')):
        amadeus = Client(client_id= settings.AMADEUS_KEY,client_secret= settings.AMADEUS_SECRET)
        try:
            response = amadeus.shopping.flight_offers_search.get(
                originLocationCode='BOS',
                destinationLocationCode='LAX',
                departureDate='2022-01-10',
                adults = 1,
                currencyCode = "USD"
                )
            mydata = response.data
            #data is a json file that contains a lot of information about the flights, i might switch over to flight_offers_price for the purposes of my project to keep it more simple and keep
            # my json way easier to read but for now ill see if i can work with this extended dataset for the extra information it includes.
            # print(data)
            return HttpResponse(mydata)
        except ResponseError as error:
            return HttpResponse('Invalid Options please try again')
        