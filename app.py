import streamlit as st
import pickle

# Load the saved model and vectorizer
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('save_cv.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Define a function to make predictions
def predict_sentiment(review):
    review_transformed = vectorizer.transform([review]).toarray()
    prediction = model.predict(review_transformed)[0]
    return 'Positive review' if prediction == 1 else 'Negative review'

# Streamlit App Interface
st.title("Movie Review Sentiment Analyzer")
st.write("This app predicts the sentiment of a movie review (positive or negative) based on its content.")

# Text input for the review
review_input = st.text_area("Enter a movie review:", "")

# Button to make prediction
if st.button("Predict Sentiment"):
    if review_input:
        result = predict_sentiment(review_input)
        st.success(f"The review is predicted to be: {result}")
    else:
        st.error("Please enter a review for prediction.")
