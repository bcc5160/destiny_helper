# Dependencies
import datetime

EP_WEAPONS_ORDER = ['SHOTGUN', 'SMG', 'SNIPER', 'ALL', 'ALL']

def get_ep_weapon_this_week():
    seed_date = datetime.datetime(2018, 9, 25, 1, 0)
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

    return weeks_until

TARGET = 0
print("The EP weapon this week is the " + get_ep_weapon_this_week())
print(str(get_number_weeks_until_mainly(TARGET)) + " weeks until the EP boss only drops " + EP_WEAPONS_ORDER[TARGET] + "s")
