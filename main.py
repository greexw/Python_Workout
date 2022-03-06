import requests
from datetime import datetime

TODAY = datetime.now().strftime("%Y%m%d")
USERNAME = ""
TOKEN = ""
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_POST_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"
PIXEL_UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/{TODAY}"

headers = {
    "X-USER-TOKEN": TOKEN
}

# User registration to pixe.la via password (token) and login (username)
# user_register_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# response = requests.post(url=PIXELA_ENDPOINT, json=user_register_params)

# Creating a new graph on pixe.la - in this case, for count the pages from everyday reading
# graph_config = {
#     "id": "graph1",
#     "name": "Reading Graph",
#     "unit": "pages",
#     "type": "int",
#     "color": "sora",
# }

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)

# Add new pixel for specific day
# pixel_post_params = {
#     "date": TODAY,
#     "quantity": "5",
# }

# response = requests.post(url=PIXEL_POST_ENDPOINT, json=pixel_post_params, headers=headers)

# Update pixel for specific day
pixel_update_params = {
    "quantity": "15"
}

response = requests.put(url=PIXEL_UPDATE_ENDPOINT, json=pixel_update_params, headers=headers)
