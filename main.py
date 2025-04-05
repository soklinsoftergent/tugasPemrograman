import extract
import normalize

text = extract.extractPdfTexts("files/Desain Karakter Shin Ultraman Telah Terungkap.pdf")
normText = normalize.normalisasi(text)
print(normText)