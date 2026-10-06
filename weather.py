import os
import sys
import requests

if len(sys.argv) > 2:
    sys.exit("Too many arguments. Please provide only the city name.")
if len(sys.argv) < 2:
    sys.exit("Please provide a city name as an argument.")

city = sys.argv[1]
API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not API_KEY:
    sys.exit("Please set the OPENWEATHER_API_KEY environment variable.")
# https://api.openweathermap.org/data/2.5/weather?q=PLACE_NAME&appid=YOUR_API_KEY&units=metric

responce = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
weather_data = responce.json()

print(weather_data)