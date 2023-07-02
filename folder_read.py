import re
import os

def get_paragraphs_from_pages(folder_name):
    # Get a list of filenames in the directory
    pages_list = os.listdir('pages/' + folder_name + '/')
    paragraphs = []
    paragraph_count = 0
    for page in pages_list:
        this_page = []
        # Open the file
        with open('pages/' + folder_name + '/' + page, 'r') as file:
            paragraph = []
            # Read each line in the file
            for line in file:
                # Split the line into words
                words = re.split('[\.!*%-]+', line.split(';C>')[1].strip())
                # Iterate through each word in the line
                for word in words:
                    # Print the word
                    if word != '':
                        paragraph.append(word.replace('=',''))
                    if '=' in word:
                        this_page.append(paragraph)
                        paragraph = []
                        paragraph_count += 1
        paragraphs.append(this_page)
    #print(paragraph_count)
    return paragraphs