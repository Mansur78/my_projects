# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ionaspeak.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 600)
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setItalic(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #4A8AF4;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ion = QtWidgets.QLabel(self.centralwidget)
        self.ion.setGeometry(QtCore.QRect(20, 0, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.ion.setFont(font)
        self.ion.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.ion.setStyleSheet("color:red;")
        self.ion.setObjectName("ion")
        self.sto = QtWidgets.QPushButton(self.centralwidget)
        self.sto.setGeometry(QtCore.QRect(670, 520, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sto.setFont(font)
        self.sto.setStyleSheet("QPushButton{\n"
                               "font: ;\n"
                               "background-color: #ACCFE3;\n"
                               "color: #080A12;\n"
                               "}\n"
                               "QPushButton:hover{\n"
                               "font: ;\n"
                               "background-color: red;\n"
                               "\n"
                               "}")
        self.sto.setObjectName("sto")
        self.St = QtWidgets.QPushButton(self.centralwidget)
        self.St.setGeometry(QtCore.QRect(540, 520, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.St.setFont(font)
        self.St.setStyleSheet("QPushButton{\n"
                              "font: ;\n"
                              "background-color: #ACCFE3;\n"
                              "color: #080A12;\n"
                              "}\n"
                              "QPushButton:hover{\n"
                              "font: ;\n"
                              "background-color: red;\n"
                              "\n"
                              "}")
        self.St.setObjectName("St")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 781, 481))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: #E5F0F7;")
        self.textEdit.setObjectName("textEdit")
        self.ing = QtWidgets.QLabel(self.centralwidget)
        self.ing.setGeometry(QtCore.QRect(20, 530, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(True)
        self.ing.setFont(font)
        self.ing.setStyleSheet("color:red;\n"
                               " ")
        self.ing.setObjectName("ing")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ion.setText(_translate("MainWindow", "@Iona"))
        self.sto.setText(_translate("MainWindow", "Stop"))
        self.St.setText(_translate("MainWindow", "Start"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.ing.setText(_translate("MainWindow", "In God We Trust"))
