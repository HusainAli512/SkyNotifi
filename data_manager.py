import requests
import requests
import json





class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self ):
        self.url = "https://api.sheety.co/c8b475b706e44731a010a5b83336d09a/copyOfFlightDeals/prices"

    def get_data(self):
        self.data = requests.get(url = self.url)
        self.data = self.data.json()
        self.data = self.data
        return self.data

    def put_data(self , data  ,id):
        self.url  = f'https://api.sheety.co/c8b475b706e44731a010a5b83336d09a/copyOfFlightDeals/prices/{id}'
        
         
        self.body = {
            'price':{
                'iataCode': data
                

                
            }


        }
        self.headers = {
            "Content-Type": "application/json"
        }
        self.response = requests.put(url = self.url, headers=self.headers, json=self.body)
        print(self.response.json())