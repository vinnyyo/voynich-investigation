import PyPDF2
from pdfminer.high_level import extract_text
import requests
import io

def get_toc(pdf_path):
    pdf = PyPDF2.PdfReader(open(pdf_path, 'rb'))
    # print(pdf.outline)
    # print(pdf.pages)
    # print(pdf.outline)
    outlines = pdf.outline
    #print(outlines)
    return [(str(outline.title), outline.page) for outline in outlines]

def get_text(pdf_path, start_page, end_page):
    text = ''
    for i in range(start_page, end_page):
        text += extract_text(pdf_path, page_numbers=[i])
    return text

def process_pdf(pdf_path):
    toc = get_toc(pdf_path)
    sections = {}
    for i in range(len(toc) - 1):
        title, start_page = toc[i]
        _, end_page = toc[i + 1]
        sections[title] = get_text(pdf_path, start_page, end_page)
    # last section
    title, start_page = toc[-1]
    sections[title] = get_text(pdf_path, start_page, None)
    return sections

#sections = process_pdf('A handbook of Native American Herbs.pdf')

# Now sections is a dictionary where the keys are the titles from the table
# of contents, and the values are the text of the corresponding sections.
#print(sections)
# pdf_path = 'A handbook of Native American Herbs.pdf'
# pdf = PyPDF2.PdfReader(open(pdf_path, 'rb'))

# pdf_url = 'https://nibmehub.com/opac-service/pdf/read/A%20handbook%20of%20Native%20American%20Herbs.pdf'
# response = requests.get(pdf_url)
# pdf_stream = io.BytesIO(response.content)
# pdf = PyPDF2.PdfReader(pdf_stream)
    
# print(pdf.outline[3].title)
# print(pdf.outline[3].page)
# papge = pdf.outline[3].page
# print(pdf.pages[34].extract_text().replace('\t',' ').replace('\n',' '))
#print(pdf.)
#print(pdf.outline)
#outlines = pdf#.outline()
#print(outlines)
# print(pdf.outline[3].title)
# print(pdf.outline[3].page)
# papge = pdf.outline[3].page
# print()
    


def get_all_pages(url):
    response = requests.get(url)
    pdf_stream = io.BytesIO(response.content)
    pdf = PyPDF2.PdfReader(pdf_stream)
    output = []
    for page in pdf.pages:
        output.append(page.extract_text().replace('\t',' ').replace('\n',' '))
    return output