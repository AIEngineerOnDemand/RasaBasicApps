from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ValidateMyForm(Action):
    """Action to validate a form that collects user details."""

    def name(self) -> Text:
        """Returns the name of the action."""
        return "user_details_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
        Validates the form. If any required slots are not filled, it sets the
        "requested_slot" to the name of the unfilled slot.
        """
        required_slots = ["name", "tel_number"]
        
        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                return [SlotSet("requested_slot", slot_name)]
            
        return [SlotSet("requested_slot", None)]


class ActionSubmit(Action):
    """Action to submit the form."""

    def name(self) -> Text:
        """Returns the name of the action."""
        return "action_submit"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
        Submits the form. Retrieves the "utter_collect_info" response from the
        domain and formats it with the user's name and mobile number.
        """
        response = domain["responses"]["utter_collect_info"][0]

        name = tracker.get_slot("name")
        mobile_number = tracker.get_slot("number")

        response_text = response["text"].format(Name=name, Number=mobile_number)

        dispatcher.utter_message(text =response_text)
        return []