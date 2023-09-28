# Prayer Generator App

This Flask-based web application generates prayers and Bible verses using OpenAI's GPT-3.5 Turbo model. Users can input their prayer request, and the app will provide a prayer or Bible verse in response.

## Getting Started

These instructions will help you set up and run the Prayer Generator App on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Flask
- OpenAI Python SDK

### Installation

1. Clone this repository:


   git clone https://github.com/ortiz2030/PrayerApp.git
   cd prayer-generator-app


2. Install the required Python packages:

 
   pip install -r requirements.txt


3. Set your OpenAI API key as an environment variable:


   export OPENAI_API_KEY=your-api-key


### Usage

1. Start the Flask application:


   python app.py


2. Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

3. Enter a prayer request in the input box and click "Generate."

4. The app will respond with a generated prayer or Bible verse.

### API Key Management

To keep your API key secure, consider using environment variables or a secret management tool.

## How It Works

The app uses OpenAI's GPT-3.5 Turbo model to generate responses based on user input. Conversations are stored in a JSON file (`conversations.json`) for reference.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for providing the GPT-3.5 Turbo model.
- Flask for the web framework.

## Contributing

If you'd like to contribute to this project, please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests to us.

## Authors

- Ortiz2030- [Your GitHub Profile](https://github.com/ortiz2030)

## Questions or Issues

If you have any questions or encounter issues with the application, please open an issue on the [GitHub repository](https://github.com/ortiz2030/PrayerApp/issues).
