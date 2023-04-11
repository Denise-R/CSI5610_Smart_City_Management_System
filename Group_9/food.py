from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime, timedelta

class Ui_FoodManagement(object):
    def setupUiFood(self, FoodManagement):
        FoodManagement.setObjectName("FoodManagement")
        FoodManagement.resize(907, 651)
        FoodManagement.setWindowIcon(QtGui.QIcon(':/pictures/ou_logo.jpg'))
        FoodManagement.setStyleSheet("background-color: #123456;")

        self.centralwidget = QtWidgets.QWidget(FoodManagement)
        FoodManagement.setCentralWidget(self.centralwidget)

        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(19, 19, 867, 590))
        self.frame1.setStyleSheet("background-color: white;")
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)

        self.titleLabel = QtWidgets.QLabel(self.frame1)
        self.titleLabel.setGeometry(QtCore.QRect(0, -1, 830, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.line = QtWidgets.QFrame(self.frame1)
        self.line.setGeometry(QtCore.QRect(20, 40, 830, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)

        self.entryLabel = QtWidgets.QLabel(self.frame1)
        self.entryLabel.setGeometry(QtCore.QRect(30, 90, 401, 20))
        font.setBold(False)
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.entryLabel.setFont(font)
        self.entryLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.entryline = QtWidgets.QFrame(self.frame1)
        self.entryline.setGeometry(QtCore.QRect(30, 113, 401, 5))
        self.entryline.setFrameShadow(QtWidgets.QFrame.Plain)
        self.entryline.setLineWidth(2)
        self.entryline.setFrameShape(QtWidgets.QFrame.HLine)

        self.outputText = QtWidgets.QTextEdit(self.frame1)
        self.outputText.setGeometry(QtCore.QRect(30, 130, 401, 61))
        self.outputText.setFont(font)
        self.outputText.setFrameShape(QtWidgets.QFrame.Box)
        self.outputText.setStyleSheet("background-color: white; border: 1px solid black;")
        self.outputText.setAlignment(QtCore.Qt.AlignCenter)

        self.button0 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("0"))
        self.button0.setGeometry(QtCore.QRect(20, 480, 278, 88))
        self.button0.setStyleSheet("background-color: white; border: 1px solid black;")
        font.setPointSize(16)
        self.button0.setFont(font)

        self.button1 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("1"))
        self.button1.setGeometry(QtCore.QRect(20, 390, 138, 88))
        self.button1.setStyleSheet("background-color: white; border: 1px solid black;")
        self.button1.setFont(font)

        self.button2 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("2"))
        self.button2.setGeometry(QtCore.QRect(160, 390, 138, 88))
        self.button2.setStyleSheet("background-color: white; border: 1px solid black;")
        self.button2.setFont(font)

        self.button3 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("3"))
        self.button3.setGeometry(QtCore.QRect(300, 390, 138, 88))
        self.button3.setStyleSheet("background-color: white; border: 1px solid black;")
        self.button3.setFont(font)

        self.button4 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("4"))
        self.button4.setGeometry(QtCore.QRect(20, 300, 138, 88))
        self.button4.setStyleSheet("background-color: white; border: 1px solid black;")
        self.button4.setFont(font)

        self.button5 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("5"))
        self.button5.setGeometry(QtCore.QRect(160, 300, 138, 88))
        self.button5.setStyleSheet("background-color: white; border: 1px solid black;")
        self.button5.setFont(font)

        self.button6 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("6"))
        self.button6.setGeometry(QtCore.QRect(300, 300, 138, 88))
        self.button6.setStyleSheet("background-color: white; border: 1px solid black;")
        self.button6.setFont(font)

        self.button7 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("7"))
        self.button7.setGeometry(QtCore.QRect(20, 210, 138, 88))
        self.button7.setStyleSheet("background-color: white; border: 1px solid black;")
        self.button7.setFont(font)

        self.button8 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("8"))
        self.button8.setGeometry(QtCore.QRect(160, 210, 138, 88))
        self.button8.setStyleSheet("background-color: white; border: 1px solid black;")
        self.button8.setFont(font)

        self.button9 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("9"))
        self.button9.setGeometry(QtCore.QRect(300, 210, 138, 88))
        self.button9.setStyleSheet("background-color: white; border: 1px solid black;")
        self.button9.setFont(font)

        self.buttonClear = QtWidgets.QPushButton(self.frame1, clicked=self.clear)
        self.buttonClear.setGeometry(QtCore.QRect(300, 480, 138, 88))
        self.buttonClear.setStyleSheet("background-color: white; border: 1px solid black;")
        self.buttonClear.setFont(font)

        self.buttonSubmit = QtWidgets.QPushButton(self.frame1, clicked=self.popup)
        self.buttonSubmit.setGeometry(QtCore.QRect(500, 497, 306, 50))
        self.buttonSubmit.setStyleSheet("background-color: #99A3A4;")
        self.buttonSubmit.setFont(font)

        self.calendarLabel = QtWidgets.QLabel(self.frame1)
        self.calendarLabel.setObjectName(u"calendarLabel")
        self.calendarLabel.setGeometry(QtCore.QRect(458, 142, 390, 61))
        font.setPointSize(14)
        self.calendarLabel.setFont(font)
        self.calendarLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.calendarline = QtWidgets.QFrame(self.frame1)
        self.calendarline.setGeometry(QtCore.QRect(458, 190, 390, 5))
        self.calendarline.setFrameShadow(QtWidgets.QFrame.Plain)
        self.calendarline.setLineWidth(2)
        self.calendarline.setFrameShape(QtWidgets.QFrame.HLine)

        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame1)
        self.calendarWidget.setGeometry(QtCore.QRect(458, 210, 390, 268))
        self.calendarWidget.setStyleSheet("background-color: gray; border: 1px solid black;")

        self.menubar = QtWidgets.QMenuBar(FoodManagement)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 26))
        self.menubar.setStyleSheet("background-color: white; color: black;")

        self.menuOptions = QtWidgets.QMenu(self.menubar)
        FoodManagement.setMenuBar(self.menubar)

        self.help = QtWidgets.QAction(FoodManagement)
        self.help.triggered.connect(self.helpPressed)
        self.help.setIcon(QtGui.QIcon(':/pictures/question.png'))
        self.menuOptions.addAction(self.help)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(FoodManagement)
        QtCore.QMetaObject.connectSlotsByName(FoodManagement)


    def clear(self):
        self.outputText.setText("")
        self.outputText.setAlignment(QtCore.Qt.AlignCenter)

    def enterNums(self, number):
        current = self.outputText.toPlainText()
        if current == "0":
            self.outputText.setText(str(number))
            self.outputText.setAlignment(QtCore.Qt.AlignCenter)
        else:
            self.outputText.setText("")
            self.outputText.setText(str(current) + str(number))
            self.outputText.setAlignment(QtCore.Qt.AlignCenter)

    def popup(self):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon(':/pictures/ou_logo.jpg'))
        meals = self.outputText.toPlainText()
        if str(meals) == "0" or str(meals).isnumeric() is False:
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Error: Food Consumption")
            msg.setText("Please enter a positive whole number to represent the meals available.")
            msg.exec_()
        elif int(meals) > 2 * pow(10, 9):
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Error: Food Consumption")
            msg.setText("The number of meals you entered is too large to be computed. "
                        "Please enter a number between 0 and 2,000,000,001.")
            msg.exec_()
        else:
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Info: Food Consumption Management")
            days = foodConsumptionManagement(int(meals))
            date = self.calendarWidget.selectedDate()
            strDate = date.toString("yyyy-MM-dd")
            strDate = datetime.strptime(strDate, '%Y-%m-%d')
            starvationDate = strDate + timedelta(days=days)
            starvationDate = starvationDate.strftime('%m/%d/%Y')
            strDate = strDate.strftime('%m/%d/%Y')
            msg.setText("\nCurrent number of meal(s): " + str(meals) +
                        "\nStart date: " + str(strDate) +
                        "\nEnd date: " + str(starvationDate) +
                        "\n\nIt will take " + str(days) + " day(s) to run out of " + str(meals) + " meal(s).")
            msg.exec_()


    def helpPressed(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon(':/pictures/question.png'))
        msg.setWindowTitle("Help: Food Consumption")
        msg.setText("This window optimizes the number of days it takes for students in the city's public school "
                    "districts to consume a given number of school lunch meal(s). "
                    "\n\nTo calculate the number of days it will take for the meal(s) to run out, enter:\n\t"
                    "1. The number of meal(s) available\n\t"
                    "2. The first day these meal(s) will be consumed\n\n"
                    "Once you submit these parameters, the total number of days it will take to run out of meals "
                    "and the end date will be displayed. ")
        msg.exec_()

    def retranslateUi(self, FoodManagement):
        _translate = QtCore.QCoreApplication.translate
        FoodManagement.setWindowTitle(_translate("FoodManagement", "Food Consumption Management"))
        self.menuOptions.setTitle(_translate("FoodManagement", "Options"))
        self.help.setText(_translate("FoodManagement", "Help"))
        self.calendarLabel.setText(_translate("FoodManagement", "Select Start Date:"))
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
