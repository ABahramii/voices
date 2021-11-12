from PyQt5 import QtCore, QtGui, QtWidgets
import audio

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 270)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelEnter = QtWidgets.QLabel(self.centralwidget)
        self.labelEnter.setGeometry(QtCore.QRect(80, 60, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelEnter.setFont(font)
        self.labelEnter.setObjectName("labelEnter")
        self.labelEnter.setStyleSheet("color: darkblue;")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(280, 70, 121, 31))
        self.startButton.setStyleSheet("background-color: #009191; color: #fff; border-radius: 12px;")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(80, 150, 191, 51))
        self.labelResult.setStyleSheet("color: darkblue;")
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelResult.setFont(font)
        self.labelResult.setObjectName("labelResult")
        self.avgFrameRate = QtWidgets.QLabel(self.centralwidget)
        self.avgFrameRate.setGeometry(QtCore.QRect(290, 150, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.avgFrameRate.setFont(font)
        self.avgFrameRate.setObjectName("avgFrameRate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # when START Button clicked
        self.startButton.clicked.connect(self.startClicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voices"))
        self.labelEnter.setText(_translate("MainWindow", "Voice streaming"))
        self.startButton.setText(_translate("MainWindow", "start"))
        self.labelResult.setText(_translate("MainWindow", "Avetage frame rate"))
        self.avgFrameRate.setText(_translate("MainWindow", ""))

    def startClicked(self):
        res = audio.start()
        self.avgFrameRate.setText(res)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
