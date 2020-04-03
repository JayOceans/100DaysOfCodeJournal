# daily work

import openpyxl as xl

wb = xl.load_workbook("store.xlsx")

sheet = wb["Sheet1"]

cell = sheet["a1"]
cell = sheet.cell(1, 1)

print(cell.values)
