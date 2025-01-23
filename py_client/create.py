# import requests
# from getpass import getpass

# auth_endpoint = "http://localhost:8000/api/auth/"
# username = input("What is your username     :  ")
# password = getpass("What is your password   : ")

# auth_response = requests.post(auth_endpoint, json={
#     'username' : username, 'password' : password
# }) 

# # print(auth_response.json())

# if auth_response.status_code == 200:
    
#     token = auth_response.json()['token']
    
#     headers = {
#         "Authorization" : f"Bearer {token}"
#     }
    
#     search_endpoint = input("Search endpoint : ")

#     endpoint = f"http://localhost:8000/v3/{search_endpoint}/"

#     get_response = requests.get(endpoint, headers=headers) 
#     print(get_response.json())