from sklearn.feature_extraction.text import TfidfVectorizer
from folder_read import *
import numpy as np

blue_pages = get_paragraphs_from_pages('blue')
all_blue_paragraph = []
for page in blue_pages:
    for paragraph in page:
        all_blue_paragraph.append(' '.join(paragraph))

not_blue_pages = get_paragraphs_from_pages('not-blue')
all_not_blue_paragraph = []
for page in not_blue_pages:
    for paragraph in page:
        all_not_blue_paragraph.append(' '.join(paragraph))

# A sample corpus
# all_paragraph

# Initialize a TfidfVectorizer object
vectorizer_blue = TfidfVectorizer()
vectorizer_not_blue = TfidfVectorizer()

# Learn the vocabulary and idf from the corpus, then transform the corpus into the TF-IDF matrix
X_blue = vectorizer_blue.fit_transform(all_blue_paragraph)

# Convert the matrix to an array and print it
#print(X.toarray())

# To see the features (i.e., the words from the corpus) corresponding to each column in the array, print
#print()
feature_names_blue = vectorizer_blue.get_feature_names_out()
print("==== Significant blue plant words ====")
# For each document, print the words with the highest TF-IDF scores
for i in range(len(all_blue_paragraph)):
    print(f"Document {i+1}")
    tfidf_scores = X_blue[i].toarray().flatten()
    sorted_indices = np.argsort(tfidf_scores)[::-1]
    for index in sorted_indices[:5]:  # Get top 5
        if tfidf_scores[index] > 0:
            print(f" - {feature_names_blue[index]}: {tfidf_scores[index]}")

# Learn the vocabulary and idf from the corpus, then transform the corpus into the TF-IDF matrix
X_not_blue = vectorizer_blue.fit_transform(all_not_blue_paragraph)

# Convert the matrix to an array and print it
#print(X.toarray())

# To see the features (i.e., the words from the corpus) corresponding to each column in the array, print
#print()
feature_names_not_blue = vectorizer_blue.get_feature_names_out()
print("==== Significant non-blue plant words ====")
# For each document, print the words with the highest TF-IDF scores
for i in range(len(all_not_blue_paragraph)):
    print(f"Document {i+1}")
    tfidf_scores = X_not_blue[i].toarray().flatten()
    sorted_indices = np.argsort(tfidf_scores)[::-1]
    for index in sorted_indices[:5]:  # Get top 5
        if tfidf_scores[index] > 0:
            print(f" - {feature_names_not_blue[index]}: {tfidf_scores[index]}")