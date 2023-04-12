from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from typing import List
import pictures.pictures_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(679, 430)
        MainWindow.setWindowIcon(QtGui.QIcon('./pictures/ou_logo.jpg'))
        MainWindow.setStyleSheet("background-color: #123456;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(19, 19, 641, 365))
        self.frame1.setStyleSheet("background-color: white;")
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")

        self.label = QtWidgets.QLabel(self.frame1)
        self.label.setGeometry(QtCore.QRect(5, 5, 641, 30))
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.line = QtWidgets.QFrame(self.frame1)
        self.line.setGeometry(QtCore.QRect(30, 35, 581, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")

        self.calendarLabel = QtWidgets.QLabel(self.frame1)
        self.calendarLabel.setObjectName(u"calendarLabel")
        self.calendarLabel.setGeometry(QtCore.QRect(30, 70, 390, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setPointSize(10)
        self.calendarLabel.setFont(font)
        self.calendarLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.calendarline = QtWidgets.QFrame(self.frame1)
        self.calendarline.setGeometry(QtCore.QRect(70, 95, 310, 5))
        self.calendarline.setFrameShadow(QtWidgets.QFrame.Plain)
        self.calendarline.setLineWidth(2)
        self.calendarline.setFrameShape(QtWidgets.QFrame.HLine)
        self.calendarline.setObjectName("calendarline")

        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame1)
        self.calendarWidget.setGeometry(QtCore.QRect(30, 110, 390, 215))
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setStyleSheet("background-color: gray; border: 1px solid black;")
        #self.calendarWidget.selectedDate()
        #self.calendarWidget.clicked[QtCore.QDate].connect(self.showDate)

        self.resourceLabel = QtWidgets.QLabel(self.frame1)
        self.resourceLabel.setObjectName(u"resourceLabel")
        self.resourceLabel.setGeometry(QtCore.QRect(450, 110, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setPointSize(10)
        self.resourceLabel.setFont(font)

        self.comboBox = QtWidgets.QComboBox(self.frame1)
        self.comboBox.setGeometry(QtCore.QRect(450, 150, 172, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.comboBox.setFont(font)

        self.label4 = QtWidgets.QLabel(self.frame1)
        self.label4.setObjectName(u"label4")
        self.label4.setGeometry(QtCore.QRect(450, 230, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setPointSize(10)
        self.label4.setFont(font)

        self.spinBox = QtWidgets.QSpinBox(self.frame1)
        self.spinBox.setGeometry(QtCore.QRect(580, 235, 42, 20))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(24)
        self.spinBox.setObjectName("spinBox")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.spinBox.setFont(font)

        self.submitButton = QtWidgets.QPushButton(self.frame1, clicked=self.book)
        self.submitButton.setGeometry(QtCore.QRect(450, 280, 172, 32))
        self.submitButton.setObjectName("btn_book_resource")
        self.submitButton.setStyleSheet("background-color: #99A3A4;")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setPointSize(12)
        self.submitButton.setFont(font)


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
        msg.setWindowIcon(QtGui.QIcon('./pictures/question.png'))
        msg.setWindowTitle("Help: Resource Booking Management")
        msg.setText("How to use Resource Booking Management window described ...")
        msg.exec_()

    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # implementing scan algorithm

        # initiate results list
        results = [0] * n
        # initiate empty list for flight and seats
        flights = []

        for (i, j, k) in bookings:
            # append the start(i)/end(j) (inclusive), and corresponding seats (k)
            flights.append((i - 1, k))
            flights.append((j, -k))
        # print(flights)
        # sort the flights list
        flights.sort()
        # print(flights)
        for flight in flights:
            # if flights surpasses the length of n
            if flight[0] >= n:
                continue
            # else
            results[flight[0]] += flight[1]

        # prefix sum
        for i in range(1, n):
            results[i] += results[i - 1]
        return results

    def book(self):
        msg = QMessageBox()
        date = self.calendarWidget.selectedDate()
        strDate = date.toString()
        resource = self.comboBox.currentText()
        amount = self.spinBox.value()
        list = self.resourceDict[resource]
        x = str(self.corpFlightBookings(list, amount))[1:-1]
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('./pictures/question.png'))
        msg.setWindowTitle("Resource Booking Management")
        msg.setText("The date needed is : " + strDate +
                    "\n The resource requested is: " + resource + "\n The number of hours requested is: " + str(amount)
                    + "\n\nThe total number of resource(es) reserved at each location is: " + x)
        msg.exec_()

    resourceDict = {
            "Public Bus": [[1,2,10],[2,3,20],[2,5,25]],
            "Vehicle": [[1,2,10],[2,2,15]],
            "Conference Room": [[1,2,6],[2,3,12],[2,4,22],[2,5,6]],
            "Book":  [[1,2,10],[2,3,30],[3,6,44],[2,4,5],[4,5,7]]
        }

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Resource Booking Management"))
        self.menuOptions.setTitle(_translate("FoodManagement", "Options"))
        self.help.setText(_translate("FoodManagement", "Help"))
        self.label.setText(_translate("MainWindow", "Resource Booking Management"))
        self.resourceLabel.setText(QtCore.QCoreApplication.translate("MainWindow", u"Select Resource:", None))
        self.calendarLabel.setText(QtCore.QCoreApplication.translate("MainWindow", u"Select Day(s)", None))
        self.label4.setText(QtCore.QCoreApplication.translate("MainWindow", u"Hour(s) needed: ", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "Public Bus"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Vehicle"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Conference Room"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Book"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
