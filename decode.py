from folder_read import *


blue_pages = get_paragraphs_from_pages('blue')
#print(blue_pages)
page_union = set()
for paragraph in blue_pages[0]:
    page_union = set(paragraph) | page_union
blue_page_intersection = page_union
for page in blue_pages:
    page_union = set()
    for paragraph in page:
        page_union = set(paragraph) | page_union
    blue_page_intersection = blue_page_intersection & page_union
print('blue:',blue_page_intersection)


blue_pages = get_paragraphs_from_pages('not-blue')
#print(blue_pages)
page_union = set()
for paragraph in blue_pages[0]:
    page_union = set(paragraph) | page_union
blue_page_intersection = page_union
for page in blue_pages:
    page_union = set()
    for paragraph in page:
        page_union = set(paragraph) | page_union
    blue_page_intersection = blue_page_intersection & page_union

print('not blue:',blue_page_intersection)