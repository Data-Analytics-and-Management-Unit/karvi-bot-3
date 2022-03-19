# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

import datetime
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionGetTime(Action):

    def name(self) -> Text:
        return "action_get_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"{datetime.datetime.now()}")

        return []

class ActionIsSmartCity(Action):

    def name(self) -> Text:
        self.city_names = [
            "bhubaneswar",
            "pune",
            "jaipur",
            "surat",
            "kochi",
            "ahmedabad",
            "jabalpur",
            "visakhapatnam",
            "solapur",
            "davangere",
            "indore",
            "new delhi",
            "coimbatore",
            "kakinada",
            "belagaavi",
            "udaipur",
            "guwahati",
            "chennai",
            "ludhiana",
            "bhopal",
            "lucknow",
            "bhagalpur",
            "faridabad",
            "chandigarh",
            "raipur",
            "ranchi",
            "dharamasala",
            "warangal",
            "panaji",
            "agartala",
            "imphal",
            "port blair",
            "new town kolkata",
            "amritsar",
            "kalyan",
            "ujjain",
            "tirupati",
            "nagpur",
            "mangalore",
            "vellore",
            "thane",
            "gwalior",
            "agra",
            "nashik",
            "rourkela",
            "kanpur",
            "madurai",
            "tumakuru",
            "kota",
            "thanjavur",
            "namchi",
            "jalandhar",
            "shimoga",
            "salem",
            "ajmer",
            "varanasi",
            "kohima",
            "hubli-dharwad",
            "aurangabad",
            "vadodara",
            "thiruvananthapuram",
            "naya raipur",
            "rajkot",
            "amravati",
            "patna",
            "karimnagar",
            "muzaffarpur",
            "puducherry",
            "gandhinagar",
            "srinagar",
            "sagar",
            "karnal",
            "satna",
            "bangalore",
            "shimla",
            "dehradun",
            "jhansi",
            "pimpri chinchwad",
            "bilaspur",
            "pasighat",
            "jammu",
            "dahod",
            "thoothukudi",
            "tiruchirappalli",
            "tirunelveli",
            "tiruppur",
            "aizawl",
            "prayagraj",
            "aligarh",
            "gangtok",
            "erode",
            "saharanpur",
            "moradabad",
            "bareilly",
            "itanagar",
            "silvassa",
            "diu",
            "kavaratti",
            "bihar sharif",
            "shillong"
        ]
        return "action_is_smart_city"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entities_list = tracker.latest_message["entities"]
        is_sm = False
        city_name = 'this'
        for e in entities_list:
            print(e)
            c = e['value'].lower()
            if c in ['city', 'cities', 'smart', 'this', 'part', 'mission']:
                continue
            if c in self.city_names:
                is_sm = True
                city_name = c
                break
            else:
                city_name = c
        
        if is_sm:
            dispatcher.utter_message(text=f"Yes, {city_name} is a smart city under India Smart Cities Mission.")
        else:
            dispatcher.utter_message(text=f"No, {city_name} is not a smart city under India Smart Cities Mission.")

        return []
