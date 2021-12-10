from django.http import HttpResponse
from amadeus import Client, ResponseError
from django.conf import settings
from django.template import loader
import pandas as pd

class AmadeusView():
    
    def AmadeusAPICall(dict):
        print(dict)
        amadeus = Client(client_id= settings.AMADEUS_KEY,client_secret= settings.AMADEUS_SECRET)
        try:
            if dict['returndate'] != '':
                response = amadeus.shopping.flight_offers_search.get(
                    originLocationCode=dict['Origin'],
                    destinationLocationCode=dict['Dest'],
                    departureDate=dict['startdate'],
                    returnDate=dict['returndate'],
                    adults = 1,
                    currencyCode = "USD"
                    )
            else:
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
            return('Invalid Options please try again')
    
    def AmadeusInfoGrab(request):
        if request.method == 'POST':
            myDict = request.POST.copy()
            myDict.pop('csrfmiddlewaretoken',None)
            flightdata = AmadeusView.AmadeusAPICall(myDict)
            print(type(flightdata))
            if flightdata == 'Invalid Options please try again':
                return HttpResponse(flightdata)
            mytable = AmadeusView.AmadeusPandas(flightdata)
            template = loader.get_template('pages/result.html')
            context = {'table':mytable}
            return HttpResponse(template.render(context))

    def AmadeusPandas(flightdata):
        mydf = pd.json_normalize(flightdata)
        splitdf = pd.json_normalize(
        flightdata, 
        record_path=['itineraries',['segments']],
        meta = ['numberOfBookableSeats', 'lastTicketingDate','id'],
        meta_prefix='meta-',
        errors='ignore')
        pricedf = mydf[['id','price.base','price.total']].copy()
        pricedf.rename(columns={'id':'prid'},inplace=True)
        splitdf[['departureDate','departureTime']] = splitdf['departure.at'].str.split('T',expand=True)
        splitdf[['arrivalDate','arrivalTime']] = splitdf['arrival.at'].str.split('T',expand=True)
        droppedsplit = splitdf.merge(pricedf, left_on='meta-id', right_on='prid')
        #finaldf = droppedsplit.drop(columns=['arrival.terminal', 'departure.terminal','blacklistedInEU','duration', 'operating.carrierCode','numberOfStops','departure.at','arrival.at','prid'])
        #switched to selecting the exact columns i wanted from just dropping a couple, since one query i did included a stops column that usually isnt made or wanted in my data so specifically selecting the columns i want is a better idea
        finaldf = droppedsplit[['meta-id','id','carrierCode','number','departure.iataCode','arrival.iataCode','aircraft.code','meta-numberOfBookableSeats','meta-lastTicketingDate',
        'departureDate','departureTime','arrivalDate','arrivalTime','price.base','price.total']].copy()
        finaldf['price.base']= '$'+ finaldf['price.base'].astype(str)
        finaldf['price.total']= '$'+ finaldf['price.total'].astype(str)
        finaldf.rename(columns={'meta-id':'flightOffer#', 'id':'indivFlightId', 'number':'flightNumber', 'meta-numberOfBookableSeats':'numberOfBookableSeats','meta-lastTicketingDate':'lastTicketingDate'},inplace=True)
        finaldf.set_index(['flightOffer#','indivFlightId'],inplace=True)
        finaldf['arrivalTime']= pd.to_datetime(finaldf['arrivalTime'],format='%H:%M:%S')
        finaldf['departureTime']= pd.to_datetime(finaldf['departureTime'],format='%H:%M:%S')
        finaldf['arrivalTime']=finaldf['arrivalTime'].apply(lambda x: x.strftime("%I:%M %p"))
        finaldf['departureTime']=finaldf['departureTime'].apply(lambda x: x.strftime("%I:%M %p"))
        httpfinaldf = finaldf.to_html()
        return (httpfinaldf)
