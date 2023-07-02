import nltk
from folder_read import *
nltk.download('averaged_perceptron_tagger')

blue_pages = get_paragraphs_from_pages('blue')
tagged = nltk.pos_tag(blue_pages[0][0])

print(tagged)