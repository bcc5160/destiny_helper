# Dependencies
import datetime
import json 
# from ask_sdk_core.handler_input import HandlerInput
# from ask_sdk_core.dispatch_components import AbstractRequestHandler
# from ask_sdk_core.utils import is_request_type

EP_WEAPONS_ORDER = ['SHOTGUN', 'SMG', 'SNIPER', 'ALL', 'ALL']

def get_ep_weapon_this_week():
    seed_date = datetime.datetime(2018, 9, 25, 1, 0) # This is when I got my EP shotgun
    today = datetime.datetime.now()
  
    delta_days = abs((today - seed_date).days)
    delta_weeks = delta_days/7

    weapon_index = (delta_weeks % 5) 

    return EP_WEAPONS_ORDER[weapon_index]

def get_number_weeks_until_mainly(target_weapon_index):
    current_weapon = get_ep_weapon_this_week()
    current_weapon_index = EP_WEAPONS_ORDER.index(current_weapon)
    weeks_until = 0

    if(current_weapon == EP_WEAPONS_ORDER[target_weapon_index]):
        return 0
    
    delta_weeks = target_weapon_index - current_weapon_index
 
    if(delta_weeks < 0):
        weeks_until = len(EP_WEAPONS_ORDER) - abs(delta_weeks)
    else:
        weeks_until = delta_weeks


def lambda_handler(event, context):
    # TODO implement
    weapon_name = get_ep_weapon_this_week()
   
    return set_response_in_session(weapon_name)
    
# ---------------------- ALEXA functions -------------------------------
def welcome_response():
    pass

def set_response_in_session(weapon_name):
    alexa_response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': 'The weapon this week is the ' + weapon_name,
            }
        }
    }
    
    return alexa_response

