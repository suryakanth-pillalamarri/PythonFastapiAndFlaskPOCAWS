import os
#FOR CREATING READING AND WRITING FILES
import zipfile
#FOR READIN GPDF FILES
from PyPDF2 import PdfReader
#fro working on pdf fiels
import fitz  # PyMuPDF
from PIL import Image
import tempfile
import time
import logging
import sys




class PDFScreenshotExtractor:
    def __init__(self, pdf_path, zip_filename):
        self.pdf_path = pdf_path
        self.output_folder = tempfile.mkdtemp()  # Useing a temporary directory for images
        self.zip_filename = zip_filename

    def extract_images(self):
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
        
        with open(self.pdf_path, 'rb') as pdf_file:
            pdf = PdfReader(pdf_file)
            for page_num in range(len(pdf.pages)):
                page = fitz.open(self.pdf_path).load_page(page_num)
                pix = page.get_pixmap()
                Image.frombytes("RGB", [pix.width, pix.height], pix.samples).save(
                    os.path.join(self.output_folder, f"page_{page_num+1}.png")
                )

    def create_zip(self):
        self.extract_images()
        if os.path.exists(self.zip_filename):
            os.remove(self.zip_filename)  # Remove existing zip file
        with zipfile.ZipFile(self.zip_filename, 'w') as zipf:
            for root, _, files in os.walk(self.output_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, self.output_folder))
                    print(f"Added to ZIP: {file_path}")
        print(f"Zip file '{self.zip_filename}' created successfully.")
          




# #taking pdf file 
# pdf_path=r"D:\Surya files\pythonaws_poc_2024\Third_problem\pdffiles\python_cheat_sheet_plotly.pdf"
# #for saving the screenshots in a temporarey folder

# # Path to the Downloads folder
# downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# # adding the zip file name with downloads such that it appears in downloads folder
# zip_filename = os.path.join(downloads_folder, "pdf_screenshots.zip")


# #creating object for the extracter class
# extracter=PDFScreenshotExtractor(pdf_path,zip_filename)
# # extracter.extract_images()
# extracter.create_zip()