from datetime import datetime
import requests

pixela_endpoint = "https://pixe.la/v1/users"

TOKEN = "CHANGE TOKEN"
USERNAME ="CHANGE USERNAME"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
#print(response)

pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2024, month=10, day=19).strftime("%Y%m%d")

pixel_params = {
    "date": today,
    "quantity": "15.25"
}

# response = requests.post(url=pixel_create_endpoint, json=pixel_params, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

new_pixel_params = {
    "quantity": "20"
}

# response = requests.put(url=pixel_update_endpoint, json=new_pixel_params, headers=headers)
# print(response)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

response = requests.delete(url=pixel_update_endpoint, headers=headers)
print(response)
