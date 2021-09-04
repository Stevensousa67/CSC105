import pandas as pd
import requests

# API Key: a78b003441ccebc7b8f659cd6c011709
# Use Google Maps API to find a city's coordinates
# Insert that coordinate into the program.

response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=41.6524911&lon=-70.2881124&exclude=current"
                        ",minutely,hourly,alerts&appid=a78b003441ccebc7b8f659cd6c011709&units=imperial").json()
responseData = pd.json_normalize(response, record_path="daily")
responseData = responseData[1:2]
responseData['pop'][1] * 100

print(f"Tomorrow will have a low of: {responseData['temp.min'][1]}°.")
print(f"Tomorrow will have a high of: {responseData['temp.max'][1]}°.")
print(f"Tomorrow will have a {responseData['pop'][1]}% chance of precipitation.")
msg_text = f"Tomorrow will have a low of: {responseData['temp.min'][1]}°, a high of: {responseData['temp.max'][1]}°," \
           f" and a {responseData['pop'][1]}% chance of precipitation."
