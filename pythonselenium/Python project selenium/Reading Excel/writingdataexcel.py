import openpyxl
from openpyxl.cell import cell

file = "C:\\Users\\Shashank L\\Downloads\\data.xlsx"
workbook = openpyxl.load_workbook(file)
sheet = workbook.active #or sheet = workbook["Data"] -->get active sheet from excel

for r in range(1,6):
    for c in range(1,4):
        sheet.cell(r,c).value="Welcome"

workbook.save(file)
