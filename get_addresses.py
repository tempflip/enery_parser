from PyPDF2 import PdfFileReader
import re

page_text = []
with open("data.pdf", "rb") as f:
    pdf = PdfFileReader(f)
    for i in range(pdf.getNumPages()):
        page = pdf.getPage(i)
        page_text.append(page.extractText())

pattern = '(AB Stora Tunabyggen\n)(\d+ |\d+: \d+|\d+-\d+:  |\d+-\d+: \d+ +|)(.+) +\((.+)\)\n(.+)'
addr_set = set()
print('\t'.join(['number', 'address', 'type'])) 
for i, text in enumerate(page_text):
    match = re.match(pattern, text)
    if match:
        num = match.group(2)
        addr = match.group(3)
        type = match.group(4)
        if addr in addr_set : continue

        addr_set.add(addr)
        
        print('\t'.join([num, addr, type]))
    else:
        print(i, "####NO MATCH####")
        print(text)

