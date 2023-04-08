from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime, timedelta




class Ui_FoodManagement(object):
    def setupUiFood(self, FoodManagement):
        FoodManagement.setObjectName("FoodManagement")
        FoodManagement.resize(502, 731)
        FoodManagement.setWindowIcon(QtGui.QIcon('./pictures/ou_logo.jpg'))
        FoodManagement.setStyleSheet("background-color: #123456;")

        self.centralwidget = QtWidgets.QWidget(FoodManagement)
        self.centralwidget.setObjectName("centralwidget")

        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(19, 19, 461, 661))
        self.frame1.setStyleSheet("background-color: white;")
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")

        self.titleLabel = QtWidgets.QLabel(self.frame1)
        self.titleLabel.setGeometry(QtCore.QRect(0, -1, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")

        self.line = QtWidgets.QFrame(self.frame1)
        self.line.setGeometry(QtCore.QRect(10, 40, 441, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")

        self.entryLabel = QtWidgets.QLabel(self.frame1)
        self.entryLabel.setGeometry(QtCore.QRect(30, 90, 401, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.entryLabel.setFont(font)
        self.entryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.entryLabel.setObjectName("entryLabel")

        self.outputLabel = QtWidgets.QLabel(self.frame1)
        self.outputLabel.setGeometry(QtCore.QRect(30, 130, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setStyleSheet("background-color: white; border: 1px solid black;")
        self.outputLabel.setText("")
        self.outputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.outputLabel.setObjectName("outputLabel")
        FoodManagement.setCentralWidget(self.centralwidget)

        self.button0 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("0"))
        self.button0.setGeometry(QtCore.QRect(20, 480, 278, 88))
        self.button0.setStyleSheet("background-color: white; border: 1px solid black;")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.button0.setFont(font)
        self.button0.setObjectName("button0")

        self.button1 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("1"))
        self.button1.setGeometry(QtCore.QRect(20, 390, 138, 88))
        self.button1.setStyleSheet("background-color: white; border: 1px solid black;")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")

        self.button2 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("2"))
        self.button2.setGeometry(QtCore.QRect(160, 390, 138, 88))
        self.button2.setStyleSheet("background-color: white; border: 1px solid black;")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.button2.setFont(font)
        self.button2.setObjectName("button2")

        self.button3 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("3"))
        self.button3.setGeometry(QtCore.QRect(300, 390, 138, 88))
        self.button3.setStyleSheet("background-color: white; border: 1px solid black;")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.button3.setFont(font)
        self.button3.setObjectName("button3")

        self.button4 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("4"))
        self.button4.setGeometry(QtCore.QRect(20, 300, 138, 88))
        self.button4.setStyleSheet("background-color: white; border: 1px solid black;")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.button4.setFont(font)
        self.button4.setObjectName("button4")

        self.button5 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("5"))
        self.button5.setGeometry(QtCore.QRect(160, 300, 138, 88))
        self.button5.setStyleSheet("background-color: white; border: 1px solid black;")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.button5.setFont(font)
        self.button5.setObjectName("button5")

        self.button6 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("6"))
        self.button6.setGeometry(QtCore.QRect(300, 300, 138, 88))
        self.button6.setStyleSheet("background-color: white; border: 1px solid black;")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.button6.setFont(font)
        self.button6.setObjectName("button6")

        self.button7 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("7"))
        self.button7.setGeometry(QtCore.QRect(20, 210, 138, 88))
        self.button7.setStyleSheet("background-color: white; border: 1px solid black;")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.button7.setFont(font)
        self.button7.setObjectName("button7")

        self.button8 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("8"))
        self.button8.setGeometry(QtCore.QRect(160, 210, 138, 88))
        self.button8.setStyleSheet("background-color: white; border: 1px solid black;")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.button8.setFont(font)
        self.button8.setObjectName("button8")

        self.button9 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("9"))
        self.button9.setGeometry(QtCore.QRect(300, 210, 138, 88))
        self.button9.setStyleSheet("background-color: white; border: 1px solid black;")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.button9.setFont(font)
        self.button9.setObjectName("button9")

        self.buttonClear = QtWidgets.QPushButton(self.frame1, clicked=self.clear)
        self.buttonClear.setGeometry(QtCore.QRect(300, 480, 138, 88))
        self.buttonClear.setStyleSheet("background-color: white; border: 1px solid black;")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.buttonClear.setFont(font)
        self.buttonClear.setObjectName("buttonClear")

        self.buttonSubmit = QtWidgets.QPushButton(self.frame1, clicked=self.popup)
        self.buttonSubmit.setGeometry(QtCore.QRect(70, 590, 320, 50))
        self.buttonSubmit.setStyleSheet("background-color: white; border: 1px solid black;")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.buttonSubmit.setFont(font)
        self.buttonSubmit.setObjectName("buttonSubmit")

        self.menubar = QtWidgets.QMenuBar(FoodManagement)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 26))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet("background-color: white; color: black;")

        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        FoodManagement.setMenuBar(self.menubar)

        self.home = QtWidgets.QAction(FoodManagement)
        self.home.setObjectName("home")
        self.help = QtWidgets.QAction(FoodManagement)
        self.help.setObjectName("help")
        self.menuOptions.addAction(self.home)
        self.home.triggered.connect(self.homePressed)
        self.home.setIcon(QtGui.QIcon('./pictures/home.png'))
        self.help.triggered.connect(self.helpPressed)
        self.help.setIcon(QtGui.QIcon('./pictures/question.png'))
        self.menuOptions.addAction(self.help)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(FoodManagement)
        QtCore.QMetaObject.connectSlotsByName(FoodManagement)


    def clear(self):
        self.outputLabel.setText("")

    def enterNums(self, number):
        current = self.outputLabel.text()
        self.outputLabel.setText("")
        self.outputLabel.setText(str(current) + str(number))

    def popup(self):
        meals = self.outputLabel.text()
        days = foodConsumptionManagement(int(meals))
        msg = QMessageBox()
        starvationDate = datetime.now().date() + timedelta(days=days)
        starvationDate = starvationDate.strftime('%m/%d/%Y')
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('./pictures/ou_logo.jpg'))
        msg.setWindowTitle("Food Consumption Info")
        msg.setText("\nCurrent number of meal(s): " + str(meals) +
                            "\n\nMinimum number of days to consume meal(s): " + str(days) +
                    "\n\nMeals will run out on: " + str(starvationDate))
        msg.exec_()

    def homePressed(self):
        import homePage
        self.homeWindow = QtWidgets.QMainWindow()
        self.homeui = homePage.Ui_MainWindow()
        self.homeui.setupUiHome(self.homeWindow)
        #FoodManagement.hide()
        self.homeWindow.show()


    def helpPressed(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('./pictures/question.png'))
        msg.setWindowTitle("Help: Food Consumption")
        msg.setText("How to use food Management window described")
        msg.exec_()

    def retranslateUi(self, FoodManagement):
        _translate = QtCore.QCoreApplication.translate
        FoodManagement.setWindowTitle(_translate("FoodManagement", "Food Consumption Management"))
        self.menuOptions.setTitle(_translate("FoodManagement", "Options"))
        self.home.setText(_translate("FoodManagement", "Home"))
        self.help.setText(_translate("FoodManagement", "Help"))
        self.titleLabel.setText(_translate("FoodManagement", "Food Consumption Management"))
        self.button7.setText(_translate("FoodManagement", "7"))
        self.buttonSubmit.setText(_translate("FoodManagement", "Submit"))
        self.button8.setText(_translate("FoodManagement", "8"))
        self.button9.setText(_translate("FoodManagement", "9"))
        self.button5.setText(_translate("FoodManagement", "5"))
        self.button4.setText(_translate("FoodManagement", "4"))
        self.button6.setText(_translate("FoodManagement", "6"))
        self.button3.setText(_translate("FoodManagement", "3"))
        self.button2.setText(_translate("FoodManagement", "2"))
        self.button1.setText(_translate("FoodManagement", "1"))
        self.buttonClear.setText(_translate("FoodManagement", "Clear"))
        self.button0.setText(_translate("FoodManagement", "0"))
        self.entryLabel.setText(_translate("FoodManagement", "Enter the number of meals available: "))


def foodConsumptionManagement(n):
    """Because we go through the BFS tree one layer at a time, if a value is visited multiple times either:
            1. The path taken to reach the already known value is determined not to be the fasted route
            2. At least two different paths can reach that value at the same layer, and therefore took
                the same number of days.
        Anytime q[0][0] == 1 (q[0][0] will never = 0 before q[0][0] = 1) a minimum path has been found.
        Another minimum path may also exist in the same layer, however, it will take the same number of days
        to eat the initial number of meals, n"""
    visited_values = set()
    q = [[n, 0]]
    while q[0][0] != 1:
        if q[0][0] not in visited_values:
            # Case 1: eat one meal
            case1 = q[0][0] - 1
            days = q[0][1] + 1
            q.append([case1, days])

            # Case 2: eat half the meals (n/2)
            if q[0][0] % 2 == 0:
                case2 = q[0][0] / 2
                q.append([case2, days])

            # Case 3: eat 2/3 of the meals 2(n/3)
            if q[0][0] % 3 == 0:
                case3 = q[0][0] / 3
                q.append([case3, days])

            # q[0][0] is added to the set of visited_values
            visited_values.add(q[0][0])

        # remove this value from the list
        q.pop(0)

    """No matter what path we use to eat the meals, we will always end up with 1 meal left, 
        that will always take 1 day to eat."""
    min_days = q[0][1] + 1
    return min_days

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FoodManagement = QtWidgets.QMainWindow()
    ui = Ui_FoodManagement()
    ui.setupUiFood(FoodManagement)
    FoodManagement.show()
    sys.exit(app.exec_())
