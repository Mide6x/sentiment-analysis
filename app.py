import streamlit as st
import nltk
import ssl
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

ssl._create_default_https_context = ssl._create_unverified_context


st.title("Sentiment Analysis App by Olumide Adewole")

user_name = st.text_input("What's your name?")
if user_name:
    st.write(f"Hello, {user_name}!")

#Name of course
course_name = st.text_input("Enter the course you want to make comments about:")
if course_name:
    st.write(f"You want to make comments about the course: {course_name}")

#Nature of comment
user_input = st.text_area("Enter your comments about the lecture and lecturer:")

if user_input:
    st.write(f"You: {user_input}")

#Sentiment analysis function
def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)

    # Determine sentiment
    if sentiment_scores['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Analyze sentiment on user input
if user_input:
    sentiment = analyze_sentiment(user_input)
    st.write(f"Sentiment: {sentiment}")

    # Display sentiment-specific message including the course name
    if sentiment == 'Positive':
        st.success(f"You made a positive comment about the lecturer of {course_name}!")
    elif sentiment == 'Negative':
        st.error(f"You made a negative comment about the lecturer of {course_name}.")
    else:
        st.info(f"You made a neutral comment about the lecturer of {course_name}.")
