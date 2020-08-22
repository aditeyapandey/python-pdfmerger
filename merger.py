from PyPDF2 import PdfFileMerger
import sys

totalFiles = input() 

print(totalFiles)

if totalFiles==1:
    print("Not enough files to merge!")
    sys.exit()

pdfs = []

for x in range (totalFiles):
    file = input()
    pdfs.append(file)

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()