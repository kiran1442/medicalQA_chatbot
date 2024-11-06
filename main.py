import os
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib
from DataLoad import *

# Load the Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')
print("DONE")

# Generate embeddings for each question in the dataset
print("--------------Start----------------")


# Initialize TF-IDF Vectorizer
tfidf_matrix_path = 'tfidf_matrix.pkl'
tfidf_vectorizer_path = 'tfidf_vectorizer.pkl'

# Check if TF-IDF matrix and vectorizer already exist
if os.path.exists(tfidf_matrix_path) and os.path.exists(tfidf_vectorizer_path):
    # Load existing TF-IDF matrix and vectorizer
    tfidf_matrix = joblib.load(tfidf_matrix_path)
    vectorizer = joblib.load(tfidf_vectorizer_path)
    print("Loaded TF-IDF matrix and vectorizer from disk.")
else:
    # Initialize TF-IDF Vectorizer and create matrix
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['question'])

    # Save TF-IDF matrix and vectorizer to disk for future use
    joblib.dump(tfidf_matrix, tfidf_matrix_path)
    joblib.dump(vectorizer, tfidf_vectorizer_path)
    print("TF-IDF matrix and vectorizer created and saved to disk.")


# Function to retrieve the most relevant answer
def retrieve_answer(user_question):
    # Transform the user question to TF-IDF space
    user_question_tfidf = vectorizer.transform([user_question])

    # Compute cosine similarity between user question and all dataset questions
    similarities = cosine_similarity(user_question_tfidf, tfidf_matrix)
    most_similar_idx = similarities.argmax()
    best_match_score = similarities[0][most_similar_idx]

    # Fallback if similarity is too low
    if best_match_score < 0.2:
        return "I'm sorry, I couldn't find a relevant answer."

    return df.iloc[most_similar_idx]['answer']


print("-----------END----------------")

