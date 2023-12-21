from typing import Any, Text, Dict, List
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionGetWeather(Action):

    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #city = tracker.get_slot("city")
        # city = tracker.latest_message['text']
        # weather_data = self.get_weather(city)
        
        city_slot = next(tracker.get_latest_entity_values("city"), None)
        city = tracker.get_slot("city") or city_slot
        
        print(city)
        
        if city:
            weather_data = self.get_weather(city)
            print(f"City: {city}")
            print(f"weather_data: {weather_data}")
            if weather_data:
                  response = f"The weather in {city} is {weather_data['main']['temp']}°C, with {weather_data['weather'][0]['description']}"
 
        else:
            response = f"Sorry, I couldn't find out the weather for the location specified"      
      
        
        # if weather_data:
        #     response = f"The weather in {city} is {weather_data['main']['temp']}°C, with {weather_data['weather'][0]['description']}"
        # else:
        #     response = f"Sorry, I couldn't find out the weather in {city}"     

        dispatcher.utter_message(text=response)
        
        
        return []


    @staticmethod
    def get_weather(city: Text) -> Dict[Text, Any]:
        # Here goes the weather API call
        api_key = "your_api_key"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        params = {"appid": api_key, "q": city, "units": "metric"}
        try:
            print(f" API Requested URL :{base_url}?{params}")
            result = requests.get(base_url, params=params)
            api_response = result.json()
            print(f" API Response :{api_response}")
            
            if api_response['cod'] == 200:
                return api_response

        except requests.exceptions.RequestException as e:   
            print(f" API Error :{e}")

        return None