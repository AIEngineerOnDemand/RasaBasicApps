from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ValidateMyForm(Action):

    def name(self) -> Text:
        return "user_details_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        required_slots = ["name", "tel_number"]
        
        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]
            
            return [SlotSet("requested_slot", None)]


class ActionSubmit(Action):
    
    def name(self) -> Text:
        return "action_submit"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = domain['responses']["utter_collect_info"][0]
        
        name - tracker.get_slot("name")
        tel_number = tracker.get_slot("tel_number")
        
        response_text = response["text"].format(name=name, tel_number=tel_number)
        
        dispatcher.utter_message(response_text)
        
        return []
         
    