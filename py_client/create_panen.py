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
        "hasil_panen": 1,
        "berat_ton": 10,
        "tanggal_panen": "2025-01-28 10:45:20"
    },
    {
        "hasil_panen": 2,
        "berat_ton": 12,
        "tanggal_panen": "2025-01-27 09:15:30"
    },
    {
        "hasil_panen": 3,
        "berat_ton": 15,
        "tanggal_panen": "2025-01-26 11:30:45"
    },
    {
        "hasil_panen": 4,
        "berat_ton": 20,
        "tanggal_panen": "2025-01-25 08:20:10"
    },
    {
        "hasil_panen": 5,
        "berat_ton": 18,
        "tanggal_panen": "2025-01-24 14:35:50"
    },
    {
        "hasil_panen": 6,
        "berat_ton": 22,
        "tanggal_panen": "2025-01-23 07:45:20"
    },
    {
        "hasil_panen": 7,
        "berat_ton": 25,
        "tanggal_panen": "2025-01-22 10:15:35"
    },
    {
        "hasil_panen": 8,
        "berat_ton": 27,
        "tanggal_panen": "2025-01-21 13:55:10"
    },
    {
        "hasil_panen": 9,
        "berat_ton": 30,
        "tanggal_panen": "2025-01-20 12:10:15"
    },
    {
        "hasil_panen": 10,
        "berat_ton": 33,
        "tanggal_panen": "2025-01-19 09:40:50"
    },
    {
        "hasil_panen": 11,
        "berat_ton": 35,
        "tanggal_panen": "2025-01-18 15:20:10"
    },
    {
        "hasil_panen": 12,
        "berat_ton": 40,
        "tanggal_panen": "2025-01-17 11:30:45"
    },
    {
        "hasil_panen": 13,
        "berat_ton": 45,
        "tanggal_panen": "2025-01-16 14:50:20"
    }
    ]


    

    endpoint_panenan = "http://localhost:8000/v3/panenan-create/"

    for panenan in panenan_list:
        response_panenan = requests.post(endpoint_panenan, headers=headers, json=panenan)
        print("Panenan Response:", response_panenan.status_code, response_panenan.json())

