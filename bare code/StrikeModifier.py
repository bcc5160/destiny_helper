# Imports
import os
import datetime
import json 
import math

# Modifiers in order of rotation
singes = ["solar", "void", "arc"]
positiveModifers = ["grenadier", "heavyweight", "stasis", "brawler"]
negativeModifiers = ["blackout", "grounded", "iron"]

def get_modifiers_today():
    current_mod = {}
    seed_date = datetime.datetime(2020, 12, 1, 12, 0)
    today_date = datetime.datetime.now()

    # test
    # test_date = datetime.datetime(2021, 1, 1, 12, 0)
    # today_date = test_date

    delta_days = abs((today_date - seed_date).days)
    delta_weeks = math.floor(delta_days/7)

    singes_index = delta_weeks % 3
    positiveModifers_index = delta_weeks % 4
    negativeModifiers_index = delta_weeks % 3 

    current_mod = {
        'singe': singes[singes_index],
        'positive_mod': positiveModifers[positiveModifers_index],
        'negative_mod': negativeModifiers[negativeModifiers_index]
    }

    return current_mod

print(get_modifiers_today())