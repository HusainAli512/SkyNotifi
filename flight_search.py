import requests 
from dotenv import load_dotenv
import os 
load_dotenv()
api_key = os.getenv("api_key")
api_secret = os.getenv("api_secret")
access_token = os.getenv("access_token")
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
        def __init__(self ):
        
            self.url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"


        def get_destination(self,city ):
                self.parameters = {
                'keyword' : city,
                'max' : 2,
                "include": "AIRPORTS"
            }

                self.headers = {
                    "grant_type" :"client_credentials" ,
                    "client_id" : api_key,
                    "client_secret": api_secret,
                    "Authorization" : f'Bearer {access_token}'
                }
                self.flight = requests.get(url = self.url ,headers = self.headers ,params= self.parameters )
                self.flight = self.flight.json()
                self.flight = self.flight['data'][0]['iataCode']
                return self.flight