# Dependencies
import requests
import json

D2_URL = "https://www.bungie.net/Platform/Destiny2/Milestones/"
auth_headers = {'X-API-Key': '17165e72584647a5a29a8347262a82a3'}

def load_json(file):
    with open(file) as f:
        data = json.load(f)
    
        return data

def get_milestones():
    with requests.Session() as session:
        session.headers = auth_headers
        session.get(D2_URL)

        response = session.get(D2_URL, headers=auth_headers)
        print(response.json())
        r = requests.get(D2_URL, headers=auth_headers)
        return r.json()

def lambda_handler(event, context):
    LEVIATHAN_ACTIVITY_HASH = "3660836525"
    milestones = get_milestones()
    
    if(milestones != None):
        normal_leviathan_hash = milestones["Response"][LEVIATHAN_ACTIVITY_HASH]["availableQuests"][0]["activity"]["variants"][0]["activityHash"]
        leviathan_dictionary = load_json("lev_raid.json")
        
        this_weeks_order = leviathan_dictionary[str(normal_leviathan_hash)]["order"] 
        response = "The order for the Leviathan Raid this week is, first " + this_weeks_order[0] + ", second " + this_weeks_order[1] + ", third " + this_weeks_order[2] + " then Calus." 
        
        return set_response_in_session(response)
# ---------------------- ALEXA functions -------------------------------
def welcome_response():
    pass

def set_response_in_session(input_string):
    alexa_response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': input_string,
            }
        }
    }
    
    return alexa_response


