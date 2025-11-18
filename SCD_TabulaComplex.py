import pandas as pd
import numpy as np
import tabula

############################ Comprehensive method #######################################
############################ PAGE 8 #######################################
tables = tabula.read_pdf("PDFs/Social Care Dashboard - 20221003.pdf",
                        pages="8", multiple_tables=True,
                        stream=True,
                        area='right')
tables[0]

title8 = tables[0].loc[0,'Power BI Desktop']

df = tables[0][['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 5']]
df.dropna(how='all', inplace=True)

headerrows = list(zip(df.iloc[0], df.iloc[1], df.iloc[2], df.iloc[3])) # Combines the lists element-wise
headerrows[0] = tuple([x for x in headerrows[0] if isinstance(x,str)])
header = [' '.join(tup) for tup in headerrows] # Squashes elements into first non-null value

df.columns = header
df8 = df[4:]
df8


############################ PAGE 9 #######################################
tables = tabula.read_pdf("PDFs/Social Care Dashboard - 20221003.pdf",
                        pages="9", multiple_tables=True,
                        stream=True,
                        area='right')
tables[0]

title9 = tables[0].loc[0,'Power BI Desktop']

df = tables[0][['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 3', 'Unnamed: 4']]
df.dropna(how='all', inplace=True)

nrows = 7
headerrows = list(zip(df.iloc[0], df.iloc[1], df.iloc[2], df.iloc[3], df.iloc[4], df.iloc[5], df.iloc[6])) # Combines the lists element-wise
headerrows[0] = tuple([x for x in headerrows[0] if isinstance(x,str)])
headerrows[3] = tuple([x for x in headerrows[0] if isinstance(x,str)])
header = [' '.join(tup) for tup in headerrows] # Squashes elements into first non-null value

df.columns = header
df9 = df[7:]
df9

############################ PAGE 10 #######################################
tables = tabula.read_pdf("PDFs/Social Care Dashboard - 20221003.pdf",
                        pages="10", multiple_tables=True,
                        stream=True,
                        area='right')
tables[0]

title10 = tables[0].loc[0,'Power BI Desktop']

df = tables[0][['Power BI Desktop', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']]
df.dropna(how='all', inplace=True)
df = df[1:-1]
df.iloc[2,0] = np.nan
df['Power BI Desktop'] = df['Power BI Desktop'].str.replace('\d+', '')
df['Unnamed: 1'] = df['Unnamed: 1'].combine_first(df['Unnamed: 2'])
df.drop(columns='Unnamed: 2', inplace=True)
df

headerrows = list(zip(df.iloc[0], df.iloc[1], df.iloc[2], df.iloc[3]
                    , df.iloc[4], df.iloc[5], df.iloc[6], df.iloc[7])) # Combines the lists element-wise
nrows = len(headerrows[0])
for n, headerrow in enumerate(headerrows):
    headerrows[n] = tuple([x for x in headerrow if isinstance(x,str)])

header = [' '.join(tup) for tup in headerrows] # Squashes elements into first non-null value

df.columns = header
df10 = df[nrows:]
df10


############################ PAGE 12 #######################################
tables = tabula.read_pdf("PDFs/Social Care Dashboard - 20221003.pdf",
                        pages="12", multiple_tables=False,
                        stream=True,
                        area=(9, 65, 92, 100), relative_area=True #top left bottom right
                        )
tables[0]




tables = tabula.read_pdf("PDFs/Social Care Dashboard - 20221003.pdf",
                        pages="12", multiple_tables=False,
                        stream=True,
                        area=(9, 65, 92, 100), relative_area=True #top left bottom right
                        )
tables[0]
title12 = 'REABLEMENT'

df = tables[0].drop(columns='Unnamed: 2')
df = df.T.reset_index().T

nrows = 5
headerrows = list(zip(df.iloc[0], df.iloc[1], df.iloc[2], df.iloc[3], df.iloc[4])) # Combines the lists element-wise
for n, headerrow in enumerate(headerrows):
    headerrows[n] = tuple([x for x in headerrow if isinstance(x,str)])

header = [' '.join(tup) for tup in headerrows] # Squashes elements into first non-null value


df.columns = header
df12 = df[nrows:]
df12


############################ PAGE 18 #######################################
tables = tabula.read_pdf("PDFs/Social Care Dashboard - 20221003.pdf",
                        pages="18", multiple_tables=True,
                        stream=True,
                        area='right')
tables[0]

title18 = tables[0].loc[0,'Power BI Desktop']

df = tables[0][['Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10']]
df.dropna(how='all', inplace=True)
nrows = 2
df.iloc[1:2,0] = np.nan
df['Unnamed: 9'] = df['Unnamed: 9'].combine_first(df['Unnamed: 10'])
df.drop(columns='Unnamed: 10', inplace=True)
df

headerrows = list(zip(df.iloc[0], df.iloc[1])) # Combines the lists element-wise
for n, headerrow in enumerate(headerrows):
    headerrows[n] = tuple([x for x in headerrow if isinstance(x,str)])

header = [' '.join(tup) for tup in headerrows] # Squashes elements into first non-null value


df.columns = header
df18 = df[nrows:]
df18.iloc[3,1] = 11.53
df18



############################ PAGE 20 #######################################
tables = tabula.read_pdf("PDFs/Social Care Dashboard - 20221003.pdf",
                        pages="20", multiple_tables=True,
                        stream=True,
                        area='right')
tables[0]

title20 = tables[0].loc[0,'Power BI Desktop']

df = tables[0][['Unnamed: 10', 'Unnamed: 11']]
df.dropna(how='all', inplace=True)
nrows = 2
df.iloc[1:2,0] = np.nan

headerrows = list(zip(df.iloc[0], df.iloc[1])) # Combines the lists element-wise
for n, headerrow in enumerate(headerrows):
    headerrows[n] = tuple([x for x in headerrow if isinstance(x,str)])

header = [' '.join(tup) for tup in headerrows] # Squashes elements into first non-null value


df.columns = header
df20 = df[nrows:]
df20


############################ Simplified method #######################################
# Similar pages (same exact settings work):
# 8, 14
tables = tabula.read_pdf("PDFs/Social Care Dashboard - 20221003.pdf",
                        pages="8,14", multiple_tables=True,
                        stream=True,
                        pandas_options={'header': None},
                        area=(9, 68, 92, 100), relative_area=True #top left bottom right
                        )
tables[1]


# 9, 10
tables = tabula.read_pdf("PDFs/Social Care Dashboard - 20221003.pdf",
                        pages="9,10", multiple_tables=True,
                        stream=True,
                        pandas_options={'header': None},
                        area=(9, 63, 92, 100), relative_area=True #top left bottom right
                        )
tables[0]


# 11, 12
tables = tabula.read_pdf("PDFs/Social Care Dashboard - 20221003.pdf",
                        pages="11-12", multiple_tables=True,
                        stream=True,
                        pandas_options={'header': None},
                        area=(9, 65, 92, 100), relative_area=True #top left bottom right
                        )
tables[0]

# 15, 16 Do not come out properly. Numbers are joined to the first column
tables = tabula.read_pdf("PDFs/Social Care Dashboard - 20221003.pdf",
                        pages="15,16", multiple_tables=True,
                        stream=True,
                        pandas_options={'header': None},
                        area=(9, 62, 92, 100), relative_area=True #top left bottom right
                        )
tables[0]


# 18, 20
tables = tabula.read_pdf("PDFs/Social Care Dashboard - 20221003.pdf",
                        pages="20", multiple_tables=True,
                        stream=True,
                        lattice=False,
                        pandas_options={'header': None},
                        area=(9, 76, 92, 100), relative_area=True #top left bottom right
                        )
tables[0]

# 19
tables = tabula.read_pdf("PDFs/Social Care Dashboard - 20221003.pdf",
                        pages="19", multiple_tables=True,
                        stream=True,
                        lattice=False,
                        pandas_options={'header': None},
                        area=(14, 75, 92, 100), relative_area=True #top left bottom right
                        )
tables[0]



with pd.ExcelWriter('Outputs/Social Care Dashboard.xlsx') as writer:  
    df8.to_excel(writer, sheet_name=title8)
    df9.to_excel(writer, sheet_name=title9)
    df10.to_excel(writer, sheet_name=title10)
    df11.to_excel(writer, sheet_name=title11)
    df12.to_excel(writer, sheet_name=title12)
    df14.to_excel(writer, sheet_name=title14)
    df18.to_excel(writer, sheet_name=title18)
    df19.to_excel(writer, sheet_name=title19)
    df20.to_excel(writer, sheet_name=title20)


# If appending to existing/modified workbook
#with pd.ExcelWriter('Outputs/TablesFromPDFs/Social Care Dashboard.xlsx',
#                    mode='a') as writer:  
#    df12.to_excel(writer, sheet_name=title12)

