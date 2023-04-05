import secrets
from PySide2 import QtWidgets

import ShortestRoute

class MyQtApp(ShortestRoute.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Transportation Management")
    #    self.populate_table_widget()
    
    def populate_table_widget(self):
        self.tableWidget.clear()
      #  x = ["apple","banana","mango","orange"]
      # for e in x:
      #    item = QtWidgets.QTableWidgetItem() 
      #   item.setText(e)

    def addRow(self):
    # Retrieve text from QLineEdit
        x = self.x_input.text()
        y = self.y_input.text()
        z = self.z_input.text()
        # Create a empty row at bottom of table
        numRows = self.tableWidget.rowCount()
        self.tableWidget.insertRow(numRows)
        # Add text to the row
        self.tableWidget.setItem(numRows, 0, QtWidgets.QTableWidgetItem(x))
        self.tableWidget.setItem(numRows, 1, QtWidgets.QTableWidgetItem(y))
        self.tableWidget.setItem(numRows, 2, QtWidgets.QTableWidgetItem(z))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()