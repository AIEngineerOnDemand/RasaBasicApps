# RasaBasicApps

This repository showcases basic apps that you can build with Rasa Open Source.

# RasaBasicApps

This repository showcases basic apps that you can build with Rasa Open Source.

## Getting Started

To get started, follow these steps:

1. Create a Python environment using Poetry in the main folder of this repository.
2. Install Spacy in your Python environment. If you're using Poetry, you can do this with the command `poetry add spacy`. If you're using pip, you can use the command `pip install spacy`.
3. Download and install the Spacy model that matches the one specified in your `config.yml` file. For example, if you're using `en_core_web_md`, you can download it using the command `poetry run python -m spacy download en_core_web_md` if you're using Poetry, or `python -m spacy download en_core_web_md` if you're using pip.
4. Each subfolder contains the code for a different app and will have its own readme with instructions.

## App List

- Restaurant Chatbot: [Link to Restaurant Chatbot readme](restaurant-chatbot/Readme.md)
- Weather App: [Link to Weather App readme](weather-app/Readme.md)


## Installation

Follow these steps to set up and run the project:

1. Clone this repository to your local machine.
2. Install the dependencies. This project uses Poetry for dependency management. If you have Poetry installed, you can install the dependencies with `poetry install`.
3. Ensure Rasa is installed. If not, you can install it with `pip install rasa`.
4. Train the chatbot model with `rasa train`.
5. Start the chatbot with `rasa run`.

Feel free to explore the different apps and their respective instructions to learn more about building chatbots with Python and Rasa Open Source.

Happy coding!