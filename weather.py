
import requests
import json
from pprint import pprint

def get_meteo(lat,lon,api_key):

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


get_meteo(lat,lon, api_key)