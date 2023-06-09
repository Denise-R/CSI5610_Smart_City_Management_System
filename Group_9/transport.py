from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import shortestroute as sr

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Transportation Management")
        MainWindow.resize(820, 530)
        MainWindow.setWindowIcon(QtGui.QIcon(':/pictures/ou_logo.jpg'))
        MainWindow.setStyleSheet("background-color: #123456;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(20, 10, 781, 481))
        self.frame1.setStyleSheet("background-color: white;")
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")

        self.label1 = QtWidgets.QLabel(self.frame1)
        self.label1.setGeometry(QtCore.QRect(5, 5, 781, 30))
        self.label1.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)

        self.line = QtWidgets.QFrame(self.frame1)
        self.line.setGeometry(QtCore.QRect(30, 35, 781, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")

        self.label = QtWidgets.QLabel(self.frame1)
        self.label.setGeometry(QtCore.QRect(285, 70, 496, 411))
        self.label.setObjectName("label")
        self.pixmap = QtGui.QPixmap(':/pictures/Map.jpg')
        self.label.setPixmap(self.pixmap)

        self.comboBox_Start = QtWidgets.QComboBox(self.frame1)
        self.comboBox_Start.setGeometry(QtCore.QRect(140, 80, 125, 25))
        self.comboBox_Start.setObjectName("comboBox_Start")
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
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.comboBox_Start.setFont(font)

        self.startLabel = QtWidgets.QLabel(self.frame1)
        self.startLabel.setGeometry(QtCore.QRect(10, 80, 130, 25))
        self.startLabel.setObjectName("startLabel")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setPointSize(12)
        self.startLabel.setFont(font)

        self.destinationLabel = QtWidgets.QLabel(self.frame1)
        self.destinationLabel.setGeometry(QtCore.QRect(10, 130, 130, 25))
        self.destinationLabel.setObjectName("destinationLabel")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setPointSize(12)
        self.destinationLabel.setFont(font)

        self.routeLabel = QtWidgets.QLabel(self.frame1)
        self.routeLabel.setGeometry(QtCore.QRect(10, 260, 61, 20))
        self.routeLabel.setObjectName("routeLabel")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setPointSize(12)
        self.routeLabel.setFont(font)

        self.submitButton = QtWidgets.QPushButton(self.frame1, clicked=self.racecar)
        self.submitButton.setGeometry(QtCore.QRect(30, 180, 215, 51))
        self.submitButton.setObjectName("submitButton")
        self.submitButton.setStyleSheet("background-color: #99A3A4;")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setPointSize(12)
        self.submitButton.setFont(font)

        self.comboBox_Dest = QtWidgets.QComboBox(self.frame1)
        self.comboBox_Dest.setGeometry(QtCore.QRect(140, 130, 125, 25))
        self.comboBox_Dest.setObjectName("comboBox_Dest")
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
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.comboBox_Dest.setFont(font)

        # table widget
        self.tableWidget = QtWidgets.QTableWidget(self.frame1)
        self.tableWidget.setGeometry(QtCore.QRect(10, 290, 260, 181))
        self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QtWidgets.QTableWidgetItem()
        __qtablewidgetitem.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QtWidgets.QTableWidgetItem()
        __qtablewidgetitem1.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Null"))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Null"))
        self.tableWidget.setStyleSheet("border: 1px solid black;")
        self.tableWidget.setObjectName(u"tableWidget")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(7)
        self.tableWidget.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 24))
        self.menubar.setStyleSheet("background-color: white; color: black;")

        self.menuOptions = QtWidgets.QMenu(self.menubar)
        MainWindow.setMenuBar(self.menubar)

        self.help = QtWidgets.QAction(MainWindow)
        self.help.triggered.connect(self.helpPressed)
        self.help.setIcon(QtGui.QIcon('./pictures/question.png'))
        self.menuOptions.addAction(self.help)
        self.menubar.addAction(self.menuOptions.menuAction())
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def homePressed(self):
        import homePage
        self.homeWindow = QtWidgets.QMainWindow()
        self.homeui = homePage.Ui_MainWindow()
        self.homeui.setupUiHome(self.homeWindow)
        self.homeWindow.show()

    def helpPressed(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon(':/pictures/question.png'))
        msg.setWindowTitle("Help: Transportation Management")
        msg.setText("How to use transportation Management window described ...")
        msg.exec_()

    def get_path(self, path):
        pathLength = len(path)
        self.tableWidget.setRowCount(pathLength + 1)
        path.reverse()
        end = path[-1]
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem('0'))
        self.tableWidget.setItem(pathLength - 1, 0, QtWidgets.QTableWidgetItem(end))
        self.tableWidget.setItem(pathLength, 0, QtWidgets.QTableWidgetItem('Total'))
        total = 0
        for i in range(0, pathLength - 1):
            a = path[i]
            b = path[i + 1]
            val = sr.init_graph[a]
            dist = val[b]
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(a))
            self.tableWidget.setItem(i + 1, 1, QtWidgets.QTableWidgetItem(str(dist)))
            total = total + dist
        self.tableWidget.setItem(pathLength, 1, QtWidgets.QTableWidgetItem(str(total)))


    def racecar(self):
        msg = QMessageBox()
        start = self.comboBox_Start.currentText()
        end = self.comboBox_Dest.currentText()
        previous_nodes, shortest_path = sr.dijkstra_algorithm(graph=sr.graph, start_node=start)
        path = sr.print_result(previous_nodes, shortest_path, start_node=start, target_node=end)
        self.get_path(path)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Transportation Management"))
        self.label.setText("")

        self.menuOptions.setTitle(_translate("FoodManagement", "Options"))
        self.help.setText(_translate("FoodManagement", "Help"))

        self.label1.setText(_translate("MainWindow", "Transportation Management"))
        self.comboBox_Start.setItemText(0,  _translate("MainWindow", "The Shire"))
        self.comboBox_Start.setItemText(1,  _translate("MainWindow", "Bree"))
        self.comboBox_Start.setItemText(2,  _translate("MainWindow", "RivenDell"))
        self.comboBox_Start.setItemText(3,  _translate("MainWindow", "Gundabad"))
        self.comboBox_Start.setItemText(4,  _translate("MainWindow", "Mirkwood"))
        self.comboBox_Start.setItemText(5,  _translate("MainWindow", "Erebor"))
        self.comboBox_Start.setItemText(6,  _translate("MainWindow", "Lake Town"))
        self.comboBox_Start.setItemText(7,  _translate("MainWindow", "Dol Guldur"))
        self.comboBox_Start.setItemText(8,  _translate("MainWindow", "Moria"))
        self.comboBox_Start.setItemText(9,  _translate("MainWindow", "Isengard"))
        self.comboBox_Start.setItemText(10, _translate("MainWindow", "Helms Deep"))
        self.comboBox_Start.setItemText(11, _translate("MainWindow", "Minas Tirith"))
        self.comboBox_Start.setItemText(12, _translate("MainWindow", "Minas Morgul"))
        self.comboBox_Start.setItemText(13, _translate("MainWindow", "Dead Marshes"))
        self.comboBox_Start.setItemText(14, _translate("MainWindow", "Mount Doom"))

        self.startLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "Start :", None))
        self.destinationLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "Destination :", None))
        self.routeLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "Route", None))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.comboBox_Dest.setItemText(0, _translate("MainWindow", "The Shire"))
        self.comboBox_Dest.setItemText(1, _translate("MainWindow", "Bree"))
        self.comboBox_Dest.setItemText(2, _translate("MainWindow", "RivenDell"))
        self.comboBox_Dest.setItemText(3, _translate("MainWindow", "Gundabad"))
        self.comboBox_Dest.setItemText(4, _translate("MainWindow", "Mirkwood"))
        self.comboBox_Dest.setItemText(5, _translate("MainWindow", "Erebor"))
        self.comboBox_Dest.setItemText(6, _translate("MainWindow", "Lake Town"))
        self.comboBox_Dest.setItemText(7, _translate("MainWindow", "Dol Guldur"))
        self.comboBox_Dest.setItemText(8, _translate("MainWindow", "Moria"))
        self.comboBox_Dest.setItemText(9, _translate("MainWindow", "Isengard"))
        self.comboBox_Dest.setItemText(10, _translate("MainWindow", "Helms Deep"))
        self.comboBox_Dest.setItemText(11, _translate("MainWindow", "Minas Tirith"))
        self.comboBox_Dest.setItemText(12, _translate("MainWindow", "Minas Morgul"))
        self.comboBox_Dest.setItemText(13, _translate("MainWindow", "Dead Marshes"))
        self.comboBox_Dest.setItemText(14, _translate("MainWindow", "Mount Doom"))

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QtCore.QCoreApplication.translate("MainWindow", u"Realms", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QtCore.QCoreApplication.translate("MainWindow", u"Distance", None));

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
