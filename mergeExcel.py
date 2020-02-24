import xlrd
import xlsxwriter
import os

root = os.path.abspath('./files')

files_names = os.listdir('./files')
source_xls = []
for filename in files_names:
    tmp = os.path.join(root, filename)
    source_xls.append(tmp)

print(source_xls)
target_xls = r"D:\PythonProjects\mergeExcel\result.xlsx"



data = []
for i in source_xls:
    wb = xlrd.open_workbook(i)
    for sheet in wb.sheets():
        for rownum in range(sheet.nrows):
            data.append(sheet.row_values(rownum))
print(data)

# 写入数据
workbook = xlsxwriter.Workbook(target_xls)
worksheet = workbook.add_worksheet()
font = workbook.add_format({"font_size": 14})
for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.write(i, j, data[i][j], font)

workbook.close()
