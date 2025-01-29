import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
username = input("What is your username     :  ")
password = getpass("What is your password   : ")

auth_response = requests.post(auth_endpoint, json={
    'username': username, 'password': password
})

if auth_response.status_code == 200:
    token = auth_response.json()['token']

    headers = {
        "Authorization": f"Bearer {token}"
    }

    panenan_list = [
    {
        "hasil_panen": 4,
        "berat_ton": 29,
        "tanggal_panen": "2025-01-08 11:45:20"
    }
    ]


    endpoint_panenan = "http://localhost:8000/v3/panenan-create/"

    for panenan in panenan_list:
        response_panenan = requests.post(endpoint_panenan, headers=headers, json=panenan)
        print("Panenan Response:", response_panenan.status_code, response_panenan.json())

