from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ValidateMyForm(Action):
    """
    This class is a custom action to validate a form that collects user details.
    It is a subclass of the `Action` class provided by the Rasa SDK.

    Methods:
    - name: Returns the name of the action.
    - run: Validates the form. If any required slots are not filled, it sets the
           "requested_slot" to the name of the unfilled slot.
    """

    def name(self) -> Text:
        """Returns the name of the action."""
        return "user_details_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
        Validates the form. If any required slots are not filled, it sets the
        "requested_slot" to the name of the unfilled slot.

        Parameters:
        - dispatcher: the dispatcher which is used to send messages back to the user.
        - tracker: the state tracker for the current user.
        - domain: the bot's current domain.

        Returns:
        A list of `SlotSet` events. If a required slot is not filled, it sets the
        "requested_slot" to the name of the unfilled slot. If all required slots are
        filled, it sets the "requested_slot" to None.
        """
        required_slots = ["name", "tel_number"]
        
        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                return [SlotSet("requested_slot", slot_name)]
            
        return [SlotSet("requested_slot", None)]


class ActionSubmit(Action):
    """
    This class is a custom action to submit the form.
    It is a subclass of the `Action` class provided by the Rasa SDK.

    Methods:
    - name: Returns the name of the action.
    - run: Submits the form. Retrieves the "utter_collect_info" response from the
           domain and formats it with the user's name and mobile number.
    """

    def name(self) -> Text:
        """Returns the name of the action."""
        return "action_submit"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
        Submits the form. Retrieves the "utter_collect_info" response from the
        domain and formats it with the user's name and mobile number.

        Parameters:
        - dispatcher: the dispatcher which is used to send messages back to the user.
        - tracker: the state tracker for the current user.
        - domain: the bot's current domain.

        Returns:
        A list of events. In this case, it's an empty list because the form submission
        doesn't result in any events.
        """
        response = domain["responses"]["utter_confirm_info"][0]

        name = tracker.get_slot("name")
        mobile_number = tracker.get_slot("number")
        email = tracker.get_slot("email")    

        response_text = response["text"].format(Name=name, Number=mobile_number, Email=email)

        dispatcher.utter_message(text =response_text)
        return []