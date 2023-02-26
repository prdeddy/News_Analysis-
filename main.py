import pandas as pd
import os
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

results_dir = 'results'
dfs = {}

for filename in os.listdir(results_dir):
    if filename.endswith('.txt'):
        year = int(filename.split('.')[0])
        with open(os.path.join(results_dir, filename), 'r') as f:
            lines = f.readlines()
        contents = []
        dates = []
        for line in lines:
            date_str, content = line.split(' ', 1)
            date = pd.Timestamp(date_str)
            contents.append(content.strip())
            dates.append(date)
        df = pd.DataFrame({'date': dates, 'content': contents})
        dfs[year] = df


def lemmatization(text):
    # Create a WordNetLemmatizer object
    lemmatizer = WordNetLemmatizer()

    # Tokenize the text into words
    words = nltk.word_tokenize(text)

    # Lemmatize each word in the list of words
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

    # Join the lemmatized words into a new string
    lemmatized_text = " ".join(lemmatized_words)
    return lemmatized_text


def remove_stop_words(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text)

    # Get the list of English stop words from nltk
    stop_words = set(stopwords.words('english'))

    # Filter out the stop words from the list of words
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Join the filtered words into a new string
    filtered_text = " ".join(filtered_words)
    return filtered_text


def word_count(text):
    words = text.split()
    word_counts = Counter(words)
    return word_counts


###-----------------------------------------------------------###



cleaned_text = []
years = []
for year in range(2002,2023):
    year_content = ' '.join([text for text in dfs[year].content]).lower()
    clean_year_content = re.sub('[^a-z]',' ',year_content)
    clean_year_content = re.sub('\s+',' ',clean_year_content)
    lemmatized_content = lemmatization(clean_year_content)
    useful_text = remove_stop_words(lemmatized_content)
    cleaned_text.append(useful_text)
    years.append(year)

cleaned_data = pd.DataFrame({'Year':years,'Content':cleaned_text})
cleaned_data.to_csv('toi_data_cleaned.csv')

word_of_interest = "naxal,maoist"
word_of_interest = word_of_interest.split(',')
# Create a list to store the word count for the word of interest for each year
word_count_by_year = []





