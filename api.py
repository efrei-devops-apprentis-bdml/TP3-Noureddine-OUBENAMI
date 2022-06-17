import flask
from flask import request
import requests
import json
import os

from pprint import pprint
app = flask.Flask(__name__)
app.config["DEBUG"] = True


# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>Simple Weather Scrapping</h1><p>This site is a prototype API for weather.</p>"

@app.route('/', methods=['GET'])
def wrap():
    lat = request.args["lat"]
    lon = request.args["lon"]
    api_key = os.environ['API_KEY']
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

    weather_data = requests.get(url).json()
    
    print("\nMétéo à latitude : " , lat ," et longitude : ", lon," : \n")

    json_str = json.dumps(weather_data)
    resp = json.loads(json_str)

    ### Affichage
    return weather_data['current']

if __name__ == "__main__":
    port=80
    app.run(host="0.0.0.0", port=port)
