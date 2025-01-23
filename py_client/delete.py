# ERROR

import requests

plant = input("What is the name of plant you want to delete?\n")

try:
    plant = plant
except:
    plant = None
    print(f'{plant} not a valid name of plant')

if plant:
    endpoint = f"http://localhost:8000/v3/tanaman/{plant}/"

    get_response = requests.delete(endpoint) 

    print(get_response.status_code, get_response.status_code == 204)