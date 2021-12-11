# 崔浩然
# 时间:2021/11/17 17:21
# 功能：用pycharm创建excel表格
from openpyxl import Workbook

wb = Workbook()  # 创建一个Workbook对象
ws = wb.active
ws.title = 'qq'  # 设置该工作表的的标题为qq

ws.append([123,456,789,0])  #这样增加的是一横排资料
ws.append([123,456,789,0])  #这样增加的是一横排资料
ws.append([123,456,789,0])  #这样增加的是一横排资料

wb.save('new_excel.xlsx')  # 保存工作表
