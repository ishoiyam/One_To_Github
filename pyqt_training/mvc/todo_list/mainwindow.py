# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 535)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.todoView = QtWidgets.QListView(self.centralwidget)
        self.todoView.setGeometry(QtCore.QRect(10, 10, 451, 241))
        self.todoView.setObjectName("todoView")
        self.completeButton = QtWidgets.QPushButton(self.centralwidget)
        self.completeButton.setGeometry(QtCore.QRect(259, 270, 181, 51))
        self.completeButton.setObjectName("completeButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(40, 270, 181, 51))
        self.deleteButton.setObjectName("deleteButton")
        self.todoEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.todoEdit.setGeometry(QtCore.QRect(12, 360, 451, 51))
        self.todoEdit.setObjectName("todoEdit")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(10, 420, 451, 51))
        self.addButton.setObjectName("addButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 476, 27))
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
        self.completeButton.setText(_translate("MainWindow", "Complete"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.addButton.setText(_translate("MainWindow", "Add Todo"))
