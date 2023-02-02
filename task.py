from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


def extractPdfText(pdf_file):
    resourceManager = PDFResourceManager()
    stringIo = StringIO()
    device = TextConverter(resourceManager, stringIo, laparams=LAParams())
    interpreter = PDFPageInterpreter(resourceManager, device)
    for page in PDFPage.get_pages(pdf_file, caching=True, check_extractable=True):
        interpreter.process_page(page)
    text = stringIo.getvalue()
    stringIo.close()
    device.close()
    return text


def compareFiles(file1Path, file2Path):
    file1 = open(file1Path, "r")
    file2 = open(file2Path, "r")

    for line in file1:
        if line == file2.readline():
            print(line)
            pass
        else:
            print("mismatch")

    file1.close()
    file2.close()


pdfFile = open('test_task.pdf', 'rb')
pdfData = extractPdfText(pdfFile)
pdfFile.close()

outputFile = open("output.txt", "w")
outputFile.write(pdfData)
outputFile.close()

compareFiles('output.txt', 'goldenOutput.txt')
