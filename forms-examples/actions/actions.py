from typing import Any, Text, Dict, List, Optional
from rasa_sdk import Tracker,Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction

class ValidateContactForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_contact_form"

    async def required_slots(
        self,
        slots_mapped_in_domain: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> Optional[List[Text]]:
        required_slots = slots_mapped_in_domain[:]
        
        if tracker.get_slot("name") is None:
            required_slots.append("name")
        if tracker.get_slot("email") is None:
            required_slots.append("email")
        if tracker.get_slot("phone") is None:
            required_slots.append("phone")

        return required_slots
    async def extract_name(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:
        text = tracker.latest_message.get("text")

        if not text:
            dispatcher.utter_message(template="utter_ask_again")
            return {"name": None}

        return {"name": text}

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
        number = tracker.get_slot("number")
        email = tracker.get_slot("email")   
        response_text = f"Hello {name}, your number is {number} and your email is {email}."
        dispatcher.utter_message(text =response_text)
        return []