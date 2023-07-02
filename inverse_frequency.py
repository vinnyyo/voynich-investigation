from nltk import word_tokenize
from nltk.probability import FreqDist
from folder_read import *

blue_pages = get_paragraphs_from_pages('blue')
not_blue_pages = get_paragraphs_from_pages('not-blue')
all_words = []
for page in blue_pages:
    for paragraph in page:
        for word in paragraph:
            all_words.append(word)
for page in not_blue_pages:
    for paragraph in page:
        for word in paragraph:
            all_words.append(word)

#text = "your text here"
#tokens = word_tokenize(text)

# Frequency distribution
fdist = FreqDist(all_words)
freqlist = [(word, count / len(all_words)) for word, count in fdist] # can I unpack this like a tuple?
print(fdist.least_common(10))

# Print the 10 most common tokens and their percentages
print(freqlist[:10])

# Print the 10 least common tokens and their percentages
print(freqlist[:-10])

