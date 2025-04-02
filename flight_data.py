import requests 
from dotenv import load_dotenv
import os 
load_dotenv()
api_key = os.getenv("api_key")
api_secret = os.getenv("api_secret")
access_token = os.getenv("access_token")
class FlightData:
    def __init__(self):
        self.url  = 'https://test.api.amadeus.com/v2/shopping/flight-offers'

    def get_offers(self,  iata):
        self.parameters = { 
            'originLocationCode' : 'LHR' ,
            'destinationLocationCode' : iata, 
            'departureDate' : '2025-04-03', 
            'adults' : 1,
            'nonStop' : 'true' , 
            'currencyCode' : 'PKR'

        }
        self.headers = {
                    "grant_type" :"client_credentials" ,
                    "client_id" : api_key,
                    "client_secret": api_secret,
                    "Authorization" : f'Bearer {access_token}'
                }
        self.data = requests.get(url = self.url , params=self.parameters , headers = self.headers)
        self.data = self.data.json()
        
        return self.data