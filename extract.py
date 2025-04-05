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
    with open(path_to_file, "r", encoding="utf-8") as file:
        return file.read()

#print(extractPdfTexts("files/Desain Karakter Shin Ultraman Telah Terungkap.pdf"))
