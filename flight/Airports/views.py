from django.http import HttpResponse
from amadeus import Client, ResponseError
from django.conf import settings
from django.template import loader
import pandas as pd,lxml.html as lh,requests,numpy as np
from .models import Airports, RecentRequest
from sqlalchemy import create_engine
from rest_framework import viewsets, permissions
from .serializers import RRSerializer

class RRViewSet(viewsets.ModelViewSet):
    queryset = RecentRequest.objects.all()
    serializer_class = RRSerializer
    permission_classes = [permissions.IsAuthenticated]


def Airport_DB_Return():
    return [(x.IATAcode,x.Airportname) for x in Airports.objects.all()]
    

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
        #finaldf['price.base']= '$'+ finaldf['price.base'].astype(str)
        #finaldf['price.total']= '$'+ finaldf['price.total'].astype(str)
        finaldf.rename(columns={'meta-id':'flightOffer', 'id':'indivFlightID', 'number':'flightNum', 
        'meta-numberOfBookableSeats':'numOfBookableSeats','meta-lastTicketingDate':'lastTicketingDate',
        'price.base':'basePrice','price.total':'totalPrice','departure.iataCode':'departureAirport',
        'arrival.iataCode': 'arrivalAirport', 'aircraft.code':'aircraftCode'
         },inplace=True)
        finaldf.set_index(['flightOffer','indivFlightID'],inplace=True)
        finaldf['arrivalTime']= pd.to_datetime(finaldf['arrivalTime'],format='%H:%M:%S')
        finaldf['departureTime']= pd.to_datetime(finaldf['departureTime'],format='%H:%M:%S')
        finaldf['arrivalTime']=finaldf['arrivalTime'].apply(lambda x: x.strftime("%I:%M %p"))
        finaldf['departureTime']=finaldf['departureTime'].apply(lambda x: x.strftime("%I:%M %p"))
        finaldf['carrierCode']=finaldf['carrierCode'].map(AmadeusView.quickAirlineDict())


        engine = create_engine('postgresql:///flight')
        finaldf.to_sql(RecentRequest._meta.db_table, if_exists='replace', con = engine,index = True)
        httpfinaldf = finaldf.to_html()
        return (httpfinaldf)
    
    def quickAirlineDict():
        url='http://en.wikipedia.org/wiki/List_of_airline_codes#'
        page = requests.get(url)
        doc = lh.fromstring(page.content)
        tr_elements = doc.xpath('//tr')
        col=[]
        i=0
        for t in tr_elements[0]:
            i+=1
            name=t.text_content()
            col.append((name,[]))
        for j in range(1,len(tr_elements)):
            T=tr_elements[j]
            i=0
            for t in T.iterchildren():
                data=t.text_content() 
                if i>0:
                    try:
                        data=int(data)
                    except:
                        pass
                col[i][1].append(data)
                i+=1
        [col.pop() for (title,C) in col]
        Dict={title:column for (title,column) in col}
        df=pd.DataFrame(Dict)
        df.rename(columns={'IATA\n': 'IATA', 'Airline\n': 'Airline'}, inplace=True)
        df['IATA']= df['IATA'].str.strip()
        df['Airline']=df['Airline'].str.replace('\n','')
        dfnew = df[['IATA','Airline']].copy()
        dfnew.replace('',np.nan, inplace=True)
        dfnew.dropna(inplace=True)
        dfnew.set_index(['IATA'],inplace=True)
        return dfnew.to_dict()['Airline']