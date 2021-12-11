# 崔浩然
# 时间:2021/12/11 11:40
# 功能
import os
import sys

import traceback
from fenbanClass import *
import requests
from PySide2.QtCore import QObject
from PySide2.QtGui import QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
import picture_rc
from fenbanClass import *
from PySide2.QtWidgets import QApplication, QMessageBox

class FenBan(QObject):
    
    def __init__(self):
        QObject.__init__(self)
        
        # 从 UI 定义中动态 创建一个相应的窗口对象
        self.ui = QUiLoader().load('ui/分班界面.ui')
        self.ui.pushButton.clicked.connect(self.create)
        self.ui.pushButton_2.clicked.connect(self.fen)
        self.ui.pushButton_3.clicked.connect(self.see)
        self.ui.pushButton_4.clicked.connect(self.out)
        
    def create(self):
        create_name_list()
        QMessageBox.information(self.ui, '信息', '生成成功')
        
    def fen(self):
        QMessageBox.information(self.ui, '信息', '分班成功')
        
    def see(self):
        if os.system('分班名单.xlsx') == 0:
            print("成功")
       
    def out(self):
        
        QMessageBox.information(self.ui, '信息', '望子成龙，二十八中')
        sys.exit()
        