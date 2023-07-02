from nltk import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
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

# Print the 10 most common tokens and their counts
print(fdist.most_common(10))

# Plot the frequency distribution
fdist.plot(30, cumulative=False)
plt.show()
plt.savefig('plot.png')