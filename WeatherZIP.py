# !/usr/bin/python3.6
# https://openweathermap.org/current

'''
By ZIP code
Description:
Please note if country is not specified then the search works for USA as a default.

API call:
api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}
Examples of API calls:
api.openweathermap.org/data/2.5/weather?zip=94040,us
http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={APIKEY}
'''

import json
import urllib.request



myKey = '38c4c3270131acb9c7ed9a7733812730'
zipCode = input("Enter zipcode: ")
# zipCode = '07728'
URL = "http://api.openweathermap.org/data/2.5/weather?zip=" + zipCode + ",us&APPID=" + myKey
websource = urllib.request.urlopen(URL)
data = json.loads(websource.read().decode())

Temp = round(((float(data['main']['temp'])-273.15)*1.8+32), 2)
Visi = float(data['visibility'])/1000

print("Today's weather in " + str(data['name']) + " calls for: " + str(data['weather'][0]['description']))
print("The temperature will be: " + str(Temp) + "F")
print("The humidity is: " + str(data['main']['humidity']) + "%")
print("Visibility is: " + str(Visi) + " Km")
print("The wind speed is: " + str(data['wind']['speed']) + " meters/sec")
