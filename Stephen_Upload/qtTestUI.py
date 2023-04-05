from PySide2 import QtWidgets

import ShortestRoute

class MyQtApp(ShortestRoute.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()

"""
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
"""