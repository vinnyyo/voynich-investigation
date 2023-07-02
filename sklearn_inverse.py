from sklearn.feature_extraction.text import TfidfVectorizer
from folder_read import *
import numpy as np

all_pages = get_paragraphs_from_pages('everything')
all_paragraph = []
for page in all_pages:
    for paragraph in page:
        all_paragraph.append(' '.join(paragraph))

# A sample corpus
# all_paragraph

# Initialize a TfidfVectorizer object
vectorizer = TfidfVectorizer()

# Learn the vocabulary and idf from the corpus, then transform the corpus into the TF-IDF matrix
X = vectorizer.fit_transform(all_paragraph)

# Convert the matrix to an array and print it
#print(X.toarray())

# To see the features (i.e., the words from the corpus) corresponding to each column in the array, print
#print()
feature_names = vectorizer.get_feature_names_out()
for i in range(len(all_paragraph)):
    print(f"Document {i+1}")
    tfidf_scores = X[i].toarray().flatten()
    sorted_indices = np.argsort(tfidf_scores)[::-1]
    for index in sorted_indices[:5]:  # Get top 5
        if tfidf_scores[index] > 0:
            print(f" - {feature_names[index]}: {tfidf_scores[index]}")
