from typing import Any, Text, Dict, List, Optional
from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import SlotSet,FollowupAction
from rasa_sdk.interfaces import EventType
from rasa_sdk.types import DomainDict

class ActionConfirmfirst_name(Action):
    def name(self) -> Text:
        return "action_confirm_first_name"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        intent = tracker.get_intent_of_latest_message()
        if intent == "affirm":
            return [SlotSet("first_name", tracker.get_slot("confirm_first_name")), SlotSet("confirm_first_name", None)]
        elif intent == "deny":
            return [SlotSet("confirm_first_name", None), FollowupAction("contact_form")]


class ValidateContactForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_contact_form"
    async def deactivate(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Okay, we have cancelled the form.")
        return await super().deactivate(dispatcher, tracker, domain)
    async def required_slots(
        self,
        slots_mapped_in_domain: List[Text],
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Optional[List[Text]]:
        return ["first_name", "email", "number"]
    async def extract_first_name(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:
        text_of_last_user_message = tracker.latest_message.get("text")
        intent = tracker.latest_message['intent'].get('name')
        if intent == "inform":
            return  {"first_name": None , "confirm_first_name": text_of_last_user_message}
        else:
            return {"first_name": None, "confirm_first_name": None}
    async def validate_first_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        text_of_last_user_message = tracker.latest_message.get("text")
        intent = tracker.latest_message['intent'].get('name')       
        if intent == "inform" and slot_value is None:
            dispatcher.utter_message(text=f"Your first_name is {text_of_last_user_message}?")
            return {"first_name": None, "confirm_first_name": text_of_last_user_message}
        else:
            return {"first_name": None, "confirm_first_name": None}

  
  
    
class ActionSubmit(Action):
    """
    This class is a custom action to submit the form.
    It is a subclass of the `Action` class provided by the Rasa SDK.

    Methods:
    - first_name: Returns the first_name of the action.
    - run: Submits the form. Retrieves the "utter_collect_info" response from the
           domain and formats it with the user's first_name and mobile number.
    """

    def name(self) -> Text:
        """Returns the first_name of the action."""
        return "action_submit"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
        Submits the form. Retrieves the "utter_collect_info" response from the
        domain and formats it with the user's first_name and mobile number.

        Parameters:
        - dispatcher: the dispatcher which is used to send messages back to the user.
        - tracker: the state tracker for the current user.
        - domain: the bot's current domain.

        Returns:
        A list of events. In this case, it's an empty list because the form submission
        doesn't result in any events.
        """
        
       # response = domain["responses"]["utter_confirm_info"][0]
        first_name = tracker.get_slot("first_name")
        number = tracker.get_slot("number")
        email = tracker.get_slot("email")   
        response_text = f"Hello {first_name}, your number is {number} and your email is {email}."
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
                {"event": "form", "first_name": None},  # Deactivate the form
                {"event": "slot", "first_name": "first_name", "value": None},  # Reset the 'first_name' slot
                {"event": "slot", "first_name": "number", "value": None},  # Reset the 'number' slot
                {"event": "slot", "first_name": "email", "value": None},  # Reset the 'email' slot
            ]