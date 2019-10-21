# Dependencies
import requests
import json

D2_URL = "https://www.bungie.net/Platform/Destiny2/Milestones/"
auth_headers = {'X-API-Key': '17165e72584647a5a29a8347262a82a3'}

def lambda_handler(event, context):
    with requests.Session() as session:
        session.headers = auth_headers
        session.get(D2_URL)

        response = session.get(D2_URL, headers=auth_headers)
        print(response.json())
        r = requests.get(D2_URL, headers=auth_headers)
        return r.json()
