import PyPDF2

with open('wtr.pdf', 'rb') as watermark_file:
	watermark_reader = PyPDF2.PdfFileReader(watermark_file)
	watermark_page = watermark_reader.getPage(0)

	with open('twopage.pdf', 'rb') as main_file:
		main_reader = PyPDF2.PdfFileReader(main_file)
		main_num_pages = main_reader.getNumPages()

		writer = PyPDF2.PdfFileWriter()

		for num in range(main_num_pages):
			page = main_reader.getPage(num)
			page.mergePage(watermark_page)
			writer.addPage(page)

		with open('new.pdf', 'wb') as file:
			writer.write(file)



