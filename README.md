
# Python-PDFMerger

This python script will merge your python folders remotely on your computer.

Saves you from uploading pdf files that may contain confidential data to cloud or third-party softwares.

## Setup

Requires Python > 2.7

Requires Py2PDF: https://pypi.org/project/PyPDF2/, **Install: pip install PyPDF2**

## Usage

1. Clone the github repo: https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository

2. > cd python-pdfmerger

3. In the >PDFFiles Folder you can add the files that you want to merge. The name of the files have to be in a specific format to ensure ordering of pdfs in the final merged document.

    *File 1: 1.pdf<br>
    File 2: 2.pdf \\
    File 3: 3.pdf \\
    :\\
    :\\
    File 100: 100.pdf*

4. > python merger.py

## 

A merged file will be produced named: result.pdf 
