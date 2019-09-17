from PyPDF2 import PdfFileReader
import re

i = 0

with open("energy_usage.pdf", "rb") as f:
    pdf = PdfFileReader(f)
    for i in range(pdf.getNumPages()):
        page = pdf.getPage(i)
        
        print (page.extractText())
        print ('XXX_NEW_LINE_XXX')
        i+= 1
        if i == 5 : exit()
