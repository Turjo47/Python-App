# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\Laptop\RajIT Project\attendence app\Python App\Backup\localserver.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LocalserverWindow(object):
    def setupUi(self, LocalserverWindow):
        LocalserverWindow.setObjectName("LocalserverWindow")
        LocalserverWindow.resize(364, 437)
        LocalserverWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(LocalserverWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 380, 121, 16))
        self.label_4.setObjectName("label_4")
        self.syncButton = QtWidgets.QPushButton(self.centralwidget)
        self.syncButton.setGeometry(QtCore.QRect(260, 0, 75, 23))
        self.syncButton.setStyleSheet("")
        self.syncButton.setObjectName("syncButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 30, 321, 341))
        self.tableWidget.setMaximumSize(QtCore.QSize(331, 16777215))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        LocalserverWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LocalserverWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 364, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        LocalserverWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LocalserverWindow)
        self.statusbar.setObjectName("statusbar")
        LocalserverWindow.setStatusBar(self.statusbar)
        self.actionVersion = QtWidgets.QAction(LocalserverWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.actionConfigaration = QtWidgets.QAction(LocalserverWindow)
        self.actionConfigaration.setObjectName("actionConfigaration")
        self.actionAdd_New = QtWidgets.QAction(LocalserverWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("f:\\Laptop\\RajIT Project\\attendence app\\Python App\\Backup\\fugue-icons-3.5.6/icons/plus-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_New.setIcon(icon)
        self.actionAdd_New.setObjectName("actionAdd_New")
        self.actionSave = QtWidgets.QAction(LocalserverWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("f:\\Laptop\\RajIT Project\\attendence app\\Python App\\Backup\\fugue-icons-3.5.6/icons/document-sub.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.setObjectName("actionSave")
        self.action_list = QtWidgets.QAction(LocalserverWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("f:\\Laptop\\RajIT Project\\attendence app\\Python App\\Backup\\fugue-icons-3.5.6/icons/document-share.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_list.setIcon(icon2)
        self.action_list.setObjectName("action_list")
        self.actionConfigaration_2 = QtWidgets.QAction(LocalserverWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("f:\\Laptop\\RajIT Project\\attendence app\\Python App\\Backup\\fugue-icons-3.5.6/icons/hammer-screwdriver.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfigaration_2.setIcon(icon3)
        self.actionConfigaration_2.setObjectName("actionConfigaration_2")
        self.actionVersion_2 = QtWidgets.QAction(LocalserverWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("f:\\Laptop\\RajIT Project\\attendence app\\Python App\\Backup\\fugue-icons-3.5.6/icons/paper-plane--pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVersion_2.setIcon(icon4)
        self.actionVersion_2.setObjectName("actionVersion_2")
        self.actionStatus = QtWidgets.QAction(LocalserverWindow)
        self.actionStatus.setObjectName("actionStatus")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionStatus)
        self.menuFile.addAction(self.actionAdd_New)
        self.menuFile.addAction(self.action_list)
        self.menuSetting.addAction(self.actionConfigaration_2)
        self.menuAbout.addAction(self.actionVersion_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(LocalserverWindow)
        QtCore.QMetaObject.connectSlotsByName(LocalserverWindow)

    def retranslateUi(self, LocalserverWindow):
        _translate = QtCore.QCoreApplication.translate
        LocalserverWindow.setWindowTitle(_translate("LocalserverWindow", "Easy Attendence Management Local Server"))
        self.label_4.setText(_translate("LocalserverWindow", "Powerd By rajIT Ltd."))
        self.syncButton.setText(_translate("LocalserverWindow", "Sync"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("LocalserverWindow", "IP"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("LocalserverWindow", "Status"))
        self.menuFile.setTitle(_translate("LocalserverWindow", "File"))
        self.menuSetting.setTitle(_translate("LocalserverWindow", "Setting"))
        self.menuAbout.setTitle(_translate("LocalserverWindow", "About"))
        self.actionVersion.setText(_translate("LocalserverWindow", "Version"))
        self.actionConfigaration.setText(_translate("LocalserverWindow", "Configaration"))
        self.actionAdd_New.setText(_translate("LocalserverWindow", "Add New Device"))
        self.actionSave.setText(_translate("LocalserverWindow", "Save"))
        self.action_list.setText(_translate("LocalserverWindow", "Device List"))
        self.actionConfigaration_2.setText(_translate("LocalserverWindow", "Configaration"))
        self.actionVersion_2.setText(_translate("LocalserverWindow", "Version"))
        self.actionStatus.setText(_translate("LocalserverWindow", "Status"))
