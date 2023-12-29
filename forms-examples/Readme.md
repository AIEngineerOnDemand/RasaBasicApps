# Rasa Bot - Name Entity Extraction Experiment

This branch, `experiment-name-entity-extraction`, is dedicated to experimenting with different pipelines and data configurations in our Rasa bot. The main goal is to improve the bot's capability to extract unseen names as `name` entities.

## Experiment Details

We are testing various configurations of the pipeline and experimenting with different sets of training data. The aim is to find a configuration that allows the bot to generalize well from the training data and accurately extract unseen names in user messages.

## Changes Made

In this branch, we have made changes to the following files:

1. `config.yml`: We have experimented with different pipeline configurations, including the use of `DIETClassifier` and `SpacyEntityExtractor`.

2. `nlu.yml`: We have added more training examples to help the bot learn to recognize names in different contexts.

## Results

We will update this section with the results of our experiments, including any improvements in the bot's ability to extract unseen names as entities.

## Contributing

If you have any suggestions or feedback, please open an issue or submit a pull request. All contributions are welcome!