from math import radians
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import random

# 创建ui界面
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 677)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(830, 540, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(950, 540, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(120, 290, 115, 19))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(120, 340, 115, 19))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(120, 390, 115, 19))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(120, 440, 115, 19))
        self.radioButton_4.setObjectName("radioButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 280, 851, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 330, 851, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 380, 851, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 430, 851, 31))
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 540, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(710, 540, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 490, 271, 31))
        self.label_5.setObjectName("label_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(120, 50, 931, 211))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1123, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        self.pushButton.clicked.connect(self.onSubmmit)
        self.pushButton_2.clicked.connect(self.onClicked)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.prepareQuiz()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "练习"))
        self.pushButton.setText(_translate("MainWindow", "确认"))
        self.pushButton_2.setText(_translate("MainWindow", "下一题"))
        self.pushButton_3.setText(_translate("MainWindow", "从头开始"))
        self.pushButton_4.setText(_translate("MainWindow", "上一题"))
        self.radioButton.setText(_translate("MainWindow", "A"))
        self.radioButton_2.setText(_translate("MainWindow", "B"))
        self.radioButton_3.setText(_translate("MainWindow", "C"))
        self.radioButton_4.setText(_translate("MainWindow", "D"))

    current_ans = ""

    def onClicked(self):
        self.prepareQuiz()

    def onSubmmit(self):
        _translate = QtCore.QCoreApplication.translate

        ans = ""
        if self.radioButton.isChecked():
            ans = "A"
            print("checked A")
        elif self.radioButton_2.isChecked():
            ans = "B"
            print("checked B")

        elif self.radioButton_3.isChecked():
            ans = "C"
            print("checked C")
        elif self.radioButton_4.isChecked():
            ans = "D"
            print("checked D")
        print("ans is ", ans, "right ans is", self.current_ans)
        if ans.strip() == self.current_ans.strip():
            print("right")
            self.textBrowser.setText(_translate("MainWindow", "right"))
        else:
            print("shit")
            self.textBrowser.setText(_translate("MainWindow", "shit"))




    def getRandomQuizNum(self, range):
        return random.randint(1, range)

    def prepareQuiz(self):
        print("hello??")
        # 读取题目文本material
        test = open("material.txt", "r", encoding='utf-8')
        _translate = QtCore.QCoreApplication.translate

        quizIndex = self.getRandomQuizNum(124)
        count = (quizIndex - 1) * 6 + 1
        for i in range(1, count):
            line = test.readline()
        quiz = "".join(test.readline())
        ansA = "".join(test.readline())
        ansB = "".join(test.readline())
        ansC = "".join(test.readline())
        ansD = "".join(test.readline())

        correctAns = "".join(test.readline())
        print("correctAns is ",correctAns,"and len is",len(correctAns))
        self.current_ans = correctAns[len(correctAns) -2]
        print("currentans is ",self.current_ans)

        self.textBrowser.setText(_translate("MainWindow", quiz))
        self.label.setText(_translate("MainWindow", ansA))
        self.label_2.setText(_translate("MainWindow", ansB))
        self.label_3.setText(_translate("MainWindow", ansC))
        self.label_4.setText(_translate("MainWindow", ansD))
        self.label_5.setText(_translate("MainWindow", self.current_ans))
        test.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow1 = QMainWindow()  # MainWindow1随便改
    ui = Ui_MainWindow()  # 随便改
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())
