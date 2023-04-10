from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import re

#cant remove new nums

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 540)
        MainWindow.setWindowIcon(QtGui.QIcon('./pictures/ou_logo.jpg'))
        MainWindow.setStyleSheet("background-color: #123456;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(19, 19, 760, 480))
        self.frame1.setStyleSheet("background-color: white;")
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)

        self.titleLabel = QtWidgets.QLabel(self.frame1)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 760, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.line = QtWidgets.QFrame(self.frame1)
        self.line.setGeometry(QtCore.QRect(20, 40, 720, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)

        self.addDropCodesLabel = QtWidgets.QLabel(self.frame1)
        self.addDropCodesLabel.setGeometry(QtCore.QRect(30, 90, 395, 20))
        font.setBold(False)
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.addDropCodesLabel.setFont(font)
        self.addDropCodesLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.entryline = QtWidgets.QFrame(self.frame1)
        self.entryline.setGeometry(QtCore.QRect(30, 113, 395, 5))
        self.entryline.setFrameShadow(QtWidgets.QFrame.Plain)
        self.entryline.setLineWidth(2)
        self.entryline.setFrameShape(QtWidgets.QFrame.HLine)

        self.codeEdit = QtWidgets.QTextEdit(self.frame1)
        self.codeEdit.setGeometry(QtCore.QRect(30, 130, 395, 51))
        self.codeEdit.setFont(font)
        self.codeEdit.setStyleSheet("background-color: white; border: 1px solid black;")
        self.codeEdit.setAlignment(QtCore.Qt.AlignCenter)

        self.button0 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("0"))
        self.button0.setGeometry(QtCore.QRect(30, 210, 95, 51))
        self.button0.setStyleSheet("border: 1px solid black;")
        font.setBold(False)
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.button0.setFont(font)

        self.button1 = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.enterNums("1"))
        self.button1.setGeometry(QtCore.QRect(130, 210, 95, 51))
        self.button1.setStyleSheet("border: 1px solid black;")
        self.button1.setFont(font)

        self.buttonClear = QtWidgets.QPushButton(self.frame1, clicked=lambda: self.clear())
        self.buttonClear.setGeometry(QtCore.QRect(230, 210, 195, 51))
        self.buttonClear.setStyleSheet("border: 1px solid black;")
        font.setPointSize(12)
        self.buttonClear.setFont(font)

        self.buttonAdd = QtWidgets.QPushButton(self.frame1, clicked=self.addCode)
        self.buttonAdd.setGeometry(QtCore.QRect(30, 266, 195, 51))
        self.buttonAdd.setStyleSheet("background-color: #99A3A4;")
        self.buttonAdd.setFont(font)

        self.buttonRemove = QtWidgets.QPushButton(self.frame1, clicked=self.removeCode)
        self.buttonRemove.setGeometry(QtCore.QRect(230, 266, 195, 51))
        self.buttonRemove.setStyleSheet("background-color: #99A3A4;")
        self.buttonRemove.setFont(font)

        self.vehiclesLabel = QtWidgets.QLabel(self.frame1)
        self.vehiclesLabel.setGeometry(QtCore.QRect(445, 146, 200, 20))
        font.setPointSize(11)
        self.vehiclesLabel.setFont(font)

        self.line = QtWidgets.QFrame(self.frame1)
        self.line.setGeometry(QtCore.QRect(445, 166, 160, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)

        self.vehiclesText = QtWidgets.QTextEdit(self.frame1)
        self.vehiclesText.setGeometry(QtCore.QRect(625, 136, 100, 40))
        self.vehiclesText.setFont(font)
        self.vehiclesText.setStyleSheet("border: 1px solid black;")
        self.vehiclesText.setAlignment(QtCore.Qt.AlignCenter)

        self.personnelLabel = QtWidgets.QLabel(self.frame1)
        self.personnelLabel.setGeometry(QtCore.QRect(445, 206, 200, 20))
        self.personnelLabel.setFont(font)

        self.line = QtWidgets.QFrame(self.frame1)
        self.line.setGeometry(QtCore.QRect(445, 226, 160, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)

        self.personnelText = QtWidgets.QTextEdit(self.frame1)
        self.personnelText.setGeometry(QtCore.QRect(625, 196, 100, 40))
        self.personnelText.setFont(font)
        self.personnelText.setStyleSheet("border: 1px solid black;")
        self.personnelText.setAlignment(QtCore.Qt.AlignCenter)

        self.buttonSubmit = QtWidgets.QPushButton(self.frame1, clicked=self.popup)
        self.buttonSubmit.setGeometry(QtCore.QRect(625, 256, 100, 40))
        self.buttonSubmit.setStyleSheet("background-color: #99A3A4;")
        font.setPointSize(12)
        self.buttonSubmit.setFont(font)

        self.allCodes = QtWidgets.QLabel(self.frame1)
        self.allCodes.setGeometry(QtCore.QRect(30, 337, 700, 31))
        font.setPointSize(14)
        self.allCodes.setFont(font)
        self.allCodes.setAlignment(QtCore.Qt.AlignCenter)

        self.codeline = QtWidgets.QFrame(self.frame1)
        self.codeline.setGeometry(QtCore.QRect(65, 365, 630, 5))
        self.codeline.setFrameShadow(QtWidgets.QFrame.Plain)
        self.codeline.setLineWidth(2)
        self.codeline.setFrameShape(QtWidgets.QFrame.HLine)

        self.codeTextBrowser = QtWidgets.QTextBrowser(self.frame1)
        self.codeTextBrowser.setGeometry(QtCore.QRect(30, 380, 700, 80))
        font.setBold(False)
        font.setPointSize(12)
        self.codeTextBrowser.setFont(font)
        self.codeTextBrowser.setAlignment(QtCore.Qt.AlignCenter)
        self.codeTextBrowser.setStyleSheet("border: 1px solid black;")

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 26))
        self.menubar.setStyleSheet("background-color: white; color: black;")

        self.menuOptions = QtWidgets.QMenu(self.menubar)
        MainWindow.setMenuBar(self.menubar)

        self.help = QtWidgets.QAction(MainWindow)
        self.help.triggered.connect(self.helpPressed)
        self.help.setIcon(QtGui.QIcon('./pictures/question.png'))
        self.menuOptions.addAction(self.help)
        self.menubar.addAction(self.menuOptions.menuAction())

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clear(self):
        self.codeEdit.setText("")
        self.codeEdit.setAlignment(QtCore.Qt.AlignCenter)

    def enterNums(self, number):
        current = self.codeEdit.toPlainText()
        if current == "0":
            self.codeEdit.setText(str(number))
            self.codeEdit.setAlignment(QtCore.Qt.AlignCenter)
        else:
            self.codeEdit.setText("")
            self.codeEdit.setAlignment(QtCore.Qt.AlignCenter)
            self.codeEdit.setText(str(current) + str(number))
            self.codeEdit.setAlignment(QtCore.Qt.AlignCenter)

    def addCode(self):
        currentCode = self.codeEdit.toPlainText()
        checkCode = set(currentCode)
        validSet = {'0', '1'}
        if checkCode != validSet and checkCode != {'0'} and checkCode != {'1'}:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowIcon(QtGui.QIcon('./pictures/question.png'))
            msg.setWindowTitle("Error: Invalid Entry")
            msg.setText("The resource code '" + currentCode + "' is not a valid code. "
                                                              "This code should contain only 0's and 1's.  ")
            msg.exec_()
            return
        strCurrentCode = ", " + currentCode + ", "
        allCodes = self.codeTextBrowser.toPlainText()
        allCodesList = allCodes.split(", ")
        if allCodesList[0] == currentCode or allCodesList[-1] == currentCode or strCurrentCode in allCodes:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowIcon(QtGui.QIcon('./pictures/question.png'))
            msg.setWindowTitle("Error: Repeated Entry")
            msg.setText("The resource code '" + currentCode + "' is already a current city resource code. ")
            msg.exec_()
            return
        if strCurrentCode not in allCodes:
            self.codeEdit.setText("")
            self.codeEdit.setAlignment(QtCore.Qt.AlignCenter)
            self.codeTextBrowser.setText("")
            self.codeTextBrowser.setText(str(allCodes) + ", " + str(currentCode))

    def removeCode(self):
        currentCode = self.codeEdit.toPlainText()
        checkCode = set(currentCode)
        validSet = {'0', '1'}
        if checkCode != validSet and checkCode != {'0'} and checkCode != {'1'}:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowIcon(QtGui.QIcon('./pictures/question.png'))
            msg.setWindowTitle("Error: Invalid Entry")
            msg.setText("The resource code '" + currentCode + "' is not a valid code. "
                                                              "This code should contain only 0's and 1's.  ")
            msg.exec_()
            return
        strCurrentCode = ", " + currentCode + ", "
        allCodes = self.codeTextBrowser.toPlainText()
        allCodesList = allCodes.split(", ")
        self.codeEdit.setText("")
        self.codeEdit.setAlignment(QtCore.Qt.AlignCenter)
        if allCodesList[0] == currentCode:
            allCodesList.pop(0)
            updatedCodes = allCodesList
            newCodes = ", ".join([str(elem) for i, elem in enumerate(updatedCodes)])
        elif allCodesList[-1] == currentCode:
            allCodesList.pop(-1)
            updatedCodes = allCodesList
            newCodes = ", ".join([str(elem) for i, elem in enumerate(updatedCodes)])
        elif strCurrentCode in allCodes:
            newCodes = re.sub(strCurrentCode, ", ", allCodes)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowIcon(QtGui.QIcon('./pictures/question.png'))
            msg.setWindowTitle("Error: Code Removed")
            msg.setText("The resource code '" + currentCode + "' was not found in the list of "
                        "all the city resource codes available.")
            msg.exec_()
            return
        self.codeTextBrowser.setText("")
        print("newCodes: " + str(newCodes))

        self.codeTextBrowser.setText(str(newCodes))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('./pictures/question.png'))
        msg.setWindowTitle("Error: Invalid Entry")
        msg.setText("The resource code '" + currentCode + "' was removed from the list of "
                    "all the city resource codes available.")
        msg.exec_()


    def popup(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('./pictures/question.png'))
        msg.setWindowTitle("Info: Resource Management")
        vehicles = self.vehiclesText.toPlainText()
        personnel = self.personnelText.toPlainText()
        allCodes = self.codeTextBrowser.toPlainText()
        print(allCodes)
        if vehicles.isnumeric() == False:
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Error: Resource Management")
            msg.setText("Please enter a positive whole number to represent number of vehicles requested.")
            msg.exec_()
        elif personnel.isnumeric() == False:
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Error: Resource Management")
            msg.setText("Please enter a positive whole number to represent number of personnel requested.")
            msg.exec_()
        else:
            msg.setText("The max number of 0's or vehicles requested: " + str(vehicles) +
                        "\nThe max number of 1's or personnel requested: " + str(personnel) +
                        "\n\n Solution : ...")
            msg.exec_()

    def helpPressed(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('./pictures/question.png'))
        msg.setWindowTitle("Help: Resource Management")
        msg.setText("How to use Resource Management window described")
        msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Resource Allocation Management"))
        self.titleLabel.setText(_translate("MainWindow", "Resource Allocation Management"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.help.setText(_translate("MainWindow", "Help"))
        self.addDropCodesLabel.setText(_translate("MainWindow", "Resource Codes"))
        self.button0.setText(_translate("MainWindow", "0\n(vehicles)"))
        self.button1.setText(_translate("MainWindow", "1\n(personnel)"))
        self.buttonClear.setText(_translate("MainWindow", "Clear"))
        self.buttonAdd.setText(_translate("MainWindow", "Add Code"))
        self.buttonRemove.setText(_translate("MainWindow", "Remove Code"))
        self.vehiclesLabel.setText(_translate("MainWindow", "Vehicles Requested :"))
        self.personnelLabel.setText(_translate("MainWindow", "Personnel Requested:"))
        self.buttonSubmit.setText(_translate("MainWindow", "Submit"))
        self.allCodes.setText(_translate("MainWindow", "All City Resource Codes"))
        self.codeTextBrowser.setText(_translate("MainWindow", "10, 0001, 111001, 1, 0"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
