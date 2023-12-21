# Rasa Weather App

This is a weather app built using Rasa Open Source.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/your-username/rasa-weather-app.git
    ```

2. Install the required dependencies:

    ```shell
    pip install -r requirements.txt
    ```

3. Set up the necessary environment variables:

    ```shell
    export OPENWEATHERMAP_API_KEY=your-api-key
    ```

    Replace `your-api-key` with your OpenWeatherMap API key.

## Usage

1. Train the Rasa model:

    ```shell
    rasa train
    ```

2. Start the Rasa server:

    ```shell
    rasa run -m models --enable-api --cors "*"
    ```

3. Start the weather app frontend:

    ```shell
    cd frontend
    npm install
    npm start
    ```

4. Access the weather app in your browser at `http://localhost:3000`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
