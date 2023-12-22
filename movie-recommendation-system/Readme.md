# Movie Recommendation System

This is a movie recommendation system built using Rasa Open Source. It recommends movies based on the genre provided by the user.

## Table of Contents

- [Movie Recommendation System](#movie-recommendation-system)
  - [Table of Contents](#table-of-contents)
  - [Contributing](#contributing)
  - [License](#license)


1. Train the Rasa model:

    ```shell
    rasa train
    ```

2. Start the Rasa server:

    ```shell
    rasa run -m models --enable-api --cors "*"
    ```

3. Start the action server:

    ```shell
    rasa run actions
    ```

4. Interact with the bot in your terminal or connect it to a frontend of your choice.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details