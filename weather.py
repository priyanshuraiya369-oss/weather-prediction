import os
import sys
import requests
import json

if len(sys.argv) > 2:
    sys.exit("Too many arguments. Please provide only the city name.")
if len(sys.argv) < 2:
    sys.exit("Please provide a city name as an argument.")


city = sys.argv[1].strip().capitalize()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not API_KEY:
    sys.exit("Please set the OPENWEATHER_API_KEY environment variable.")
# https://api.openweathermap.org/data/2.5/weather?q=PLACE_NAME&appid=YOUR_API_KEY&units=metric

responce = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
weather_data = responce.json()

print(f"Weather information for {city}:")
print("\nSky conditions:", weather_data["weather"][0]["description"])
print("Temperature:", weather_data["main"]["temp"], "°C")
print("Feels like:", weather_data["main"]["feels_like"], "°C")
print("Humidity:", weather_data["main"]["humidity"], "%")
print("Wind speed:", weather_data["wind"]["speed"], "m/s")
print("Pressure:", weather_data["main"]["pressure"], "hPa")
print("Visibility:", weather_data.get("visibility", "N/A"), "meters")
print("Cloudiness:", weather_data["clouds"]["all"], "%")
print("Sunrise:", weather_data["sys"]["sunrise"])
print("Sunset:", weather_data["sys"]["sunset"])
print("Timezone:", weather_data["timezone"], "seconds from UTC")