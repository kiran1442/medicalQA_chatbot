# Medical Q&A Chatbot using MedQuAD Dataset

This project is a specialized medical question-answering chatbot using the MedQuAD dataset. It employs TF-IDF vectorization for efficient retrieval of relevant medical answers and is designed with a simple user interface using Streamlit.

## Features

- Efficient Retrieval:Uses TF-IDF vectorization for fast similarity searches.

- Medical Entity Recognition: Provides answers to user questions based on medical terms found in the MedQuAD dataset.

- Streamlit Interface: Interactive UI to enter questions and retrieve answers.

## Prerequisites
### Ensure you have the following installed:
- Python 3.7 or higher
<!-- start:code block -->
### Install the required dependencies using pip:
    pip install -r requirements.txt
<!-- end:code block -->

## Getting Started
### Download the MedQuAD Dataset: 
Download the XML files from the MedQuAD GitHub repository and place them in a dataset/ folder in the project directory.

### Run the Chatbot:
<!-- start:code block -->
### Run the following command in the terminal to start the chatbot interface:
    streamlit run chatbot.py
<!-- end:code block -->

### Enter a Medical Question: 
Once the Streamlit interface opens, you can enter a medical question, and the chatbot will retrieve the most relevant answer from the MedQuAD dataset.

## How It Works

### Data Loading: 
The XML files in the MedQuAD dataset are parsed to extract medical question-answer pairs.

### TF-IDF Vectorization:
The TfidfVectorizer is used to vectorize the questions for efficient similarity matching.
The TF-IDF matrix and vectorizer are saved as .pkl files (tfidf_matrix.pkl and tfidf_vectorizer.pkl) to reduce load times on future runs.

### Answer Retrieval:
For each user query, the chatbot transforms it into the TF-IDF space and calculates cosine similarity with the questions in the dataset.
The answer corresponding to the most similar question is returned.

# Project Structure

- app.py: The main Streamlit application script.
- requirements.txt: A list of required Python packages for the project.
- tfidf_matrix.pkl: This file stores the TF-IDF matrix, which is a sparse matrix representation of all the questions in the dataset.
- tfidf_vectorizer.pkl: This file stores the vocabulary(uniques words) and IDF value for each term across all the questions in the dataset.
- DataLoad.py: Data loading and analysis file.
- main.py: Main code for the project.