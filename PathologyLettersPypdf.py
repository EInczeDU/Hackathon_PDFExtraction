import pandas as pd
import numpy as np
import pypdf


file_name = "File1.pdf"
path_to_pdf = f"PDFs/path/{file_name}"
path_to_output = f"Outputs/Histopathology/{file_name}.csv"

data = pypdf.PdfReader(path_to_pdf).pages
for page in data:
    text = page.extract_text()
    print(text)