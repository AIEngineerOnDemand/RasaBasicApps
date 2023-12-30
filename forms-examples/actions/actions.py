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
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[List[Text]]:
        return ["name", "email", "number"]
    
    async def extract_name(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:
        name = tracker.get_slot("name")
        return {"name": name}

    async def extract_number(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:
        number = tracker.get_slot("number")
        return {"number": number}
    
    async def extract_email(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:
        email = tracker.get_slot("email")
        return {"email": email}
 
    
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
        
       # response = domain["responses"]["utter_confirm_info"][0]
        name = tracker.get_slot("name")
        number = tracker.get_slot("number")
        email = tracker.get_slot("email")   
        response_text = f"Hello {name}, your number is {number} and your email is {email}."
        dispatcher.utter_message(text =response_text)
        return []
    
    class ActionResetForm(Action):
        def name(self) -> Text:
            return "action_reset_form"

        async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict[Text, Any]]:
            return [
                {"event": "form", "name": None},  # Deactivate the form
                {"event": "slot", "name": "name", "value": None},  # Reset the 'name' slot
                {"event": "slot", "name": "number", "value": None},  # Reset the 'number' slot
                {"event": "slot", "name": "email", "value": None},  # Reset the 'email' slot
            ]