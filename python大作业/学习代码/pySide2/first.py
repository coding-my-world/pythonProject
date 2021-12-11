# 崔浩然
# 时间:2021/11/19 19:34
# 功能：第一个pyqt5程序
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox


def handleCalc():  # 统计按钮的点击事件函数
    info = textEdit.toPlainText()  # 获取文本
    # 薪资20000以上和以下的人员名单
    salary_above_20k = ''  # 高于20000
    salary_below_20k = ''  # 低于20000
    for line in info.splitlines():
        if not line.strip():
            continue
        parts = line.split(' ')
        # 去掉列表中的空字符串内容
        parts = [p for p in parts if p]
        name, salary, age = parts
        if int(salary) >= 20000:
            salary_above_20k += name + '\n'
        else:
            salary_below_20k += name + '\n'
    QMessageBox.about(window, "统计结果",
                      f'''薪资20000 以上的有：\n{salary_above_20k}
                      \n薪资20000以下的有：\n{salary_below_20k}''')


app = QApplication([])
window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('薪资统计')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("请输入薪资表")
textEdit.move(10, 25)
textEdit.resize(300, 350)

button = QPushButton('统计', window)
button.move(380, 80)
button.clicked.connect(handleCalc)
window.show()
app.exec_()
