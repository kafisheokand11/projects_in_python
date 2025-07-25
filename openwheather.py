import json 
import requests
city=input("enter the city name:")
sc=input("enter the sc name:")
cc=input("enter the cc name:")
url="http://api.openweathermap.org/geo/1.0/direct?q={},{},{}&limit=10&appid=648a165bcef4a847f468e06a213eb0b6".format(city,sc,cc)
 
complete_url=url+"appid"+"&q"+city
response=requests.get(url)
x=response.json()
# print(response)
# print(x)
r1=x[0]["lat"]
# print(r1)
r2=x[0]["lon"]
url1="https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=648a165bcef4a847f468e06a213eb0b6".format(r1,r2)
complete_url1=url1+"appid"+"&q"+city
response=requests.get(url1)
x1=response.json()
tempr=x1["main"]["temp"]
print(tempr)
print(response)
print(x1)