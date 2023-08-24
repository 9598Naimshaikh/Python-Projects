# create a PDF Merger Programm...

from PyPDF2 import PdfMerger
import os

merger = PdfMerger()
folder_path = os.listdir()

for file in folder_path:
    if file.endswith('pdf'):
        merger.append(file)


merger.write('Merged.pdf')
merger.close()
