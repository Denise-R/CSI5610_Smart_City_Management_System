from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):

    def __init__(self) -> None:
        self.mat = [[1, 0, 1, 0, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 0, 1, 1, 1, 1, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 0, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1, 1, 1, 1, 1]]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 730)
        MainWindow.setWindowIcon(QtGui.QIcon('./pictures/ou_logo.jpg'))
        MainWindow.setStyleSheet("background-color: #123456;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(20, 15, 1080, 670))
        self.frame1.setStyleSheet("background-color: white;")
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")

        self.label = QtWidgets.QLabel(self.frame1)
        self.label.setGeometry(QtCore.QRect(5, 5, 1080, 30))
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.line = QtWidgets.QFrame(self.frame1)
        self.line.setGeometry(QtCore.QRect(30, 35, 1080, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")

        self.p11 = QtWidgets.QPushButton(self.frame1)
        self.p11.setGeometry(QtCore.QRect(50, 110, 111, 71))
        self.p11.setStyleSheet("background-image: url(./pictures/image1x1.png);")
        self.p11.setText("")
        self.p11.setObjectName("p11")
        self.p12 = QtWidgets.QPushButton(self.frame1)
        self.p12.setGeometry(QtCore.QRect(160, 110, 111, 71))
        self.p12.setStyleSheet("background-image: url(./pictures/image1x2.png);")
        self.p12.setText("")
        self.p12.setObjectName("p12")
        self.p13 = QtWidgets.QPushButton(self.frame1)
        self.p13.setGeometry(QtCore.QRect(270, 110, 111, 71))
        self.p13.setStyleSheet("background-image: url(./pictures/image1x3.png);")
        self.p13.setText("")
        self.p13.setObjectName("p13")
        self.p14 = QtWidgets.QPushButton(self.frame1)
        self.p14.setGeometry(QtCore.QRect(380, 110, 111, 71))
        self.p14.setStyleSheet("background-image: url(./pictures/image1x4.png);")
        self.p14.setText("")
        self.p14.setObjectName("p14")
        self.p15 = QtWidgets.QPushButton(self.frame1)
        self.p15.setGeometry(QtCore.QRect(490, 110, 111, 71))
        self.p15.setStyleSheet("background-image:  url(./pictures/image1x5.png);")
        self.p15.setText("")
        self.p15.setObjectName("p15")
        self.p16 = QtWidgets.QPushButton(self.frame1)
        self.p16.setGeometry(QtCore.QRect(600, 110, 111, 71))
        self.p16.setStyleSheet("background-image:  url(./pictures/image1x6.png);")
        self.p16.setText("")
        self.p16.setObjectName("p16")
        self.p17 = QtWidgets.QPushButton(self.frame1)
        self.p17.setGeometry(QtCore.QRect(710, 110, 111, 71))
        self.p17.setStyleSheet("background-image: url(./pictures/image1x7.png);")
        self.p17.setText("")
        self.p17.setObjectName("p17")
        self.p18 = QtWidgets.QPushButton(self.frame1)
        self.p18.setGeometry(QtCore.QRect(820, 110, 101, 71))
        self.p18.setStyleSheet("background-image:url(./pictures/image1x8.png);")
        self.p18.setText("")
        self.p18.setObjectName("p18")
        self.p19 = QtWidgets.QPushButton(self.frame1)
        self.p19.setGeometry(QtCore.QRect(920, 110, 101, 71))
        self.p19.setStyleSheet("background-image: url(./pictures/image1x9.png);")
        self.p19.setText("")
        self.p19.setObjectName("p19")
        self.p21 = QtWidgets.QPushButton(self.frame1)
        self.p21.setGeometry(QtCore.QRect(50, 170, 111, 71))
        self.p21.setStyleSheet("background-image: url(./pictures/image2x1.png);")
        self.p21.setText("")
        self.p21.setObjectName("p21")
        self.p22 = QtWidgets.QPushButton(self.frame1)
        self.p22.setGeometry(QtCore.QRect(160, 170, 111, 71))
        self.p22.setStyleSheet("background-image: url(./pictures/image2x2.png);")
        self.p22.setText("")
        self.p22.setObjectName("p22")
        self.p25 = QtWidgets.QPushButton(self.frame1)
        self.p25.setGeometry(QtCore.QRect(490, 170, 111, 71))
        self.p25.setStyleSheet("background-image: url(./pictures/image2x5.png);")
        self.p25.setText("")
        self.p25.setObjectName("p25")
        self.p26 = QtWidgets.QPushButton(self.frame1)
        self.p26.setGeometry(QtCore.QRect(600, 170, 111, 71))
        self.p26.setStyleSheet("background-image: url(./pictures/image2x6.png);")
        self.p26.setText("")
        self.p26.setObjectName("p26")
        self.p24 = QtWidgets.QPushButton(self.frame1)
        self.p24.setGeometry(QtCore.QRect(380, 170, 111, 71))
        self.p24.setStyleSheet("background-image: url(./pictures/image2x4.png);")
        self.p24.setText("")
        self.p24.setObjectName("p24")
        self.p23 = QtWidgets.QPushButton(self.frame1)
        self.p23.setGeometry(QtCore.QRect(270, 170, 111, 71))
        self.p23.setStyleSheet("background-image:url(./pictures/image2x3.png);")
        self.p23.setText("")
        self.p23.setObjectName("p23")
        self.p27 = QtWidgets.QPushButton(self.frame1)
        self.p27.setGeometry(QtCore.QRect(710, 170, 111, 71))
        self.p27.setStyleSheet("background-image: url(./pictures/image2x7.png);")
        self.p27.setText("")
        self.p27.setObjectName("p27")
        self.p28 = QtWidgets.QPushButton(self.frame1)
        self.p28.setGeometry(QtCore.QRect(820, 170, 101, 71))
        self.p28.setStyleSheet("background-image: url(./pictures/image2x8.png);")
        self.p28.setText("")
        self.p28.setObjectName("p28")
        self.p29 = QtWidgets.QPushButton(self.frame1)
        self.p29.setGeometry(QtCore.QRect(920, 170, 101, 71))
        self.p29.setStyleSheet("background-image: url(./pictures/image2x9.png);")
        self.p29.setText("")
        self.p29.setObjectName("p29")
        self.p31 = QtWidgets.QPushButton(self.frame1)
        self.p31.setGeometry(QtCore.QRect(50, 240, 111, 71))
        self.p31.setStyleSheet("background-image: url(./pictures/image3x1.png);")
        self.p31.setText("")
        self.p31.setObjectName("p31")
        self.p41 = QtWidgets.QPushButton(self.frame1)
        self.p41.setGeometry(QtCore.QRect(50, 310, 111, 71))
        self.p41.setStyleSheet("background-image:url(./pictures/image4x1.png);")
        self.p41.setText("")
        self.p41.setObjectName("p41")
        self.p51 = QtWidgets.QPushButton(self.frame1)
        self.p51.setGeometry(QtCore.QRect(50, 380, 111, 71))
        self.p51.setStyleSheet("background-image: url(./pictures/image5x1.png);")
        self.p51.setText("")
        self.p51.setObjectName("p51")
        self.p61 = QtWidgets.QPushButton(self.frame1)
        self.p61.setGeometry(QtCore.QRect(50, 450, 111, 71))
        self.p61.setStyleSheet("background-image:url(./pictures/image6x1.png);")
        self.p61.setText("")
        self.p61.setObjectName("p61")
        self.CalculateETA = QtWidgets.QPushButton(self.frame1)
        self.CalculateETA.setGeometry(QtCore.QRect(50, 70, 271, 23))
        self.CalculateETA.setStyleSheet("background-color: rgb(90, 168, 86);")
        self.CalculateETA.setObjectName("CalculateETA")
        self.p71 = QtWidgets.QPushButton(self.frame1)
        self.p71.setGeometry(QtCore.QRect(50, 520, 111, 71))
        self.p71.setStyleSheet("background-image: url(./pictures/image7x1.png);")
        self.p71.setText("")
        self.p71.setObjectName("p71")
        self.p39 = QtWidgets.QPushButton(self.frame1)
        self.p39.setGeometry(QtCore.QRect(920, 240, 101, 71))
        self.p39.setStyleSheet("background-image: url(./pictures/image3x9.png);")
        self.p39.setText("")
        self.p39.setObjectName("p39")
        self.p49 = QtWidgets.QPushButton(self.frame1)
        self.p49.setGeometry(QtCore.QRect(920, 310, 101, 71))
        self.p49.setStyleSheet("background-image:url(./pictures/image4x9.png);")
        self.p49.setText("")
        self.p49.setObjectName("p49")
        self.p59 = QtWidgets.QPushButton(self.frame1)
        self.p59.setGeometry(QtCore.QRect(920, 380, 101, 71))
        self.p59.setStyleSheet("background-image: url(./pictures/image5x9.png);")
        self.p59.setText("")
        self.p59.setObjectName("p59")
        self.p69 = QtWidgets.QPushButton(self.frame1)
        self.p69.setGeometry(QtCore.QRect(920, 450, 101, 71))
        self.p69.setStyleSheet("background-image: url(./pictures/image6x9.png);")
        self.p69.setText("")
        self.p69.setObjectName("p69")
        self.p79 = QtWidgets.QPushButton(self.frame1)
        self.p79.setGeometry(QtCore.QRect(920, 520, 101, 71))
        self.p79.setStyleSheet("background-image: url(./pictures/image7x9.png);")
        self.p79.setText("")
        self.p79.setObjectName("p79")
        self.p32 = QtWidgets.QPushButton(self.frame1)
        self.p32.setGeometry(QtCore.QRect(160, 240, 111, 71))
        self.p32.setStyleSheet("background-image: url(./pictures/image3x2.png);")
        self.p32.setText("")
        self.p32.setObjectName("p32")
        self.p42 = QtWidgets.QPushButton(self.frame1)
        self.p42.setGeometry(QtCore.QRect(160, 310, 111, 71))
        self.p42.setStyleSheet("background-image: url(./pictures/image4x2.png);")
        self.p42.setText("")
        self.p42.setObjectName("p42")
        self.p52 = QtWidgets.QPushButton(self.frame1)
        self.p52.setGeometry(QtCore.QRect(160, 380, 111, 71))
        self.p52.setStyleSheet("background-image: url(./pictures/image5x2.png);")
        self.p52.setText("")
        self.p52.setObjectName("p52")
        self.p62 = QtWidgets.QPushButton(self.frame1)
        self.p62.setGeometry(QtCore.QRect(160, 450, 111, 71))
        self.p62.setStyleSheet("background-image: url(./pictures/image6x2.png);")
        self.p62.setText("")
        self.p62.setObjectName("p62")
        self.p72 = QtWidgets.QPushButton(self.frame1)
        self.p72.setGeometry(QtCore.QRect(160, 520, 111, 71))
        self.p72.setStyleSheet("background-image: url(./pictures/image7x2.png);")
        self.p72.setText("")
        self.p72.setObjectName("p72")
        self.ClickMe = QtWidgets.QPushButton(self.frame1)
        self.ClickMe.setGeometry(QtCore.QRect(430, 70, 251, 23))
        self.ClickMe.setStyleSheet("background-color: rgb(95, 176, 83);")
        self.ClickMe.setObjectName("ClickMe")
        self.Result = QtWidgets.QPushButton(self.frame1)
        self.Result.setGeometry(QtCore.QRect(770, 70, 251, 23))
        self.Result.setStyleSheet("background-color: rgb(98, 162, 93);")
        self.Result.setObjectName("Result")
        self.p33 = QtWidgets.QPushButton(self.frame1)
        self.p33.setGeometry(QtCore.QRect(270, 240, 111, 71))
        self.p33.setStyleSheet("background-image: url(./pictures/image3x3.png);")
        self.p33.setText("")
        self.p33.setObjectName("p33")
        self.p34 = QtWidgets.QPushButton(self.frame1)
        self.p34.setGeometry(QtCore.QRect(380, 240, 111, 71))
        self.p34.setStyleSheet("background-image: url(./pictures/image3x4.png);")
        self.p34.setText("")
        self.p34.setObjectName("p34")
        self.p35 = QtWidgets.QPushButton(self.frame1)
        self.p35.setGeometry(QtCore.QRect(490, 240, 111, 71))
        self.p35.setStyleSheet("background-image: url(./pictures/image3x5.png);")
        self.p35.setText("")
        self.p35.setObjectName("p35")
        self.p36 = QtWidgets.QPushButton(self.frame1)
        self.p36.setGeometry(QtCore.QRect(600, 240, 111, 71))
        self.p36.setStyleSheet("background-image: url(./pictures/image3x6.png);")
        self.p36.setText("")
        self.p36.setObjectName("p36")
        self.p37 = QtWidgets.QPushButton(self.frame1)
        self.p37.setGeometry(QtCore.QRect(710, 240, 111, 71))
        self.p37.setStyleSheet("background-image:url(./pictures/image3x7.png);")
        self.p37.setText("")
        self.p37.setObjectName("p37")
        self.p38 = QtWidgets.QPushButton(self.frame1)
        self.p38.setGeometry(QtCore.QRect(820, 240, 101, 71))
        self.p38.setStyleSheet("background-image: url(./pictures/image3x8.png);")
        self.p38.setText("")
        self.p38.setObjectName("p38")
        self.p43 = QtWidgets.QPushButton(self.frame1)
        self.p43.setGeometry(QtCore.QRect(270, 310, 111, 71))
        self.p43.setStyleSheet("background-image: url(./pictures/image4x3.png);")
        self.p43.setText("")
        self.p43.setObjectName("p43")
        self.p44 = QtWidgets.QPushButton(self.frame1)
        self.p44.setGeometry(QtCore.QRect(380, 310, 111, 71))
        self.p44.setStyleSheet("background-image: url(./pictures/image4x4.png);")
        self.p44.setText("")
        self.p44.setObjectName("p44")
        self.p45 = QtWidgets.QPushButton(self.frame1)
        self.p45.setGeometry(QtCore.QRect(490, 310, 111, 71))
        self.p45.setStyleSheet("background-image: url(./pictures/image4x5.png);")
        self.p45.setText("")
        self.p45.setObjectName("p45")
        self.p46 = QtWidgets.QPushButton(self.frame1)
        self.p46.setGeometry(QtCore.QRect(600, 310, 111, 71))
        self.p46.setStyleSheet("background-image:url(./pictures/image4x6.png);")
        self.p46.setText("")
        self.p46.setObjectName("p46")
        self.p47 = QtWidgets.QPushButton(self.frame1)
        self.p47.setGeometry(QtCore.QRect(710, 310, 111, 71))
        self.p47.setStyleSheet("background-image: url(./pictures/image4x7.png);")
        self.p47.setText("")
        self.p47.setObjectName("p47")
        self.p48 = QtWidgets.QPushButton(self.frame1)
        self.p48.setGeometry(QtCore.QRect(820, 310, 101, 71))
        self.p48.setStyleSheet("background-image: url(./pictures/image4x8.png);")
        self.p48.setText("")
        self.p48.setObjectName("p48")
        self.p53 = QtWidgets.QPushButton(self.frame1)
        self.p53.setGeometry(QtCore.QRect(270, 380, 111, 71))
        self.p53.setStyleSheet("background-image: url(./pictures/image5x3.png);")
        self.p53.setText("")
        self.p53.setObjectName("p53")
        self.p63 = QtWidgets.QPushButton(self.frame1)
        self.p63.setGeometry(QtCore.QRect(270, 450, 111, 71))
        self.p63.setStyleSheet("background-image: url(./pictures/image6x3.png);")
        self.p63.setText("")
        self.p63.setObjectName("p63")
        self.p73 = QtWidgets.QPushButton(self.frame1)
        self.p73.setGeometry(QtCore.QRect(270, 520, 111, 71))
        self.p73.setStyleSheet("background-image: url(./pictures/image7x3.png);")
        self.p73.setText("")
        self.p73.setObjectName("p73")
        self.p54 = QtWidgets.QPushButton(self.frame1)
        self.p54.setGeometry(QtCore.QRect(380, 380, 111, 71))
        self.p54.setStyleSheet("background-image: url(./pictures/image5x4.png);")
        self.p54.setText("")
        self.p54.setObjectName("p54")
        self.p64 = QtWidgets.QPushButton(self.frame1)
        self.p64.setGeometry(QtCore.QRect(380, 450, 111, 71))
        self.p64.setStyleSheet("background-image: url(./pictures/image6x4.png);")
        self.p64.setText("")
        self.p64.setObjectName("p64")
        self.p74 = QtWidgets.QPushButton(self.frame1)
        self.p74.setGeometry(QtCore.QRect(380, 520, 111, 71))
        self.p74.setStyleSheet("background-image: url(./pictures/image7x4.png);")
        self.p74.setText("")
        self.p74.setObjectName("p74")
        self.p55 = QtWidgets.QPushButton(self.frame1)
        self.p55.setGeometry(QtCore.QRect(490, 380, 111, 71))
        self.p55.setStyleSheet("background-image: url(./pictures/image5x5.png);")
        self.p55.setText("")
        self.p55.setObjectName("p55")
        self.p65 = QtWidgets.QPushButton(self.frame1)
        self.p65.setGeometry(QtCore.QRect(490, 450, 111, 71))
        self.p65.setStyleSheet("background-image: url(./pictures/image6x5.png);")
        self.p65.setText("")
        self.p65.setObjectName("p65")
        self.p75 = QtWidgets.QPushButton(self.frame1)
        self.p75.setGeometry(QtCore.QRect(490, 520, 111, 71))
        self.p75.setStyleSheet("background-image: url(./pictures/image7x5.png);")
        self.p75.setText("")
        self.p75.setObjectName("p75")
        self.p56 = QtWidgets.QPushButton(self.frame1)
        self.p56.setGeometry(QtCore.QRect(600, 380, 111, 71))
        self.p56.setStyleSheet("background-image: url(./pictures/image5x6.png);")
        self.p56.setText("")
        self.p56.setObjectName("p56")
        self.p57 = QtWidgets.QPushButton(self.frame1)
        self.p57.setGeometry(QtCore.QRect(710, 380, 111, 71))
        self.p57.setStyleSheet("background-image: url(./pictures/image5x7.png);")
        self.p57.setText("")
        self.p57.setObjectName("p57")
        self.p58 = QtWidgets.QPushButton(self.frame1)
        self.p58.setGeometry(QtCore.QRect(820, 380, 101, 71))
        self.p58.setStyleSheet("background-image: url(./pictures/image5x8.png);")
        self.p58.setText("")
        self.p58.setObjectName("p58")
        self.p66 = QtWidgets.QPushButton(self.frame1)
        self.p66.setGeometry(QtCore.QRect(600, 450, 111, 71))
        self.p66.setStyleSheet("background-image: url(./pictures/image6x6.png);")
        self.p66.setText("")
        self.p66.setObjectName("p66")
        self.p67 = QtWidgets.QPushButton(self.frame1)
        self.p67.setGeometry(QtCore.QRect(710, 450, 111, 71))
        self.p67.setStyleSheet("background-image: url(./pictures/image6x7.png);")
        self.p67.setText("")
        self.p67.setObjectName("p67")
        self.p68 = QtWidgets.QPushButton(self.frame1)
        self.p68.setGeometry(QtCore.QRect(820, 450, 101, 71))
        self.p68.setStyleSheet("background-image: url(./pictures/image6x8.png);")
        self.p68.setText("")
        self.p68.setObjectName("p68")
        self.p76 = QtWidgets.QPushButton(self.frame1)
        self.p76.setGeometry(QtCore.QRect(600, 520, 111, 71))
        self.p76.setStyleSheet("background-image: url(./pictures/image7x6.png);")
        self.p76.setText("")
        self.p76.setObjectName("p76")
        self.p77 = QtWidgets.QPushButton(self.frame1)
        self.p77.setGeometry(QtCore.QRect(710, 520, 111, 71))
        self.p77.setStyleSheet("background-image: url(./pictures/image7x7.png);")
        self.p77.setText("")
        self.p77.setObjectName("p77")
        self.p78 = QtWidgets.QPushButton(self.frame1)
        self.p78.setGeometry(QtCore.QRect(820, 520, 101, 71))
        self.p78.setStyleSheet("background-image: url(./pictures/image7x8.png);")
        self.p78.setText("")
        self.p78.setObjectName("p78")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 21))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet("background-color: white; color: black;")

        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)

        self.home = QtWidgets.QAction(MainWindow)
        self.home.setObjectName("home")
        self.help = QtWidgets.QAction(MainWindow)
        self.help.setObjectName("help")
        self.menuOptions.addAction(self.home)
        self.home.triggered.connect(self.homePressed)
        self.home.setIcon(QtGui.QIcon('./pictures/home.png'))
        self.help.triggered.connect(self.helpPressed)
        self.help.setIcon(QtGui.QIcon('./pictures/question.png'))
        self.menuOptions.addAction(self.help)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.CalculateETA.clicked.connect(self.algorithm)
        self.p11.clicked.connect(lambda: self.print_eta(1, 1))
        self.p12.clicked.connect(lambda: self.print_eta(1, 2))
        self.p13.clicked.connect(lambda: self.print_eta(1, 3))
        self.p14.clicked.connect(lambda: self.print_eta(1, 4))
        self.p15.clicked.connect(lambda: self.print_eta(1, 5))
        self.p16.clicked.connect(lambda: self.print_eta(1, 6))
        self.p17.clicked.connect(lambda: self.print_eta(1, 7))
        self.p18.clicked.connect(lambda: self.print_eta(1, 8))
        self.p19.clicked.connect(lambda: self.print_eta(1, 9))
        self.p21.clicked.connect(lambda: self.print_eta(2, 1))
        self.p22.clicked.connect(lambda: self.print_eta(2, 2))
        self.p23.clicked.connect(lambda: self.print_eta(2, 3))
        self.p24.clicked.connect(lambda: self.print_eta(2, 4))
        self.p25.clicked.connect(lambda: self.print_eta(2, 5))
        self.p26.clicked.connect(lambda: self.print_eta(2, 6))
        self.p27.clicked.connect(lambda: self.print_eta(2, 7))
        self.p28.clicked.connect(lambda: self.print_eta(2, 8))
        self.p29.clicked.connect(lambda: self.print_eta(2, 9))
        self.p31.clicked.connect(lambda: self.print_eta(3, 1))
        self.p32.clicked.connect(lambda: self.print_eta(3, 2))
        self.p33.clicked.connect(lambda: self.print_eta(3, 3))
        self.p34.clicked.connect(lambda: self.print_eta(3, 4))
        self.p35.clicked.connect(lambda: self.print_eta(3, 5))
        self.p36.clicked.connect(lambda: self.print_eta(3, 6))
        self.p37.clicked.connect(lambda: self.print_eta(3, 7))
        self.p38.clicked.connect(lambda: self.print_eta(3, 8))
        self.p39.clicked.connect(lambda: self.print_eta(3, 9))
        self.p41.clicked.connect(lambda: self.print_eta(4, 1))
        self.p42.clicked.connect(lambda: self.print_eta(4, 2))
        self.p43.clicked.connect(lambda: self.print_eta(4, 3))
        self.p44.clicked.connect(lambda: self.print_eta(4, 4))
        self.p45.clicked.connect(lambda: self.print_eta(4, 5))
        self.p46.clicked.connect(lambda: self.print_eta(4, 6))
        self.p47.clicked.connect(lambda: self.print_eta(4, 7))
        self.p48.clicked.connect(lambda: self.print_eta(4, 8))
        self.p49.clicked.connect(lambda: self.print_eta(4, 9))
        self.p51.clicked.connect(lambda: self.print_eta(5, 1))
        self.p52.clicked.connect(lambda: self.print_eta(5, 2))
        self.p53.clicked.connect(lambda: self.print_eta(5, 3))
        self.p54.clicked.connect(lambda: self.print_eta(5, 4))
        self.p55.clicked.connect(lambda: self.print_eta(5, 5))
        self.p56.clicked.connect(lambda: self.print_eta(5, 6))
        self.p57.clicked.connect(lambda: self.print_eta(5, 7))
        self.p58.clicked.connect(lambda: self.print_eta(5, 8))
        self.p59.clicked.connect(lambda: self.print_eta(5, 9))
        self.p61.clicked.connect(lambda: self.print_eta(6, 1))
        self.p62.clicked.connect(lambda: self.print_eta(6, 2))
        self.p63.clicked.connect(lambda: self.print_eta(6, 3))
        self.p64.clicked.connect(lambda: self.print_eta(6, 4))
        self.p65.clicked.connect(lambda: self.print_eta(6, 5))
        self.p66.clicked.connect(lambda: self.print_eta(6, 6))
        self.p67.clicked.connect(lambda: self.print_eta(6, 7))
        self.p68.clicked.connect(lambda: self.print_eta(6, 8))
        self.p69.clicked.connect(lambda: self.print_eta(6, 9))
        self.p71.clicked.connect(lambda: self.print_eta(7, 1))
        self.p72.clicked.connect(lambda: self.print_eta(7, 2))
        self.p73.clicked.connect(lambda: self.print_eta(7, 3))
        self.p74.clicked.connect(lambda: self.print_eta(7, 4))
        self.p75.clicked.connect(lambda: self.print_eta(7, 5))
        self.p76.clicked.connect(lambda: self.print_eta(7, 6))
        self.p77.clicked.connect(lambda: self.print_eta(7, 7))
        self.p78.clicked.connect(lambda: self.print_eta(7, 8))
        self.p79.clicked.connect(lambda: self.print_eta(7, 9))

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
        msg.setWindowTitle("Help: Emergency Management")
        msg.setText("How to use Emergency Management window described")
        msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Emergency Management"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.home.setText(_translate("MainWindow", "Home"))
        self.help.setText(_translate("MainWindow", "Help"))
        self.label.setText(_translate("MainWindow", "Emergency Management"))
        self.CalculateETA.setText(_translate("MainWindow", "Calculate ETA"))
        self.ClickMe.setText(_translate("MainWindow", "Click where the emergency is happening"))
        self.Result.setText(_translate("MainWindow", " ETA(min) *"))

    def algorithm(self):
        temp_mat = self.mat
        m = len(temp_mat)
        n = len(temp_mat[0])

        for _ in range(2):
            for r in range(m):
                for c in range(n):
                    if temp_mat[r][c] > 0:
                        left = float('inf')
                        right = float('inf')
                        up = float('inf')
                        down = float('inf')
                        if (c != 0):
                            left = temp_mat[r][c - 1]
                        if (c != n - 1):
                            right = temp_mat[r][c + 1]
                        if (r != 0):
                            up = temp_mat[r - 1][c]
                        if (r != m - 1):
                            down = temp_mat[r + 1][c]
                        temp_mat[r][c] = min(left, right, up, down) + 1
        self.mat = temp_mat

    def print_eta(self, i, j):
        x = self.mat[i - 1][j - 1]
        if(x == 0):
            x = 0.15
        t = str(x)
        self.Result.setText(t)
        


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
