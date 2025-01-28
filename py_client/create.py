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

    # tanaman_list = [
    #     {"owner": 1, "nama_tanaman": "padi", "jenis": "serelia", "waktu_tanam_hari": 120, "harga_perTon": 5000000, "peluang_hama": 3, "public": False}
    # ]

    # hama_list = [
    #     # {"nama_hama": "ulat", "rate_bahaya": 4, "makhluk": "HEWAN", "obat": 1}
    # ]
    
    pupes_list = [
    {
        "jenis": "PESTISIDA",
        "nama_obat": "AgroShield",
        "produsen": "AgriCo",
        "warna": "PUTIH"
    }]


    # endpoint_tanaman = "http://localhost:8000/v3/tanaman/"
    # endpoint_hama = "http://localhost:8000/v3/hama/"
    endpoint_pupes = "http://localhost:8000/v3/pestisida-pupuk/"

    for pupes in pupes_list:
        response_pupes = requests.post(endpoint_pupes, headers=headers, json=pupes)
        print("Hama Response:", response_pupes.status_code, response_pupes.json())
