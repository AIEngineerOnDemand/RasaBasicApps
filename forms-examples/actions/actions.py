from typing import Any, Text, Dict, List, Optional
from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import SlotSet,FollowupAction
from rasa_sdk.interfaces import EventType
from rasa_sdk.types import DomainDict

def clean_name(name):
    return "".join([c for c in name if c.isalpha()])

class ActionCheckIfFirstNameIsKnown(Action):
    def name(self) -> Text:
        return "action_check_if_first_name_is_known"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        confirm_first_name = tracker.get_slot('confirm_first_name')

        if not confirm_first_name:
    # start the contact form
             return [FollowupAction("contact_form")]
        else: 
            # do nothing
            pass 

class ActionCheckConfirmFirstName(Action):

    def name(self) -> Text:
        return "action_check_confirm_first_name"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        confirm_first_name = tracker.get_slot('confirm_first_name')

        if confirm_first_name:
            # perform the action to confirm the first name
            dispatcher.utter_message(text=  f"Use this name {confirm_first_name}?")
        else:
            # do nothing
            pass

        return []       
        
class ActionSetFirstName(Action):

    def name(self) -> Text:
        return "action_set_first_name"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        confirm_first_name = tracker.get_slot('confirm_first_name')
        
        if confirm_first_name:
            # Perform the action to set the first name
            print('collecting',confirm_first_name)
            return [SlotSet("first_name", confirm_first_name), SlotSet("confirm_first_name", None),  
                    FollowupAction("contact_form")]
        else:
            pass    


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
    # async def extract_first_name(
    #     self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    # ) -> Dict[Text, Any]:
    #     text_of_last_user_message = tracker.latest_message.get("text")
    #     intent = tracker.latest_message['intent'].get('name')
    #     if intent == "inform":
    #         return  {"first_name": None , "confirm_first_name": text_of_last_user_message}
    #     else:
    #         return {"first_name": None, "confirm_first_name": None}
    # async def validate_confirm_first_name(
    #     self,
    #     slot_value: Any,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     slot_value = clean_name(slot_value)
    #     if slot_value: 
    #             if slot_value  and len(slot_value) > 2 :       
    #                 dispatcher.utter_message(text=f"Use this name {slot_value}?")
    #                 return {"first_name": slot_value, "confirm_first_name": slot_value}
    #             else:
    #                 return {"first_name": None, "confirm_first_name": None}
    #     else:
    #         return {"first_name": None, "confirm_first_name": None}
            
    async def validate_first_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        prev_mentioned_name = tracker.get_slot("confirm_first_name")
        prev_mentioned_name = clean_name(prev_mentioned_name) if prev_mentioned_name else None

        slot_value = clean_name(slot_value)
        if len(slot_value) < 3:
                dispatcher.utter_message(text="Your first_name should be at least 3 characters long.")
                return {"first_name": None, "confirm_first_name": None}
        if slot_value== prev_mentioned_name:
            return {"first_name": slot_value, "confirm_first_name": slot_value}
  
  
    
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
        response_text = f"We have collected the following information:  1. name {first_name}, 2 number {number}, 3 email is {email}."
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
          return  [
                {"first_name": None, "email": None, "number": None, "confirm_first_name": None}
            ]