import requests
from datetime import datetime

MY_LAT = 52.520008
MY_LONG = 13.404954
CLOCK_FORMAT = 0 #12hour format time

# #ISS location
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)
# print(iss_position)


#SUNRISE and SUNSET TIMES

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": CLOCK_FORMAT
}

response =requests.get(url ="https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
# #to get the hour from the 24hr clock
# print(sunrise.split("T")[1].split(":")[0])

time_now = datetime.now()

print(time_now)
