import pandas as pd
import numpy as np
import pypdf, pytesseract, os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Ed006315\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
path_to_pdf = f"PDFs/path/"

# loop through all the files in the path to pdf folder
for file_name in os.listdir(path_to_pdf):
    if file_name.endswith(".pdf"):
        full_path_to_pdf = os.path.join(path_to_pdf, file_name)


        data = pypdf.PdfReader(full_path_to_pdf).pages
        for page_number, page in enumerate(data):

            # extract text
            text = page.extract_text()
            print(text)

            # save images from page and perform OCR
            for img_number, image_file_object in enumerate(page.images):
                with open(f"Outputs/{file_name}_{page_number}_{img_number}.png", "wb") as img_file:
                    img_file.write(image_file_object.data)
                imagestring = pytesseract.image_to_string(f"Outputs/{file_name}_{page_number}_{img_number}.png")
                
                # save OCR text to file
                with open(f"Outputs/{file_name}_{page_number}_{img_number}_OCR.txt", "w") as text_file:
                    text_file.write(imagestring)