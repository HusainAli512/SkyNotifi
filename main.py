#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from flight_data import FlightData
sheet_data = DataManager()
flight_data = FlightData()

sheet = sheet_data.get_data()['prices']

flight = FlightSearch()
print(len(sheet))
for i in range(len(sheet)):
     
    print(f"From : {sheet[i]['city']}")
    iata = sheet[i]['iataCode']
    print(iata)
    if sheet[i]['iataCode'] == '':
            pass
    else:    
        # iata =flight.get_destination(sheet[i]['city'])
        new_price= []
        flight_offers = flight_data.get_offers(iata)
        for j in range(len(flight_offers['data'])):
            city =   flight_offers['data'][j]['itineraries'][0]['segments'][0]['arrival']['iataCode']
            price =  flight_offers['data'][j]['price']['total']
            
            new_price.append(float(price))
        if not new_price:
                 continue
        
        print(f"TO : {city} and price : {min(new_price)}")