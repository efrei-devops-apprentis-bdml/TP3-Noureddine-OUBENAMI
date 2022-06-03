<h1 align="center"> Simple Weather Scrapping</h1>


This program is a simple weather scrapping with Python and Docker.

It use the small, more complete, Python Docker image based on Alpine Linux. 

<h2 align="center">Prerequisite</h2>
  

To launch this program, you need :
  - A latitude
  - A longitude
  - An OpenWeather API key
  - Docker
 
 <h2 align="center">How to launch it</h2>

 
 1- Download this Github project 
 2- Pull the Docker image https://hub.docker.com/r/abzer34/weather
 3- Write this script in your CLI
 > docker run --env LAT="*****" --env LONG="*****" --env API_KEY="*****" weather:0.0.4


<h3 align="center">Built with </h3>

- Python
- Docker
- OpenWeather API
