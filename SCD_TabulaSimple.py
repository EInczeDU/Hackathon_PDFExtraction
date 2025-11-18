import pandas as pd
import numpy as np
import tabula


############################ Simplified method #######################################
path_to_pdf = "PDFs/Social Care Dashboard - 20221003.pdf"
path_to_output = "Outputs/TablesFromPDF.xlsx"

title8 = "ADULT SERVICES ACTIVITY"
title9= "ADULT ASSESSMENTS"
title10 = "RESIDENTIAL CARE"
title11 = "CARE AT HOME"
title12 = "REABLEMENT"
title14 = "CHILDREN'S SERVICES STATUS"
title18 = "ABSENCE"
title19 = "CARE HOME SUMMARY"
title20 = "CARE HOMES"

# Similar pages (same exact settings work):
# 8, 14
tables = tabula.read_pdf(path_to_pdf,
                        pages="8,14", multiple_tables=True,
                        stream=True,
                        pandas_options={'header': None},
                        area=(9, 68, 92, 100), relative_area=True #top left bottom right
                        )
df8 = tables[0]
df14 = tables[1]

# 9, 10
tables = tabula.read_pdf(path_to_pdf,
                        pages="9,10", multiple_tables=True,
                        stream=True,
                        pandas_options={'header': None},
                        area=(9, 63, 92, 100), relative_area=True #top left bottom right
                        )
df9 = tables[0]
df10 = tables[1]

# 11, 12
tables = tabula.read_pdf(path_to_pdf,
                        pages="11-12", multiple_tables=True,
                        stream=True,
                        pandas_options={'header': None},
                        area=(9, 65, 92, 100), relative_area=True #top left bottom right
                        )
df11 = tables[0]
df12 = tables[1]

# 15, 16 Do not come out properly. Numbers are joined to the first column
tables = tabula.read_pdf(path_to_pdf,
                        pages="15,16", multiple_tables=True,
                        stream=True,
                        pandas_options={'header': None},
                        area=(9, 62, 92, 100), relative_area=True #top left bottom right
                        )
#tables[0]


# 18, 20
tables = tabula.read_pdf(path_to_pdf,
                        pages="18,20", multiple_tables=True,
                        stream=True,
                        lattice=False,
                        pandas_options={'header': None},
                        area=(9, 76, 92, 100), relative_area=True #top left bottom right
                        )
df18 = tables[0]
df20 = tables[1]

# 19
tables = tabula.read_pdf(path_to_pdf,
                        pages="19", multiple_tables=True,
                        stream=True,
                        lattice=False,
                        pandas_options={'header': None},
                        area=(14, 75, 92, 100), relative_area=True #top left bottom right
                        )
df19 = tables[0]


with pd.ExcelWriter(path_to_output) as writer:  
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

