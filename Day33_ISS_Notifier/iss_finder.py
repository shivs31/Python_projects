import requests
from datetime import datetime

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

# To get the ISS location at +5 or -5 degrees 
def is_iss_overhead():
    response = requests.get(url=ISS_link)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT + 5 and MY_LONG -5 <= iss_longitude <= MY_LONG+5:
        return True


#To check its dark
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(ur_api_link, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now >= sunset or time_now <= sunrise:
        return True


if is_iss_overhead() and is_night():
    print("The ISS is above you in the sky")


