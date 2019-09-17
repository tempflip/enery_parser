# note : https://github.com/sylvainpelissier/PyPDF2/commit/357d6b40aa80b40e7edb1ae31db3671b3f8166d9
from PyPDF2 import PdfFileWriter, PdfFileReader
from PIL import Image

def process_xobject(xo):
	print(xo)
	for key in xo:
		obj = xo[key]
		print ('############', obj)
		if obj['/Subtype'] == '/Image':
			size = (obj['/Width'], obj['/Height'])
			data = obj.getData()

			print("$$$$$$$$$$$$$", size)
		
def process_text(xo):
	for key in xo:
		obj = xo[key]
		print (obj.getData())

with open("data.pdf", "rb") as f:
	pdf = PdfFileReader(f)
	page = pdf.getPage(1)
	# print(page)
	resources = page['/Resources']
	for res in resources:
		print ('R >>>>', res)
		# print (resources[res])
		# print ('-------------------------------')

		if res == '/XObject':
			process_xobject(resources[res].getObject())
		# if res == '/Font':
			# process_text(resources[res])

	# xo = res['/XObject']
	# print(xo)
	# for ob in xo:
	# 	print ('>>>>>', xo[ob])
		