import xlrd
import matplotlib.pyplot as plt
import numpy as np

# 打开文件
data = xlrd.open_workbook(r'testExcelData.xlsx')

# 获取表格数目
nums = len(data.sheets())
for i in range(nums):
    # 根据sheet顺序打开sheet
    sheet1 = data.sheets()[i]

# 根据sheet名称获取
sheet2 = data.sheet_by_name('Sheet1')
# 获取sheet（工作表）行（row）、列（col）数
nrows = sheet2.nrows  # 行
ncols = sheet2.ncols  # 列

x_mat = []
y_mat = []

for i in range(nrows):
    print(sheet2.row_values(i))
    x_mat.append(sheet2.row_values(i)[0])
    y_mat.append(sheet2.row_values(i)[1])

# print(x_mat)
# print(y_mat)

plt.scatter(x_mat, y_mat)
for x, y in zip(x_mat, y_mat):
    plt.text(x, y, (x, y), ha="center", va="bottom", fontsize=10)
plt.show()