<h1 align="center"> Simple Weather Scrapping</h1>

<!--notes--><!--/notes-->

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
 3- Write this script in your CLI and fill it with your latitude, longitude and API key value
 > docker run --env LAT="*****" --env LONG="*****" --env API_KEY="*****" weather:0.0.4


 <h2 align="center">Bonus</h2>
 
 According to the bonus part :
 - This project have 0 CVE through Trivy
 > docker run aquasec/trivy image abzer34/weather:0.0.4
 <img width="444" alt="image" src="https://user-images.githubusercontent.com/75072085/171857758-4af9588f-e32e-46c7-ba35-3164dcff6236.png">
 
 - No error was detected by Hadolint, verifiable with 
 > docker run --rm -i hadolint/hadolint < Dockerfile
 
 - No credentials are saved in the program


<h3 align="center">Built with </h3>

- Python
- Docker
- OpenWeather API
