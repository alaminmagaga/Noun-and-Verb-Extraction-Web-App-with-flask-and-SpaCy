# Noun and Verb Extraction Web App

The Noun and Verb Extraction Web App was developed using the Flask framework and offers a powerful solution for extracting nouns and verbs from text documents. By implementing advanced natural language processing techniques, including part-of-speech tagging, the app effectively identifies and extracts nouns and verbs from the provided text. The user interface is designed to be intuitive, allowing users to paste text and receive a comprehensive list of extracted nouns and verbs.

## Introduction

The Noun and Verb Extraction Web App provides an efficient way to extract nouns and verbs from text documents. Whether you're analyzing written content, conducting linguistic research, or performing any task that requires noun and verb identification, this web app simplifies the process.

## Features

- **Noun Extraction**: The app utilizes part-of-speech tagging to identify and extract nouns from the provided text.
- **Verb Extraction**: The app employs advanced natural language processing techniques to identify and extract verbs from the provided text.
- **Intuitive User Interface**: The user interface allows users to easily input text and receive a comprehensive list of extracted nouns and verbs.
- **Efficient Processing**: The app efficiently processes the text and provides quick results, enabling users to save time and effort.

## Technologies Used

The Noun and Verb Extraction Web App is built using the following technologies:

- Flask: Python web framework for building the application.
- Python: Programming language used for development.
- Natural Language Processing (NLP): Techniques and libraries for part-of-speech tagging and text analysis.
- HTML/CSS: Markup and styling for the web interface.

## Installation

To run the Noun and Verb Extraction Web App locally, follow these steps:

```
git clone https://github.com/alaminmagaga/Noun-and-Verb-Extraction-Web-App-with-flask-and-SpaCy.git
```
```
cd Noun-and-Verb-Extraction-Web-App-with-flask-and-SpaCy
```
```
python -m venv venv
```

Activate the virtual environment:

- For Windows: 
```
venv\Scripts\activate
```
- For Unix or Linux: 
```
source venv/bin/activate
```

Install the required dependencies:
```
pip install -r requirements.txt
```
```
python app.py
```

The web app will be accessible at `http://localhost:5000`.

## Usage

1. Open your web browser and go to `http://localhost:5000`.
2. Paste the text you want to analyze into the provided input field.
3. Click the "Extract" button to initiate the noun and verb extraction process.
4. The app will generate a comprehensive list of extracted nouns and verbs from the provided text.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Make your modifications and commit them: `git commit -am 'Add some feature'`
4. Push the branch to your forked repository: `git push origin feature-name`
5. Submit a pull request to the original repository.

## License

This project is licensed under the [MIT License](LICENSE).


