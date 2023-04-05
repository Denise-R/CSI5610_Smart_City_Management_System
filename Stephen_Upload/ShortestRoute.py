# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShortestRoute.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ShortestRoute_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 10, 601, 411))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 0, 411, 401))
        self.label.setStyleSheet(u"background-image: url(:/newPrefix/Map.jpg);")
        self.label.setPixmap(QPixmap(u":/newPrefix/Map.jpg"))
        self.label.setScaledContents(True)
        self.label.setTextInteractionFlags(Qt.NoTextInteraction)
        self.comboBox_Start = QComboBox(self.frame)
        self.comboBox_Start.addItem("")
        self.comboBox_Start.addItem("")
        self.comboBox_Start.addItem("")
        self.comboBox_Start.addItem("")
        self.comboBox_Start.addItem("")
        self.comboBox_Start.addItem("")
        self.comboBox_Start.addItem("")
        self.comboBox_Start.addItem("")
        self.comboBox_Start.addItem("")
        self.comboBox_Start.addItem("")
        self.comboBox_Start.addItem("")
        self.comboBox_Start.addItem("")
        self.comboBox_Start.addItem("")
        self.comboBox_Start.addItem("")
        self.comboBox_Start.addItem("")
        self.comboBox_Start.setObjectName(u"comboBox_Start")
        self.comboBox_Start.setGeometry(QRect(10, 30, 161, 41))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 10, 60, 16))
        font = QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 70, 91, 20))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 190, 61, 20))
        self.label_4.setFont(font)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 130, 113, 51))
        self.comboBox_Dest = QComboBox(self.frame)
        self.comboBox_Dest.addItem("")
        self.comboBox_Dest.addItem("")
        self.comboBox_Dest.addItem("")
        self.comboBox_Dest.addItem("")
        self.comboBox_Dest.addItem("")
        self.comboBox_Dest.addItem("")
        self.comboBox_Dest.addItem("")
        self.comboBox_Dest.addItem("")
        self.comboBox_Dest.addItem("")
        self.comboBox_Dest.addItem("")
        self.comboBox_Dest.addItem("")
        self.comboBox_Dest.addItem("")
        self.comboBox_Dest.addItem("")
        self.comboBox_Dest.addItem("")
        self.comboBox_Dest.addItem("")
        self.comboBox_Dest.setObjectName(u"comboBox_Dest")
        self.comboBox_Dest.setGeometry(QRect(10, 90, 161, 41))
        self.tableWidget = QTableWidget(self.frame)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 220, 171, 181))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.comboBox_Start.setItemText(0, QCoreApplication.translate("MainWindow", u"The Shire", None))
        self.comboBox_Start.setItemText(1, QCoreApplication.translate("MainWindow", u"Bree", None))
        self.comboBox_Start.setItemText(2, QCoreApplication.translate("MainWindow", u"RivenDell", None))
        self.comboBox_Start.setItemText(3, QCoreApplication.translate("MainWindow", u"Gundabad", None))
        self.comboBox_Start.setItemText(4, QCoreApplication.translate("MainWindow", u"Mirkwood", None))
        self.comboBox_Start.setItemText(5, QCoreApplication.translate("MainWindow", u"Lake Town", None))
        self.comboBox_Start.setItemText(6, QCoreApplication.translate("MainWindow", u"Erebor", None))
        self.comboBox_Start.setItemText(7, QCoreApplication.translate("MainWindow", u"Lake Town", None))
        self.comboBox_Start.setItemText(8, QCoreApplication.translate("MainWindow", u"Moria", None))
        self.comboBox_Start.setItemText(9, QCoreApplication.translate("MainWindow", u"Isengard", None))
        self.comboBox_Start.setItemText(10, QCoreApplication.translate("MainWindow", u"Helms Deep", None))
        self.comboBox_Start.setItemText(11, QCoreApplication.translate("MainWindow", u"Minas Tirith", None))
        self.comboBox_Start.setItemText(12, QCoreApplication.translate("MainWindow", u"Minas Morgul", None))
        self.comboBox_Start.setItemText(13, QCoreApplication.translate("MainWindow", u"Dead Marshes", None))
        self.comboBox_Start.setItemText(14, QCoreApplication.translate("MainWindow", u"Mount Doom", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Destination", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Route", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.comboBox_Dest.setItemText(0, QCoreApplication.translate("MainWindow", u"The Shire", None))
        self.comboBox_Dest.setItemText(1, QCoreApplication.translate("MainWindow", u"Bree", None))
        self.comboBox_Dest.setItemText(2, QCoreApplication.translate("MainWindow", u"RivenDell", None))
        self.comboBox_Dest.setItemText(3, QCoreApplication.translate("MainWindow", u"Gundabad", None))
        self.comboBox_Dest.setItemText(4, QCoreApplication.translate("MainWindow", u"Mirkwood", None))
        self.comboBox_Dest.setItemText(5, QCoreApplication.translate("MainWindow", u"Lake Town", None))
        self.comboBox_Dest.setItemText(6, QCoreApplication.translate("MainWindow", u"Erebor", None))
        self.comboBox_Dest.setItemText(7, QCoreApplication.translate("MainWindow", u"Lake Town", None))
        self.comboBox_Dest.setItemText(8, QCoreApplication.translate("MainWindow", u"Moria", None))
        self.comboBox_Dest.setItemText(9, QCoreApplication.translate("MainWindow", u"Isengard", None))
        self.comboBox_Dest.setItemText(10, QCoreApplication.translate("MainWindow", u"Helms Deep", None))
        self.comboBox_Dest.setItemText(11, QCoreApplication.translate("MainWindow", u"Minas Tirith", None))
        self.comboBox_Dest.setItemText(12, QCoreApplication.translate("MainWindow", u"Minas Morgul", None))
        self.comboBox_Dest.setItemText(13, QCoreApplication.translate("MainWindow", u"Dead Marshes", None))
        self.comboBox_Dest.setItemText(14, QCoreApplication.translate("MainWindow", u"Mount Doom", None))

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Realms", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Distance", None));
    # retranslateUi

