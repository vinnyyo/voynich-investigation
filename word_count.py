from folder_read import *

blue_pages = get_paragraphs_from_pages('blue')
word_count = {}
for page in blue_pages:
    for paragraph in page:
        for word in paragraph:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1


sorted_dict = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
print('Top Words From Pages With Blue Plants:')
for item in sorted_dict[:9]:
    print(item)
#print('word_count:', )
blue_pages = get_paragraphs_from_pages('not-blue')
word_count = {}
for page in blue_pages:
    for paragraph in page:
        for word in paragraph:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1


sorted_dict = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
print('Top Words From Pages With Plants That Are Not Blue:')
for item in sorted_dict[:9]:
    print(item)