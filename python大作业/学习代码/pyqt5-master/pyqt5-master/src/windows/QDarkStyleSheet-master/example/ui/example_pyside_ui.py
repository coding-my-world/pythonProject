# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example.ui'
#
# Created: Sun Nov 27 13:09:31 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1068, 824)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.East)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.toolBox = QtGui.QToolBox(self.groupBox)
        self.toolBox.setObjectName("toolBox")
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 98, 44))
        self.page.setObjectName("page")
        self.gridLayout_4 = QtGui.QGridLayout(self.page)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit = QtGui.QLineEdit(self.page)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 697, 210))
        self.page_2.setObjectName("page_2")
        self.gridLayout_5 = QtGui.QGridLayout(self.page_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.listWidget = QtGui.QListWidget(self.page_2)
        self.listWidget.setObjectName("listWidget")
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        self.gridLayout_5.addWidget(self.listWidget, 0, 0, 1, 1)
        self.toolBox.addItem(self.page_2, "")
        self.verticalLayout_3.addWidget(self.toolBox)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.tabWidget_2 = QtGui.QTabWidget(self.tab)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.checkableButton = QtGui.QPushButton(self.tab_3)
        self.checkableButton.setCheckable(True)
        self.checkableButton.setChecked(True)
        self.checkableButton.setObjectName("checkableButton")
        self.gridLayout_6.addWidget(self.checkableButton, 1, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.tab_3)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.tab_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_6.addWidget(self.pushButton_5, 2, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tableWidget = QtGui.QTableWidget(self.tab_5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(4)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.gridLayout_7.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.dateEdit = QtGui.QDateEdit(self.tab)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.radioButton = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_4.addWidget(self.radioButton)
        self.checkBox = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_4.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_2)
        self.checkBox_2.setTristate(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_4.addWidget(self.checkBox_2)
        self.treeWidget = QtGui.QTreeWidget(self.groupBox_2)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        self.verticalLayout_4.addWidget(self.treeWidget)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.bt_delay_popup = QtGui.QToolButton(self.centralwidget)
        self.bt_delay_popup.setObjectName("bt_delay_popup")
        self.horizontalLayout.addWidget(self.bt_delay_popup)
        self.bt_instant_popup = QtGui.QToolButton(self.centralwidget)
        self.bt_instant_popup.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.bt_instant_popup.setObjectName("bt_instant_popup")
        self.horizontalLayout.addWidget(self.bt_instant_popup)
        self.bt_menu_button_popup = QtGui.QToolButton(self.centralwidget)
        self.bt_menu_button_popup.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.bt_menu_button_popup.setObjectName("bt_menu_button_popup")
        self.horizontalLayout.addWidget(self.bt_menu_button_popup)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout.addWidget(self.doubleSpinBox)
        self.toolButton = QtGui.QToolButton(self.centralwidget)
        self.toolButton.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1068, 23))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuSubmenu_2 = QtGui.QMenu(self.menuMenu)
        self.menuSubmenu_2.setObjectName("menuSubmenu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget1 = QtGui.QDockWidget(MainWindow)
        self.dockWidget1.setObjectName("dockWidget1")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtGui.QComboBox(self.dockWidgetContents)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalSlider = QtGui.QSlider(self.dockWidgetContents)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.textEdit = QtGui.QTextEdit(self.dockWidgetContents)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.line = QtGui.QFrame(self.dockWidgetContents)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.progressBar = QtGui.QProgressBar(self.dockWidgetContents)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.frame = QtGui.QFrame(self.dockWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(0, 100))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.verticalLayout_2.addWidget(self.frame)
        self.dockWidget1.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget1)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidget2 = QtGui.QDockWidget(MainWindow)
        self.dockWidget2.setObjectName("dockWidget2")
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout_3 = QtGui.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalSlider = QtGui.QSlider(self.dockWidgetContents_2)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout_3.addWidget(self.verticalSlider, 0, 0, 1, 1)
        self.dockWidget2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget2)
        self.actionAction = QtGui.QAction(MainWindow)
        self.actionAction.setObjectName("actionAction")
        self.actionSub_menu = QtGui.QAction(MainWindow)
        self.actionSub_menu.setObjectName("actionSub_menu")
        self.actionAction_C = QtGui.QAction(MainWindow)
        self.actionAction_C.setObjectName("actionAction_C")
        self.menuSubmenu_2.addAction(self.actionSub_menu)
        self.menuSubmenu_2.addAction(self.actionAction_C)
        self.menuMenu.addAction(self.actionAction)
        self.menuMenu.addAction(self.menuSubmenu_2.menuAction())
        self.menubar.addAction(self.menuMenu.menuAction())
        self.toolBar.addAction(self.actionAction)
        self.toolBar.addAction(self.actionSub_menu)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton, self.checkableButton)
        MainWindow.setTabOrder(self.checkableButton, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.tabWidget_2)
        MainWindow.setTabOrder(self.tabWidget_2, self.tableWidget)
        MainWindow.setTabOrder(self.tableWidget, self.radioButton)
        MainWindow.setTabOrder(self.radioButton, self.checkBox)
        MainWindow.setTabOrder(self.checkBox, self.checkBox_2)
        MainWindow.setTabOrder(self.checkBox_2, self.treeWidget)
        MainWindow.setTabOrder(self.treeWidget, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.bt_delay_popup)
        MainWindow.setTabOrder(self.bt_delay_popup, self.bt_instant_popup)
        MainWindow.setTabOrder(self.bt_instant_popup, self.bt_menu_button_popup)
        MainWindow.setTabOrder(self.bt_menu_button_popup, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.doubleSpinBox)
        MainWindow.setTabOrder(self.doubleSpinBox, self.toolButton)
        MainWindow.setTabOrder(self.toolButton, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.horizontalSlider)
        MainWindow.setTabOrder(self.horizontalSlider, self.textEdit)
        MainWindow.setTabOrder(self.textEdit, self.verticalSlider)
        MainWindow.setTabOrder(self.verticalSlider, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.listWidget)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "ToolBox", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QtGui.QApplication.translate("MainWindow", "Page 1", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.item(0).setText(QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(1).setText(QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(2).setText(QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(3).setText(QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(4).setText(QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(5).setText(QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(6).setText(QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(7).setText(QtGui.QApplication.translate("MainWindow", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QtGui.QApplication.translate("MainWindow", "Page 2", None, QtGui.QApplication.UnicodeUTF8))
        self.checkableButton.setText(QtGui.QApplication.translate("MainWindow", "Checkable button", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.verticalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "New Row", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "New Column", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "New Column 2", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QtGui.QApplication.translate("MainWindow", "Page", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("MainWindow", "RadioB&utton", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "CheckBox", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("MainWindow", "CheckBox Tristate", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "qdz", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "qzd", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.topLevelItem(1).setText(0, QtGui.QApplication.translate("MainWindow", "effefe", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_delay_popup.setText(QtGui.QApplication.translate("MainWindow", "Delayed popup  ", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_instant_popup.setText(QtGui.QApplication.translate("MainWindow", "Instant popup", None, QtGui.QApplication.UnicodeUTF8))
        self.bt_menu_button_popup.setText(QtGui.QApplication.translate("MainWindow", "MenuButtonPopup", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("MainWindow", "&Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSubmenu_2.setTitle(QtGui.QApplication.translate("MainWindow", "&Submenu 2", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget1.setWindowTitle(QtGui.QApplication.translate("MainWindow", "&Dock widget 1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Item 0", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Item 2", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget2.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Dock widget &2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAction.setText(QtGui.QApplication.translate("MainWindow", "&Action", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSub_menu.setText(QtGui.QApplication.translate("MainWindow", "&Action B", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSub_menu.setToolTip(QtGui.QApplication.translate("MainWindow", "submenu", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAction_C.setText(QtGui.QApplication.translate("MainWindow", "Action &C", None, QtGui.QApplication.UnicodeUTF8))

