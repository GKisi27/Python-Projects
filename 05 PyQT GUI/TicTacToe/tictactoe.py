# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tictactoe.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import main_icon, reload_icon


class Ui_TicTacToeWindow(object):
    def setupUi(self, TicTacToeWindow):
        TicTacToeWindow.setObjectName("TicTacToeWindow")
        TicTacToeWindow.resize(500, 650)
        TicTacToeWindow.setMinimumSize(QtCore.QSize(500, 650))
        TicTacToeWindow.setMaximumSize(QtCore.QSize(500, 650))
        TicTacToeWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        TicTacToeWindow.setWindowIcon(QtGui.QIcon(':/tictactoe.png'))
        TicTacToeWindow.setIconSize(QtCore.QSize(50, 50))
        self.centralwidget = QtWidgets.QWidget(TicTacToeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.button1.sizePolicy().hasHeightForWidth())
        self.button1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.button1.setFont(font)
        self.button1.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n"
"QPushButton:hover{color: rgb(255, 255, 255);\n"
"background-color: rgb(100,100,100);\n"
"border-color: rgb(25,25,25);\n"
"border-radius: 20px;\n"
"border :3px solid;}\n"
"\n"
"QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"")
        self.button1.setText("")
        self.button1.setObjectName("button1")
        self.gridLayout.addWidget(self.button1, 1, 0, 1, 1)
        self.button7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.button7.sizePolicy().hasHeightForWidth())
        self.button7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(30)
        font.setBold(True)
        self.button7.setFont(font)
        self.button7.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n"
"QPushButton:hover{color: rgb(255, 255, 255);\n"
"background-color: rgb(100,100,100);\n"
"border-color: rgb(25,25,25);\n"
"border-radius: 20px;\n"
"border :3px solid;}\n"
"\n"
"QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"")
        self.button7.setText("")
        self.button7.setObjectName("button7")
        self.gridLayout.addWidget(self.button7, 3, 0, 1, 1)
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.button3.sizePolicy().hasHeightForWidth())
        self.button3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.button3.setFont(font)
        self.button3.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n"
"QPushButton:hover{color: rgb(255, 255, 255);\n"
"background-color: rgb(100,100,100);\n"
"border-color: rgb(25,25,25);\n"
"border-radius: 20px;\n"
"border :3px solid;}\n"
"\n"
"QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"")
        self.button3.setText("")
        self.button3.setObjectName("button3")
        self.gridLayout.addWidget(self.button3, 1, 2, 1, 1)
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.button4.sizePolicy().hasHeightForWidth())
        self.button4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(30)
        font.setBold(True)
        self.button4.setFont(font)
        self.button4.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n"
"QPushButton:hover{color: rgb(255, 255, 255);\n"
"background-color: rgb(100,100,100);\n"
"border-color: rgb(25,25,25);\n"
"border-radius: 20px;\n"
"border :3px solid;}\n"
"\n"
"QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"")
        self.button4.setText("")
        self.button4.setObjectName("button4")
        self.gridLayout.addWidget(self.button4, 2, 0, 1, 1)
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.button2.sizePolicy().hasHeightForWidth())
        self.button2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.button2.setFont(font)
        self.button2.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n"
"QPushButton:hover{color: rgb(255, 255, 255);\n"
"background-color: rgb(100,100,100);\n"
"border-color: rgb(25,25,25);\n"
"border-radius: 20px;\n"
"border :3px solid;}\n"
"\n"
"QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"")
        self.button2.setText("")
        self.button2.setObjectName("button2")
        self.gridLayout.addWidget(self.button2, 1, 1, 1, 1)
        self.button8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.button8.sizePolicy().hasHeightForWidth())
        self.button8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(30)
        font.setBold(True)
        self.button8.setFont(font)
        self.button8.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n"
"QPushButton:hover{color: rgb(255, 255, 255);\n"
"background-color: rgb(100,100,100);\n"
"border-color: rgb(25,25,25);\n"
"border-radius: 20px;\n"
"border :3px solid;}\n"
"\n"
"QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"")
        self.button8.setText("")
        self.button8.setObjectName("button8")
        self.gridLayout.addWidget(self.button8, 3, 1, 1, 1)
        self.button9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.button9.sizePolicy().hasHeightForWidth())
        self.button9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(30)
        font.setBold(True)
        self.button9.setFont(font)
        self.button9.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n"
"QPushButton:hover{color: rgb(255, 255, 255);\n"
"background-color: rgb(100,100,100);\n"
"border-color: rgb(25,25,25);\n"
"border-radius: 20px;\n"
"border :3px solid;}\n"
"\n"
"QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"")
        self.button9.setText("")
        self.button9.setObjectName("button9")
        self.gridLayout.addWidget(self.button9, 3, 2, 1, 1)
        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.button6.sizePolicy().hasHeightForWidth())
        self.button6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(30)
        font.setBold(True)
        self.button6.setFont(font)
        self.button6.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n"
"QPushButton:hover{color: rgb(255, 255, 255);\n"
"background-color: rgb(100,100,100);\n"
"border-color: rgb(25,25,25);\n"
"border-radius: 20px;\n"
"border :3px solid;}\n"
"\n"
"QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"")
        self.button6.setText("")
        self.button6.setObjectName("button6")
        self.gridLayout.addWidget(self.button6, 2, 2, 1, 1)
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.reset_button.sizePolicy().hasHeightForWidth())
        self.reset_button.setSizePolicy(sizePolicy)
        self.reset_button.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n"
"QPushButton:hover{color: rgb(255, 255, 255);\n"
"background-color: rgb(100,100,100);\n"
"border-color: rgb(25,25,25);\n"
"border-radius: 20px;\n"
"border :3px solid;}\n"
"\n"
"QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"")
        self.reset_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset_button.setIcon(icon)
        self.reset_button.setIconSize(QtCore.QSize(50, 50))
        self.reset_button.setObjectName("reset_button")
        self.gridLayout.addWidget(self.reset_button, 4, 1, 1, 1)
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.button5.sizePolicy().hasHeightForWidth())
        self.button5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(30)
        font.setBold(True)
        self.button5.setFont(font)
        self.button5.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n"
"QPushButton:hover{color: rgb(255, 255, 255);\n"
"background-color: rgb(100,100,100);\n"
"border-color: rgb(25,25,25);\n"
"border-radius: 20px;\n"
"border :3px solid;}\n"
"\n"
"QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"")
        self.button5.setText("")
        self.button5.setObjectName("button5")
        self.gridLayout.addWidget(self.button5, 2, 1, 1, 1)
        self.turn_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.turn_label.sizePolicy().hasHeightForWidth())
        self.turn_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.turn_label.setFont(font)
        self.turn_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.turn_label.setAlignment(QtCore.Qt.AlignCenter)
        self.turn_label.setObjectName("turn_label")
        self.gridLayout.addWidget(self.turn_label, 0, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)
        TicTacToeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TicTacToeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        TicTacToeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TicTacToeWindow)
        self.statusbar.setObjectName("statusbar")
        TicTacToeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TicTacToeWindow)
        QtCore.QMetaObject.connectSlotsByName(TicTacToeWindow)

        self.player = "X"
        self.button1.clicked.connect(lambda: self.button_method(self.button1))
        self.button2.clicked.connect(lambda: self.button_method(self.button2))
        self.button3.clicked.connect(lambda: self.button_method(self.button3))
        self.button4.clicked.connect(lambda: self.button_method(self.button4))
        self.button5.clicked.connect(lambda: self.button_method(self.button5))
        self.button6.clicked.connect(lambda: self.button_method(self.button6))
        self.button7.clicked.connect(lambda: self.button_method(self.button7))
        self.button8.clicked.connect(lambda: self.button_method(self.button8))
        self.button9.clicked.connect(lambda: self.button_method(self.button9))
        self.reset_button.clicked.connect(self.reset_method)


    def reset_method(self):
        #Reset player
        self.player = "X"
        self.turn_label.setText(self.player + "'s Turn")

        #Set all buttons text to ""
        self.button1.setText("")
        self.button2.setText("")
        self.button3.setText("")
        self.button4.setText("")
        self.button5.setText("")
        self.button6.setText("")
        self.button7.setText("")
        self.button8.setText("")
        self.button9.setText("")

        #Set all buttons enable
        self.button1.setEnabled(True)
        self.button2.setEnabled(True)
        self.button3.setEnabled(True)
        self.button4.setEnabled(True)
        self.button5.setEnabled(True)
        self.button6.setEnabled(True)
        self.button7.setEnabled(True)
        self.button8.setEnabled(True)
        self.button9.setEnabled(True)

        #Reset background color
        self.button1.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n")
        self.button2.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n")
        self.button3.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n")
        self.button4.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n")
        self.button5.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n")
        self.button6.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n")
        self.button7.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n")
        self.button8.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n")
        self.button9.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(67, 67, 67);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n")

    def update_button_text(self):
        self.btn1_text = self.button1.text()
        self.btn2_text = self.button2.text()
        self.btn3_text = self.button3.text()
        self.btn4_text = self.button4.text()
        self.btn5_text = self.button5.text()
        self.btn6_text = self.button6.text()
        self.btn7_text = self.button7.text()
        self.btn8_text = self.button8.text()
        self.btn9_text = self.button9.text()

    def disable_button(self):
        self.button1.setDisabled(True)
        self.button2.setDisabled(True)
        self.button3.setDisabled(True)
        self.button4.setDisabled(True)
        self.button5.setDisabled(True)
        self.button6.setDisabled(True)
        self.button7.setDisabled(True)
        self.button8.setDisabled(True)
        self.button9.setDisabled(True)

    def declare_winner(self):
        if self.winner[0] == True:
            self.winner[1].setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 110, 168);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n")
            self.winner[2].setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 110, 168);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n")
            self.winner[3].setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 110, 168);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n")
            self.turn_label.setText(self.winner[1].text() + " Won")
            self.disable_button()


    def check_for_winner(self):
        #Check Rows
        if self.btn1_text == self.btn2_text == self.btn3_text != "":
            return True, self.button1, self.button2, self.button3
        if self.btn4_text == self.btn5_text == self.btn6_text != "":
            return True, self.button4, self.button5, self.button6
        if self.btn7_text == self.btn8_text == self.btn9_text != "":
            return True, self.button7, self.button8, self.button9

        #Check Columns
        if self.btn1_text == self.btn4_text == self.btn7_text != "":
            return True, self.button1, self.button4, self.button7
        if self.btn2_text == self.btn5_text == self.btn8_text != "":
            return True, self.button2, self.button5, self.button8
        if self.btn3_text == self.btn6_text == self.btn9_text != "":
            return True, self.button3, self.button6, self.button9

        #Check Diagonal
        if self.btn1_text == self.btn5_text == self.btn9_text != "":
            return True, self.button1, self.button5, self.button9
        if self.btn3_text == self.btn5_text == self.btn7_text != "":
            return True, self.button3, self.button5, self.button7

    def check_for_draw(self):
        if self.btn1_text != "" and self.btn2_text != "" and self.btn3_text != "" and self.btn4_text != "" and self.btn5_text != "" and self.btn6_text != "" and self.btn7_text != "" and self.btn8_text != "" and self.btn9_text != "":
            return True


    def button_method(self, btn):
        btn.setText(self.player)
        btn.setDisabled(True)
        self.update_button_text()
        self.switch_player()
        self.turn_label.setText(self.player + "'s Turn")
        self.winner = self.check_for_winner()
        if self.winner != None:
             self.declare_winner()
        else:
            self.draw = self.check_for_draw()
            if self.draw:
                self.turn_label.setText("It's Draw")
                self.button1.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(252,49,69);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n")
                self.button2.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(252,49,69);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n")
                self.button3.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(252,49,69);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n")
                self.button4.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(252,49,69);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n")
                self.button5.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(252,49,69);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n")
                self.button6.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(252,49,69);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n")
                self.button7.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(252,49,69);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n")
                self.button8.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(252,49,69);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n")
                self.button9.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(252,49,69);\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 20px;\n"
"border :4px solid;}\n"
"\n")
                self.disable_button()


    def switch_player(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"




    def retranslateUi(self, TicTacToeWindow):
        _translate = QtCore.QCoreApplication.translate
        TicTacToeWindow.setWindowTitle(_translate("TicTacToeWindow", "MainWindow"))
        self.turn_label.setText(_translate("TicTacToeWindow", "X\'s Turn"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TicTacToeWindow = QtWidgets.QMainWindow()
    ui = Ui_TicTacToeWindow()
    ui.setupUi(TicTacToeWindow)
    TicTacToeWindow.show()
    sys.exit(app.exec_())
