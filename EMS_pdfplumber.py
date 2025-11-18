import pandas as pd
import numpy as np
import pdfplumber

# Import data
with pdfplumber.open("PDFs/EMS Performance Tracker.pdf") as pdf:
    page = pdf.pages[0] 
    table = page.extract_table()
# In this case there was a single table on the first page. Try .find_tables or .extract_tables in other circumstances
#https://github.com/jsvine/pdfplumber#extracting-tables

# Remove newlines from column headers. Specific to this case
for n, header in enumerate(table[:4]): #Loops through table headers. How many levels of headers is table-specific
    for m, el in enumerate(header): # Loops through individual cells within a row
        if type(el) == str:
            table[n][m] = el.replace("\n", "")

# Combine last two header rows because they should have been the same level
lasttwo = list(zip(table[2], table[3])) # Combines the two lists element-wise
bottomheader = [next((x for x in tup if x is not None), None) for tup in lasttwo] # Squashes elements into first non-null value

# Create headers and rows for final version of table
levels=[table[0], table[1], bottomheader] # Combines all header rows into a single list
cols = pd.MultiIndex.from_arrays(levels) # Transforms header list into a pandas MultiIndex, to be used as header
data = table[4:] # Selects data rows from original extract (4th row and below in this case)

# Create dataframe using data rows and headers
df = pd.DataFrame(table[4:], columns=cols)
df.rename(columns={np.nan:''}, inplace=True) #Replace empty header cells showing up as NaN with an empty string

# Save required subset of data
df.iloc[:, 2:7].to_csv('Outputs/tablefrompdf.csv', index=False) 
# We needed columns 3 til 7, Python indexing starts at 0 and slicing is non-inclusive on the right side