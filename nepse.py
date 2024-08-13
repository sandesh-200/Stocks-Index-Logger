import requests as req
import pyttsx3 as tt
import time
import json
from datetime import datetime
now = datetime.now()
# while True:
def speak_index(value):
    engine = tt.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(value)
    engine.runAndWait()
    engine.stop()



def fetch_index():
    data = (req.get('https://nepalstock.onrender.com/nepse-index')).json()
    data_list = [];
    for unit_data in data:
        if unit_data['index'] == 'NEPSE Index':
            index_data = unit_data['currentValue']
            percentage_change = unit_data['perChange']
            data_list.append((index_data,percentage_change))
    return data_list

fetch_index()

def detect_index_change():
    previous_data = None

    while True:
        current_data = fetch_index()[0][0]
        per_change = fetch_index()[0][1]
        if previous_data is not None and current_data != previous_data:
            speak_index(f"Change in Stock Index Detected by {per_change} percentage which now becomes {current_data}which means the market has been {'decreased' if current_data<previous_data else 'increased'}")
            previous_data = current_data
        else:
            speak_index(f"No changes detected Sir! Index is still {current_data}")
        time.sleep(3)

detect_index_change()






