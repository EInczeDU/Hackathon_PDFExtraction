from matplotlib.pyplot import vlines
import pandas as pd
import numpy as np
import pdfplumber

# Import data
tables = dict()
with pdfplumber.open("PDFs/Social Care Dashboard - 20221003.pdf") as pdf:
    for n, page in enumerate(pdf.pages):
        tables[n] = page.extract_tables()

# In this case there was a single table on the first page. Try .find_tables or .extract_tables in other circumstances
# https://github.com/jsvine/pdfplumber#extracting-tables

with pdfplumber.open("PDFs/Social Care Dashboard - 20221003.pdf") as pdf:
    first_page = pdf.pages[7]
    print(first_page.chars[0])


def cleanup(table, hr=1):
    # Remove newlines from column headers. Specific to this case
    for n, header in enumerate(table[:2]): # Loops through table headers. How many levels of headers is table-specific
        for m, el in enumerate(header): # Loops through individual cells within a row
            if type(el) == str:
                table[n][m] = el.replace("\n", "")

    # Combine last two header rows because they should have been the same level
    #lasttwo = list(zip(table[2], table[3])) # Combines the two lists element-wise
    #bottomheader = [next((x for x in tup if x is not None), None) for tup in lasttwo] # Squashes elements into first non-null value

    # Create headers and rows for final version of table
    #levels=[table[0], table[1], bottomheader] # Combines all header rows into a single list
    levels = [table[0], table[1]]

    cols = pd.MultiIndex.from_arrays(levels) # Transforms header list into a pandas MultiIndex, to be used as header
    data = table[hr:] # Selects data rows from original extract (offset by size of header)
    return cols, data


data = list()
for k, v in tables.items():
    for table in v:
        if len(table) > 1:
            cols, rows = cleanup(table)
            data.extend(rows)
            data.extend([np.full(len(table[0]), np.nan)]) #adds a row of "nothing" to separate tables
        else:
            data.extend(table)

# Create dataframe using data rows and headers
df = pd.DataFrame(data, columns=cols)
df.rename(columns={np.nan:''}, inplace=True) # Replace empty header cells showing up as NaN with an empty string

# Save required subset of data
df.iloc[:, 2:7].to_csv('Outputs/tablefrompdf.csv', index=False) 
# We needed columns 3 til 7, Python indexing starts at 0 and slicing is non-inclusive on the right side