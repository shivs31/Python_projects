import requests
from datetime import datetime

USERNAME = "your_username"
TOKEN = "your_token"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params={
    "token":TOKEN,
    "username": USERNAME, #works only once when you requested data for the first time
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response=requests.post(url=pixela_endpoint, json=user_params)
#To check response value
# print(response.text)


#creating a html page for app
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "commit",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)


#posting a pixel

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime()

pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity": "9.74"
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)