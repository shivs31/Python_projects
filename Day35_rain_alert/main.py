import requests

OWN_Endpoint = 'http://api.openweathermap.org/data/2.5/forecast'
api_key ="ba289d5af641fe17ece213f252c23708"

weather_parameters= {
    "lat" : 52.520008,
    "lon" : 13.404954,
    "appid": api_key,
    "cnt": 4
}


response = requests.get(url=OWN_Endpoint, params=weather_parameters)
#print(response.status_code)
response.raise_for_status()
weather_data = response.json()
# list_data = weather_data['list'][0]["weather"][0]["id"]
# print(list_data)

will_rain = False
for hour_data in weather_data['list']:
    condition_code = hour_data['weather'][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")