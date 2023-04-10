import json
from operator import attrgetter
from typing import NamedTuple, List, Dict
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


class Task(NamedTuple):
    department: str
    responsible: str
    time_est: int
    description: str
    uid: int

    def __str__(self) -> str:
        return f"{self.uid};{self.department};{self.responsible};{self.time_est};{self.description}"

    def to_dict(self) -> Dict:
        return {"department": self.department, "responsible": self.responsible, "time_est": self.time_est,
                "description": self.description, "uid": self.uid}


class Ui_TaskSchedulerWindow(object):

    def __init__(self) -> None:
        self.tasks: List[Task] = []
        self.uid = 0
        self.schedule = None

    def get_uid(self):
        self.uid += 1
        return self.uid

    def setupUi(self, TaskSchedulerWindow):
        TaskSchedulerWindow.setObjectName("TaskSchedulerWindow")
        TaskSchedulerWindow.resize(950, 720)
        TaskSchedulerWindow.setWindowIcon(QtGui.QIcon(':/pictures/ou_logo.jpg'))
        TaskSchedulerWindow.setStyleSheet("background-color: #123456;")

        self.centralwidget = QtWidgets.QWidget(TaskSchedulerWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(20, 10, 910, 600))
        self.frame1.setStyleSheet("background-color: white;")
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")

        self.label1 = QtWidgets.QLabel(self.frame1)
        self.label1.setGeometry(QtCore.QRect(5, 5, 910, 30))
        self.label1.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)

        self.line = QtWidgets.QFrame(self.frame1)
        self.line.setGeometry(QtCore.QRect(30, 35, 850, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")

        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2.setGeometry(QtCore.QRect(20, 80, 910, 600))
        self.frame2.setStyleSheet("background-color: white;")
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.splitter_2 = QtWidgets.QSplitter(self.frame2)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")

        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.groupBox.setFont(font)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.label.setFont(font)
        self.verticalLayout.addWidget(self.label)

        self.department_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.department_comboBox.setObjectName("department_comboBox")
        self.department_comboBox.addItem("")
        self.department_comboBox.addItem("")
        self.department_comboBox.addItem("")
        self.department_comboBox.addItem("")
        self.department_comboBox.addItem("")
        self.department_comboBox.addItem("")
        self.department_comboBox.addItem("")
        self.department_comboBox.addItem("")
        self.department_comboBox.addItem("")
        self.department_comboBox.setItemText(8, "")
        self.verticalLayout.addWidget(self.department_comboBox)
        self.department_comboBox.setFont(font)

        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_4.setFont(font)

        self.responsible_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.responsible_lineEdit.setObjectName("responsible_lineEdit")
        self.verticalLayout.addWidget(self.responsible_lineEdit)


        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_2.setFont(font)

        self.hours_spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.hours_spinBox.setMinimum(1)
        self.hours_spinBox.setMaximum(8)
        self.hours_spinBox.setSingleStep(1)
        self.hours_spinBox.setObjectName("hours_SpinBox")
        self.verticalLayout.addWidget(self.hours_spinBox)
        self.hours_spinBox.setFont(font)

        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_3.setFont(font)

        self.description_textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.description_textEdit.setObjectName("description_textEdit")
        self.verticalLayout.addWidget(self.description_textEdit)
        self.description_textEdit.setFont(font)

        self.create_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.create_pushButton.setObjectName("create_pushButton")
        self.verticalLayout.addWidget(self.create_pushButton)
        self.create_pushButton.setFont(font)

        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setFont(font)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.tasks_listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.tasks_listWidget.setObjectName("tasks_listWidget")
        self.verticalLayout_2.addWidget(self.tasks_listWidget)
        self.tasks_listWidget.setFont(font)

        self.widget = QtWidgets.QWidget(self.groupBox_2)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.remove_pushButton = QtWidgets.QPushButton(self.widget)
        self.remove_pushButton.setObjectName("remove_pushButton")
        self.horizontalLayout.addWidget(self.remove_pushButton)
        self.remove_pushButton.setFont(font)

        self.savet_pushButton = QtWidgets.QPushButton(self.widget)
        self.savet_pushButton.setObjectName("savet_pushButton")
        self.horizontalLayout.addWidget(self.savet_pushButton)
        self.savet_pushButton.setFont(font)

        self.load_pushButton = QtWidgets.QPushButton(self.widget)
        self.load_pushButton.setObjectName("load_pushButton")
        self.horizontalLayout.addWidget(self.load_pushButton)
        self.verticalLayout_2.addWidget(self.widget)
        self.load_pushButton.setFont(font)

        self.groupBox_3 = QtWidgets.QGroupBox(self.splitter_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setFont(font)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.widget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.generate_pushButton = QtWidgets.QPushButton(self.widget_2)
        self.generate_pushButton.setObjectName("generate_pushButton")
        self.generate_pushButton.setFont(font)
        self.horizontalLayout_2.addWidget(self.generate_pushButton)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)

        self.saves_pushButton = QtWidgets.QPushButton(self.widget_2)
        self.saves_pushButton.setObjectName("saves_pushButton")
        self.saves_pushButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.saves_pushButton)
        self.verticalLayout_3.addWidget(self.widget_2)

        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_3)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(7)
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setFont(font)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout_4.addWidget(self.splitter_2)

        TaskSchedulerWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(TaskSchedulerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 24))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet("background-color: white; color: black;")

        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        TaskSchedulerWindow.setMenuBar(self.menubar)

        self.home = QtWidgets.QAction(TaskSchedulerWindow)
        self.home.setObjectName("home")
        self.help = QtWidgets.QAction(TaskSchedulerWindow)
        self.help.setObjectName("help")
        self.menuOptions.addAction(self.home)
        self.home.triggered.connect(self.homePressed)
        self.home.setIcon(QtGui.QIcon(':/pictures/home.png'))
        self.help.triggered.connect(self.helpPressed)
        self.help.setIcon(QtGui.QIcon(':/pictures/question.png'))
        self.menuOptions.addAction(self.help)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(TaskSchedulerWindow)
        QtCore.QMetaObject.connectSlotsByName(TaskSchedulerWindow)

        self.create_pushButton.clicked.connect(self.clicked_create_task)
        self.remove_pushButton.clicked.connect(self.clicked_remove_task)
        self.saves_pushButton.clicked.connect(self.clicked_save_schedule)
        self.savet_pushButton.clicked.connect(self.save_tasks)
        self.load_pushButton.clicked.connect(self.clicked_load_tasks)
        self.generate_pushButton.clicked.connect(self.clicked_generate_schedule)
        self.tableWidget.itemClicked.connect(self.itemClicked_highlight_task)

    def retranslateUi(self, TaskSchedulerWindow):
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(7)
        _translate = QtCore.QCoreApplication.translate
        TaskSchedulerWindow.setWindowTitle(_translate("TaskSchedulerWindow", "Task Scheduler"))
        self.menuOptions.setTitle(_translate("FoodManagement", "Options"))
        self.home.setText(_translate("FoodManagement", "Home"))
        self.help.setText(_translate("FoodManagement", "Help"))
        self.label1.setText(_translate("MainWindow", "Task Scheduler Management"))
        self.groupBox.setTitle(_translate("TaskSchedulerWindow", "New Task"))
        self.label.setText(_translate("TaskSchedulerWindow", "Department:"))
        self.department_comboBox.setItemText(0, _translate("TaskSchedulerWindow", "Maintenance"))
        self.department_comboBox.setItemText(1, _translate("TaskSchedulerWindow", "Transportation"))
        self.department_comboBox.setItemText(2, _translate("TaskSchedulerWindow", "Building, Safety, Environmental"))
        self.department_comboBox.setItemText(3, _translate("TaskSchedulerWindow", "Parks & Recreation"))
        self.department_comboBox.setItemText(4, _translate("TaskSchedulerWindow", "Emergency Services"))
        self.department_comboBox.setItemText(5, _translate("TaskSchedulerWindow", "Commerce"))
        self.department_comboBox.setItemText(6, _translate("TaskSchedulerWindow", "Human Resources"))
        self.department_comboBox.setItemText(7, _translate("TaskSchedulerWindow", "Water and Sewerage"))
        self.label_4.setText(_translate("TaskSchedulerWindow", "Responsible:"))
        self.label_2.setText(_translate("TaskSchedulerWindow", "Time Estimate (hours):"))
        self.label_3.setText(_translate("TaskSchedulerWindow", "Description:"))
        self.create_pushButton.setText(_translate("TaskSchedulerWindow", "Create Task"))
        self.groupBox_2.setTitle(_translate("TaskSchedulerWindow", "Current Tasks"))
        self.remove_pushButton.setText(_translate("TaskSchedulerWindow", "Remove Task"))
        self.savet_pushButton.setText(_translate("TaskSchedulerWindow", "Save Tasks"))
        self.load_pushButton.setText(_translate("TaskSchedulerWindow", "Load Tasks"))
        self.groupBox_3.setTitle(_translate("TaskSchedulerWindow", "Schedule"))
        self.generate_pushButton.setText(_translate("TaskSchedulerWindow", "Generate Schedule"))
        self.saves_pushButton.setText(_translate("TaskSchedulerWindow", "Save Schedule"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("TaskSchedulerWindow", "8 AM"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("TaskSchedulerWindow", "9 AM"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("TaskSchedulerWindow", "10 AM"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("TaskSchedulerWindow", "11 AM"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("TaskSchedulerWindow", "12 AM"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("TaskSchedulerWindow", "1 PM"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("TaskSchedulerWindow", "2 PM"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("TaskSchedulerWindow", "3 PM"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("TaskSchedulerWindow", "4 PM"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("TaskSchedulerWindow", "5 PM"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("TaskSchedulerWindow", "Monday"))
        item.setFont(font)
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("TaskSchedulerWindow", "Tuesday"))
        item.setFont(font)
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("TaskSchedulerWindow", "Wednesday"))
        item.setFont(font)
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("TaskSchedulerWindow", "Thursday"))
        item.setFont(font)
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("TaskSchedulerWindow", "Friday"))
        item.setFont(font)

    def save_tasks(self):
        t_file = QtWidgets.QFileDialog.getSaveFileName(None, "Save Tasks", "", "JSON (*.json)")
        if t_file:
            tmp_dict = [x.to_dict() for x in self.tasks]
            with open(t_file[0], "w") as jf:
                json.dump(tmp_dict, jf)

    def clicked_save_schedule(self):
        csv_list = []
        csv_list.append(";Monday;Tuesday;Wednesday;Thursday;Friday")
        for r in range(self.tableWidget.rowCount()):
            item = self.tableWidget.verticalHeaderItem(r)
            txt = item.text()
            for c in range(self.tableWidget.columnCount()):
                txt += f";{self.tableWidget.item(r, c)}"
            csv_list.append(txt)

        s_file = QtWidgets.QFileDialog.getSaveFileName(None, "Save Schedule", "", "CSV (*.csv)")
        if s_file:
            with open(s_file[0], "w") as cf:
                for l in csv_list:
                    cf.write(l + "\n")

    def clicked_load_tasks(self):
        t_file = QtWidgets.QFileDialog.getOpenFileName(None, "Load Tasks", "", "JSON (*.json)")
        if t_file:
            with open(t_file[0], "r") as jf:
                j_tasks = json.load(jf)
                self.tasks.clear()
                self.tasks_listWidget.clear()
                for t in j_tasks:
                    self.tasks.append(Task(t["department"],
                                           t["responsible"],
                                           t["time_est"],
                                           t["description"],
                                           t["uid"]))

                    self.tasks_listWidget.addItem(str(self.tasks[-1]))

    def clicked_create_task(self):
        self.tasks.append(Task(self.department_comboBox.currentText(),
                               self.responsible_lineEdit.text(),
                               self.hours_spinBox.value(),
                               self.description_textEdit.toPlainText(),
                               self.get_uid()))

        self.tasks_listWidget.addItem(str(self.tasks[-1]))

    def clicked_generate_schedule(self):
        total_time = sum(t.time_est for t in self.tasks)
        if total_time > (self.tableWidget.rowCount() * self.tableWidget.columnCount()):
            QtWidgets.QMessageBox(self, "Overbooked!", "Too many hours alocated,\nplease remove hours and try again!")
            return

        sorted_tasks = sorted(self.tasks, key=attrgetter('time_est'))
        for row in range(self.tableWidget.rowCount()):
            for column in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem())

        schedule: List[List[List[Task], int]] = [[[], 0] for x in range(self.tableWidget.columnCount())]

        for task in sorted_tasks:
            for d in schedule:
                if (d[1] + task.time_est) < self.tableWidget.rowCount():
                    d[0].append(task)
                    d[1] += task.time_est
                    break

        before = 0
        for i, day in enumerate(schedule):
            for task in day[0]:
                for x in range(before, before + task.time_est):
                    item = self.tableWidget.item(x, i)
                    item.setText(str(task.uid))
                before = task.time_est

    def clicked_remove_task(self):
        index = self.tasks_listWidget.selectionModel().selectedIndexes()

        for i in index:
            self.tasks_listWidget.takeItem(i.row())
            del self.tasks[i.row()]

    def itemClicked_highlight_task(self, item):
        if item.text() is not "":
            uid = int(item.text())
        else:
            return

        self.tasks_listWidget.clearSelection()
        for r in range(self.tasks_listWidget.count()):
            item = self.tasks_listWidget.item(r)
            iuid = int(item.text().split(";")[0])
            if iuid == uid:
                item.setSelected(True)

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
        msg.setWindowTitle("Help: Task Scheduler Management")
        msg.setText("How to use Task Scheduler Management window described ...")
        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_TaskSchedulerWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())