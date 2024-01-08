# Rasa Bot - Name Entity Extraction Experiment

This branch, `experiment-name-entity-extraction`, is dedicated to experimenting with different pipelines and data configurations in our Rasa bot. The main goal is to improve the bot's capability to extract unseen names as `name` entities.

## Experiment Details

We are testing various configurations of the pipeline and experimenting with different sets of training data. The aim is to find a configuration that allows the bot to generalize well from the training data and accurately extract unseen names in user messages.

In addition, we have developed a technique to capture users' names and fill in the form seamlessly. There are two slots for the first name entity: one is captured using entity recognition, and the other is used to record and process free text within an active form in conjunction with precise instructions on name format. The logic is expressed through a combination of simple rules that trigger custom actions implementing small decisions.

## Name Capturing Technique

Our bot uses a two-slot system to capture and process the user's first name during a conversation. 

1. The first slot, `first_name`, is filled using entity recognition. When the user provides their name during the conversation, our bot uses the trained NLU model to recognize and extract the name as a `first_name` entity.

2. The second slot, `confirm_first_name`, is used to handle free text within an active form. When the form is active, the user's input is processed as free text. This allows us to capture the user's name even if it's provided in a format that the entity recognizer might not understand.

The bot then uses a set of rules and custom actions to process the captured name. If the name is captured using entity recognition, it's directly filled into the `first_name` slot. If the name is captured as free text within the active form, the bot uses the `confirm_first_name` slot to process the name according to a set of predefined instructions on name format.

This two-slot system allows our bot to handle a wide range of user inputs and capture the user's name accurately and efficiently.
## Changes Made

In this branch, we have made changes to the following files:

1. `config.yml`: We have experimented with different pipeline configurations, including the use of `DIETClassifier` and `SpacyEntityExtractor`.
2. `forms-examples`: This file contains examples of forms that use the new name capturing technique.
3. `rules.yml`: This file contains the rules that trigger the custom actions for name capturing.
4. `actions.py`: This file contains the custom actions that implement the logic for name capturing.
## Changes Made



## Results

We will update this section with the results of our experiments, including any improvements in the bot's ability to extract unseen names as entities.

## Contributing

If you have any suggestions or feedback, please open an issue or submit a pull request. All contributions are welcome!