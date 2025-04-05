def extractPdfTexts(path_to_pdf):
    from PyPDF2 import PdfReader

    #extract PDF texts
    reader = PdfReader(path_to_pdf)
    page = ""
    for i in range(len(reader.pages)):
        read = reader.pages[i]
        pdfText = read.extract_text()
        page = page + pdfText

    return str(page)

#print(extractPdfTexts("files/Desain Karakter Shin Ultraman Telah Terungkap.pdf"))
