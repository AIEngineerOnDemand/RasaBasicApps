This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionRecommendMovie(Action):

    def name(self) -> Text:
        return "action_recommend_movie"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        genre = next(tracker.get_latest_entity_values("genre"), None)

        if genre == "comedy":
            recommeded_movie = ["The Hangover", "Knocked Up", "Superbad", "Step Brothers",
                                "Bridesmaids", "Dumb and Dumber", "Anchorman", "Old School", 
                                "Wedding Crashers", "Talladega Nights", "Mean Girls", "Pitch Perfect",
                                "Zoolander", "Napoleon Dynamite", "Anchorman 2: The Legend Continues",
                                "The 40-Year-Old Virgin", "Elf", "Airplane!", "Shaun of the Dead"]
        elif genre == "action":
            recommeded_movie = ["The Dark Knight", "The Lord of the Rings: The Return of the King", 
                                "Inception", "The Lord of the Rings: The Fellowship of the Ring",
                                "The Matrix", "Gladiator", "Braveheart", "Saving Private Ryan",
                                "The Departed", "The Lord of the Rings: The Two Towers", "Mad Max: Fury Road",
                                "Die Hard", "The Avengers", "Mission: Impossible - Fallout",
                                "John Wick", "The Bourne Identity", "The Terminator", "Kill Bill"]
        elif genre == "horror":   
            recommeded_movie = ["The Exorcist", "The Shining", "The Conjuring", "The Cabin in the Woods",
                                "The Babadook", "The Descent", "The Witch", "The Orphanage", 
                                "The Others", "The Ring", "Get Out", "A Quiet Place", "Hereditary",
                                "Psycho", "Halloween", "Nightmare on Elm Street", "The Texas Chainsaw Massacre"]
        elif genre == "romance":
            recommeded_movie = ["Titanic", "The Notebook", "The Fault in Our Stars", "A Walk to Remember",
                                "The Vow", "Dear John", "The Lucky One", "The Last Song", 
                                "The Best of Me", "Safe Haven", "La La Land", "Before Sunrise", "Eternal Sunshine of the Spotless Mind",
                                "Romeo + Juliet", "500 Days of Summer", "The Princess Bride", "Crazy Rich Asians"]
        elif genre == "drama": 
            recommeded_movie = ["The Shawshank Redemption", "The Godfather", "The Godfather: Part II",
                                "Pulp Fiction", "Fight Club", "Goodfellas", "The Social Network",
                                "The Green Mile", "The Prestige", "American Beauty",
                                "Schindler's List", "The Great Gatsby", "The Revenant", "The King's Speech"]
        else :
            recommeded_movie =[]
            
        if recommeded_movie:
            response = f"Here are some {genre} movies you might like: " + ", ".join(recommeded_movie)
        else:       
            response = "Sorry, I do not have any movie recommendations for that genre."
        
        dispatcher.utter_message(text=response)
        
        return []
