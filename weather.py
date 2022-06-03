
import requests
import json
import os
from pprint import pprint #Affichage améliorée du format JSO

def get_meteo(lat,lon,api_key):
    #utilisation de l'API OpenWeather Map
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

    weather_data = requests.get(url).json()
    
    print("\nMétéo à latitude : " , lat ," et longitude : ", lon," : \n")

    json_str = json.dumps(weather_data)
    resp = json.loads(json_str)

    ### Affichage
    print('\nLieu :')
    print('Latitude : ', resp['lat'], '  Longitude : ' ,resp['lon'], ' zone : ', resp['timezone'] )
    print('\nTempérature :')
    print (resp['current'] )
# Récupération des variables d'environnement
latitude = os.environ['LAT']
longitude = os.environ['LONG']
cle_api = os.environ['API_KEY']


get_meteo(latitude,longitude, cle_api)
