from PyPDF2 import PdfReader

def extractPdfTexts(path_to_pdf):
    #extract PDF texts
    reader = PdfReader(path_to_pdf)
    page = ""
    for i in range(len(reader.pages)):
        read = reader.pages[i]
        pdfText = read.extract_text()
        page = page + pdfText

    return str(page)

def extract(path_to_file):
    file = open(path_to_file, "r")
    return str(file)

#print(extractPdfTexts("files/Desain Karakter Shin Ultraman Telah Terungkap.pdf"))
