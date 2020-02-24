import xlsxwriter

workbook = xlsxwriter.Workbook("demo.xlsx")
worksheet = workbook.add_worksheet()

# 设置列宽
worksheet.set_column("A:A", 20)

# 设置格式
bold = workbook.add_format({"bold": True})

# 设置单元个格式
worksheet.write("A1", "Hello")

# 设置格式的单元格
worksheet.write("A2", "World")

# 写一些数字， 用行列标识
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456, bold)

# 关闭文件流
workbook.close()
