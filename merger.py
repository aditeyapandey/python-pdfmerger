from PyPDF2 import PdfFileMerger
import sys
import glob

pdfs = glob.glob("PDFFiles/*.pdf")

# Exit if there are less than 2 files to merge
if len(pdfs)<2:
    print("Not enough files to merge!")
    sys.exit()

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()