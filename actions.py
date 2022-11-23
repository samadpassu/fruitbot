# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import json
from typing import Any, Text, Dict, List
import requests

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#from rasa_sdk.events import SlotSet

class ActionWeather(Action):

    def name(self) -> Text:
         return "action_weather_form"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        get_city_slot = tracker.get_slot("city")
        url1 = requests.get(f"http://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey=OW6bredGQjuxvhkz9NxgiX2C9u64UqeL&q={get_city_slot}&language=en-us")
        data0 = url1.json()
        data_city_code = data0[0]['Key']
        url = requests.get(f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{data_city_code}?apikey=OW6bredGQjuxvhkz9NxgiX2C9u64UqeL&language=en-us&details=false&metric=false")
        data = url.json()
        data_status = data['Headline']['Text']
        data_status2 = data['Headline']['Category']
        data2 = data['DailyForecasts'][0]['Temperature']['Maximum']['Value']
        data3 = data['DailyForecasts'][0]['Day']['IconPhrase']    

        dispatcher.utter_message(f"Status: {data_status}, Condition: {data_status2}, Maximum Temperature {data2}, Day {data3}")
        return []
