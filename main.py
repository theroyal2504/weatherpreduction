#note  it must bi internet access to run this code
#APIs key update

import requests
import json   #built in module

city = input("Enter the name of the city = ")
url = f"https://api.weatherapi.com/v1/current.json?key=aae0a9be680c488a9cf62234241705&q={city}"

#requests it is  module to connect with internet and through to weather APIs key
#its works to get data in  API url
r = requests.get(url)
#print(r.text)         r.text are sting form
#print(type(r))
dictionery = json.loads(r.text)          #json.loads fuction are convert  string function to dictionery

lastupdate = dictionery["current"]["last_updated"]
tempreture = dictionery["current"]["temp_c"]
windspeed =  dictionery["current"]["wind_kph"]
humidity = dictionery["current"]["humidity"]
location = dictionery["location"]["region"]
cunty = dictionery["location"]["country"]
localtime = dictionery["location"]["localtime"]

#print(dictionery)
#print(type(dictionery))
print(f"last update and time  = {lastupdate}")
print(f"tempreture are = {tempreture}")
print(f"wind speed in  = {windspeed}")
print(f"humidity  = {humidity}")
print(f"Rigion  =  {location}")
print(f"cuntry  = {cunty}")
print(f"local time  =  {localtime}")