from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUiHome(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 550)
        MainWindow.setWindowIcon(QtGui.QIcon('./pictures/ou_logo.jpg'))
        MainWindow.setStyleSheet("background-color: #123456;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setStyleSheet("background-color: white;")
        self.frame1.setGeometry(QtCore.QRect(20, 20, 810, 530))
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")

        self.titleLabel = QtWidgets.QLabel(self.frame1)
        self.titleLabel.setGeometry(QtCore.QRect(30, 30, 741, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")

        self.task = QtWidgets.QPushButton(self.frame1)
        self.task.setGeometry(QtCore.QRect(50, 170, 221, 111))
        self.task.setStyleSheet("background-image : url(./pictures/task.png);")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        self.task.setFont(font)
        self.task.setObjectName("task")

        self.resource = QtWidgets.QPushButton(self.frame1)
        self.resource.setGeometry(QtCore.QRect(290, 170, 221, 111))
        self.resource.setStyleSheet("background-image : url(./pictures/.png);")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        self.resource.setFont(font)
        self.resource.setObjectName("resource")

        self.transport = QtWidgets.QPushButton(self.frame1, clicked=self.transport)
        self.transport.setGeometry(QtCore.QRect(530, 170, 221, 111))
        self.transport.setStyleSheet("background-image : url(./pictures/map.jpg);")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        self.transport.setFont(font)
        self.transport.setObjectName("transport")

        self.booking = QtWidgets.QPushButton(self.frame1)
        self.booking.setGeometry(QtCore.QRect(50, 320, 221, 111))
        self.booking.setStyleSheet("background-image : url(./pictures/booking.png);")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        self.booking.setFont(font)
        self.booking.setObjectName("booking")

        self.food = QtWidgets.QPushButton(self.frame1, clicked=self.food)
        self.food.setGeometry(QtCore.QRect(290, 320, 221, 111))
        self.food.setStyleSheet("background-image : url(./pictures/foodImage.png);")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        self.food.setFont(font)
        self.food.setObjectName("food")

        self.emergency = QtWidgets.QPushButton(self.frame1)
        self.emergency.setGeometry(QtCore.QRect(530, 320, 221, 111))
        self.emergency.setStyleSheet("background-image : url(./pictures/ambulance.png);")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        self.emergency.setFont(font)
        self.emergency.setObjectName("emergency")

        self.line = QtWidgets.QFrame(self.frame1)
        self.line.setGeometry(QtCore.QRect(90, 80, 621, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")

        self.namesLabel = QtWidgets.QLabel(self.frame1)
        self.namesLabel.setGeometry(QtCore.QRect(30, 460, 741, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.namesLabel.setFont(font)
        self.namesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.namesLabel.setObjectName("namesLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def food(self):
        import food
        self.foodWindow = QtWidgets.QMainWindow()
        self.foodUI = food.Ui_FoodManagement()
        self.foodUI.setupUiFood(self.foodWindow)
        MainWindow.hide()
        self.foodWindow.show()

    def transport(self):
        import transport
        self.transportWindow = QtWidgets.QMainWindow()
        self.transportUI = transport.Ui_MainWindow()
        self.transportUI.setupUi(self.transportWindow)
        MainWindow.hide()
        self.transportWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smart City Managment System"))
        self.titleLabel.setText(_translate("MainWindow", "Smart City Management System"))
        self.task.setText(_translate("MainWindow", "Task Scheduler"))
        self.resource.setText(_translate("MainWindow", "Resource Allocation"))
        self.transport.setText(_translate("MainWindow", "Transportation"))
        self.booking.setText(_translate("MainWindow", "Resource Booking"))
        self.food.setText(_translate("MainWindow", "Food Consumption"))
        self.emergency.setText(_translate("MainWindow", "Emergency Services"))
        self.namesLabel.setText(_translate("MainWindow", "Created by: Viljo Wagner, Asad Vakil, Stephen Villagonzalo, "
                                                         "Jurnee Tipton, Denise Rauschendorfer, & Irma Rrushi "))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUiHome(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


