import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
username = input("What is your username?\n")
password = getpass("What is your password?\n")

auth_response = requests.post(auth_endpoint, json={
    'username' : username, 'password' : password
}) 

# print(auth_response.json())

if auth_response.status_code == 200:
    
    token = auth_response.json()['token']
    
    headers = {
        "Authorization" : f"Bearer {token}"
    }
    
    nama_panenan = input("Tanaman panen : ")

    endpoint = f"http://localhost:8000/v3/panenan/{nama_panenan}/"

    get_response = requests.get(endpoint, headers=headers, params={"petani_nama" : username}) 
    print(get_response.json())