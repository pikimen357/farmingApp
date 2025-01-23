import requests

search_endpoint = input("Search endpoint: ")

endpoint = f"http://localhost:8000/v3/{search_endpoint}/"


get_response = requests.get(endpoint)

data_json = get_response.json()

if isinstance(data_json, list):
    for data in data_json:
        print('=================')
        if isinstance(data, dict):
            for key, value in data.items():
                print(f"{key}:  {value}")
        
else:
    print("Response is not a list")

# print(get_response.json())