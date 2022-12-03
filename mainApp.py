import os
import sys 
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton,QTextBrowser,QMenuBar,QMenu,QAction,QStatusBar,QLineEdit,QWidget,QDialog,QTableWidget,QTableWidgetItem
from PyQt5.uic import loadUi



class ServerWindow(QMainWindow):
    def __init__(self):
        super(ServerWindow,self).__init__()
        loadUi("localserver.ui",self)
        self.tableWidget.setColumnWidth(0,150)
        self.tableWidget.setColumnWidth(1,150)
        self.loaddata()
        self.actionStatus.triggered.connect(self.dlist)
        self.actionAdd_New.triggered.connect(self.displayinfo)
        self.RefreshBtn.clicked.connect(self.loaddata)
        # self.versionAction.triggered.connect(self.version)
        # self.displayinfo()
        # self.dlist()
    def loaddata(self):
        # ip = self.Ip_lineEdit.text()
        # port =self.Port_lineEdit.text()
        con = sqlite3.connect('attendence.bd')
        cur= con.cursor()
        users= cur.execute('''CREATE TABLE if not exists infos(Ip TEXT ,Port TEXT, Api Text, Status Integer,Edit Null)''')
        
        sqlquery ="SELECT Ip FROM infos"
        self.tableWidget.setRowCount(50)
        tablerow = 0 
        for row in cur.execute(sqlquery):
            self.tableWidget.setItem(tablerow,0, QtWidgets.QTableWidgetItem(row[0]))
            # self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            tablerow+=1
    def displayinfo(self):
        widget.setFixedSize(400,180)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def dlist(self):
        self.devicelist=Devicelist()
        self.devicelist.status()
        widget.setFixedSize(554,436)
        widget.setCurrentIndex(widget.currentIndex()+2)
    # def delete(self):
    #     con = sqlite3.connect('attendence.bd')
    #     cur = con.cursor()
    #     ip = self.Ip_lineEdit.text()
    #     del_ = "DELETE FORM infos WHERE rowid=1"
    #     cur.execute(del_)
         
    # def version(self):
    #     widget.setFixedSize(450,420)
    #     widget.setCurrentIndex(widget.currentIndex()+3)   
            
class InputWindow(QMainWindow):
    def __init__(self):
        super(InputWindow,self).__init__()
        loadUi("input.ui",self)
        self.saveButton.clicked.connect(self.add_database)
        self.okButton.clicked.connect(self.passinfo)

    def passinfo(self):
        widget.setFixedSize(342,437)
        widget.setCurrentIndex(widget.currentIndex()-1)
        
    def add_database(self):
        
        ip = self.Ip_lineEdit.text()
        port =self.Port_lineEdit.text()
        api = self.Api_lineEdit.text()
        con = sqlite3.connect('attendence.bd')
        cur = con.cursor()
        # users= cur.execute('''CREATE TABLE if not exists infos(Ip TEXT ,Port TEXT )''')
        cur.execute("INSERT INTO infos (Ip,Port,Api) VALUES(?,?,?)",(ip,port,api))
        con.commit()
        self.Ip_lineEdit.setText('')
        self.Port_lineEdit.setText('')
        self.Api_lineEdit.setText('')
        con.close()
class Devicelist(QMainWindow):
    def __init__(self):
        super(Devicelist,self).__init__()
        loadUi("deviceList.ui",self)
        self.status()
        # self.show()
        self.closebtn.clicked.connect(self.close)
        # self.show()
        
    def close(self):
        widget.setFixedSize(380,450)
        widget.setCurrentIndex(widget.currentIndex()-2)
    def status(self):
        con = sqlite3.connect('attendence.bd')
        cur= con.cursor()
        sqlquery ="SELECT * FROM infos"
        self.tableWidget.setRowCount(50)
        tablerow = 0 
        for row in cur.execute(sqlquery):
            self.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
            tablerow+=1
# class Version(QMainWindow):
#     def __init__(self):
#         super(Version,self).__init__()
#         loadUi("Version.ui",self)
#         self.closeButton.clicked.connect(self.closeV)    
        
    # def closeV(self):
    #     widget.setFixedSize(380,450)
    #     widget.setCurrentIndex(widget.currentIndex()-2)
        
    
    
        
if __name__ == '__main__':        
#main
    app = QApplication(sys.argv)
    widget= QtWidgets.QStackedWidget()
    serverwindow = ServerWindow()
    inputwindow = InputWindow()
    devicelist= Devicelist()
    # version = Version()
    
    widget.addWidget(serverwindow)
    widget.addWidget(inputwindow)
    widget.addWidget(devicelist)
    # widget.addWidget(version)
    widget.setFixedSize(342,437)
    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
