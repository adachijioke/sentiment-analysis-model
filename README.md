# Movie Review Sentiment Analysis with Streamlit

This project is a web application that performs sentiment analysis on movie reviews using a pre-trained machine learning model. The app is built using Streamlit and allows users to input a movie review, analyze its sentiment, and display whether it is positive or negative.

## Features

- **User Input**: Users can input a movie review directly through the web interface.
- **Sentiment Analysis**: The app analyzes the sentiment of the review as either positive or negative using a machine learning model.
- **Pre-trained Model**: The sentiment analysis model is trained on a dataset of movie reviews and saved as a `.pkl` file for loading.

## Tech Stack

- **Backend**: Python (Streamlit)
- **Machine Learning**: scikit-learn (Multinomial Naive Bayes)
- **Vectorization**: TfidfVectorizer

## Prerequisites

Make sure you have the following installed:

- Python 3.6+
- Streamlit
- scikit-learn
- pandas
- numpy
- nltk

You can install all required dependencies by running:

```bash
pip install -r requirements.txt
```

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/movie-review-sentiment-analysis-streamlit.git
   cd movie-review-sentiment-analysis-streamlit
   ```

2. **Install Dependencies**

   Install the necessary packages from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download Pre-Trained Model and Vectorizer**

   Make sure `model.pkl` (the pre-trained model) and `save_cv.pkl` (the TfidfVectorizer) are saved in the root directory of your project.

## How to Run the Application

1. Run the Streamlit app using the following command:

   ```bash
   streamlit run app.py
   ```

2. Open your browser and go to:

   ```
   http://localhost:8501
   ```

## Usage

1. Enter a movie review in the text box provided on the homepage.
2. Click the "Analyze Review" button.
3. The app will display the sentiment of the review (either "positive" or "negative").

## File Structure

```
.
├── app.py                 # Streamlit application file
├── model.pkl              # Pre-trained sentiment analysis model
├── save_cv.pkl            # Pre-trained TfidfVectorizer for feature extraction
├── requirements.txt       # List of dependencies
└── README.md              # This file
```

## Requirements

The required dependencies for running the app are:

```bash
streamlit==1.4.0
scikit-learn==1.0.2
pandas==1.3.5
numpy==1.21.4
nltk==3.6.5
```

## Acknowledgments

This project uses a dataset of movie reviews to train the sentiment analysis model. The data preprocessing includes tokenization, removal of stopwords, and vectorization using TF-IDF.