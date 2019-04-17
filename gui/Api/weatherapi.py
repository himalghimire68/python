import requests

api_key="167aac9b3c2708b1894f80f12156c2d6"
base_url="https://api.openweathermap.org/data/2.5/weather?"
city_name=input("Enter City Name:: ")
complete_url= base_url + "appid=" + api_key + "&q=" + city_name

response=requests.get(complete_url)

print(response)
x=response.json()
# print(x)

temp= x['main']['temp']
cel=temp-273.15
print(cel)

speed= x['wind']['speed']
print(speed)