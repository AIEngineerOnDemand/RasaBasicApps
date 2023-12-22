from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests

class ActionRecommendMovie(Action):

    def name(self) -> Text:
        return "action_recommend_movie"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        genre = next(tracker.get_latest_entity_values("genre"), None)
        
        if not genre:
            response = "Sorry, I do not have any movie recommendations for that genre."
            dispatcher.utter_message(text=response)
            return []
        
        # Make API request to fetch movie recommendations based on genre
        api_key = "your_api_key_here"
        
        # Fetch genre ID from TMDb API
        genre_id = self.get_genre_id(genre, api_key)
        
        if genre_id:
            url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}'
            response = requests.get(url)
            
            if response.status_code == 200:
                movies = response.json().get("results",[])
                print(movies)
                if movies:
                    response_text = f"Here are some {genre} movies you might like - "
                    for movie in movies[:5]:
                        response_text += f"{movie['title']} ({movie['release_date'][:4]}), "
                    response_text = response_text[:-2]
                else:
                    response_text = "I'm sorry, I couldn't find any recommendations for that genre."
            else:
                response_text = "Oops! Something went wrong while fetching recommendations. Please try again later."
        else:
            response_text = "I'm sorry, I couldn't find that genre in my database."    
            
        dispatcher.utter_message(text=response_text)
                        
        return []
    
    @staticmethod
    def get_genre_id(genre, api_key):
        url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
        response = requests.get(url)
        
        if response.status_code == 200:
            genres = response.json().get("genres",[])
            for g in genres:
                if g["name"].lower() == genre.lower():
                    return g["id"]
        return None


