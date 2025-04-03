#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint
from flight_data import FlightData
from notification_manager import NotificationManager

notification  = NotificationManager()
sheet_data = DataManager()
flight_data = FlightData()

sheet = sheet_data.get_data()['prices']
print(sheet)
flight = FlightSearch()
print(len(sheet))
for i in range(len(sheet)):
     
    # print(f"To : {sheet[i]['city']}")
    iata = sheet[i]['iataCode']
    prices_sheet = sheet[i]['lowestPrice']
    # print(iata)
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
        
        # print(f"TO : {city} and price : {min(new_price)}")
        if float(price) < float(prices_sheet):
          messagebody = f"sheetprice is {prices_sheet} for on api call city {city} with price {min(new_price)}, sheet city:{sheet[i]['city']} "
          print(messagebody)
          notification.sendmessage(messagebody)