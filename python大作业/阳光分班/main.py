# 崔浩然
# 时间:2021/12/11 9:48
# 功能:分班主函数
import os
import traceback
from fenbanClass import *
import requests
from PySide2.QtCore import QObject
from PySide2.QtGui import QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
import picture_rc
import fenbanClass
from show import *



app = QApplication([])
# os.system('python login.py')  #执行login_main.py文件
Fenban = FenBan()
Fenban.ui.show()
app.exec_()