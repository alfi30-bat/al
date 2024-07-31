from docx2python import docx2python

from pypdf import PdfReader
from openpyxl import load_workbook

# Load the existing workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

def extract_pages(file_path):
    reader = PdfReader(file_path)
    pages = []
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        text = page.extract_text()
        #pages.append({"page_no": i + 1, "page_text": text})
        pages.append({"A": text})# change column while entering next chap
    return pages

# Example usage
file_path = 'E:/ktg brisk.pdf'
#pages = extract_pages(file_path)
#for page in pages:
   #ws.append(page)




#
# Save the workbook
wb.save("sample.xlsx")

import pandas as pd
p=0
conte=[]

#df=pd.read_excel("sample.xlsx",  usecols='heat', nrows=30, header=None, names=["Value"]).iloc[1]["Value"]#setting name for column. then taking value
df=pd.read_excel("sample.xlsx")
conte= df['heat'].tolist()
print(len(df['heat'].tolist()))
        

