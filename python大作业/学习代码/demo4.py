# 崔浩然
# 时间:2021/11/17 17:53
# 功能：插入横排竖排以及移动
from openpyxl import load_workbook

wb = load_workbook("new_excel.xlsx")
ws = wb.active

# #插入和删除
# ws.insert_rows(7)  # 在第7行插入一行
# ws.insert_rows(7, 3)  # 从第7行开始插入3行
# ws.insert_cols(3)  # 在第3列处插入空白列一列
# ws.insert_cols(3, 3)  # 从第3列处插入空白列3列
# ws.delete_row(2)  # 删除第二列
# ws.delete_row(2, 6)  # 从第二行开始删除6行
# ws.delete_cols(5)  # 删除第五列
# ws.delete_cols(5, 3)  # 从第五列开始删除三列

#移动
ws.move_range("A2:D6",10,2,True)  # 把A1到D2范围的单元格向下移10格，向右移2格，可以为负，即向左和向上移动

wb.save('new_excel.xlsx')  # 保存工作表
