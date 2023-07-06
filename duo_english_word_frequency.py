import read_pdf_book
from nltk import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

pdf_url = 'https://nibmehub.com/opac-service/pdf/read/A%20handbook%20of%20Native%20American%20Herbs.pdf'
all_book_pages = read_pdf_book.get_all_pages(pdf_url)
all_words = []
for page in all_book_pages:
    for word in page.split(' '):
        if word != "":
            all_words.append(word.lower())

two_words = []
for i in range(len(all_words)-1):
    two_words.append(all_words[i] + ' ' + all_words[i+1])

#text = "your text here"
#tokens = word_tokenize(text)

# Frequency distribution
fdist = FreqDist(two_words)

# Print the 10 most common tokens and their counts
print(fdist.most_common(10))

# Plot the frequency distribution
fdist.plot(30, cumulative=False)
plt.show()
plt.tight_layout()
plt.savefig('plotEveryEnglishTwo.png', bbox_inches='tight')