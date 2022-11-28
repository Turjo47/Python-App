import os
import sys 
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton,QTextBrowser,QMenuBar,QMenu,QAction,QStatusBar,QLineEdit,QWidget,QDialog,QTableWidget
from PyQt5.uic import loadUi


class ServerWindow(QMainWindow):
    def __init__(self):
        super(ServerWindow,self).__init__()
        loadUi("localserver.ui",self)
        self.actionAdd_New.triggered.connect(self.displayinfo)
        
        self.displayinfo()
        
    def displayinfo(self):
        widget.setFixedSize(400,180)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.show()
    
class InputWindow(QMainWindow):       
    def __init__(self):
        super(InputWindow,self).__init__()
        loadUi("input.ui",self)
        # self.serverwindow=ServerWindow()
        
        self.saveButton.clicked.connect(self.add_database)
        self.okButton.clicked.connect(self.passinfo)
        
    def passinfo(self):
        widget.setFixedSize(400,450)
        widget.setCurrentIndex(widget.currentIndex()-1)
    def add_database(self):
        ip = self.Ip_lineEdit.text()
        port =self.Port_lineEdit.text()
        api =self.Api_lineEdit.text()
        con = sqlite3.connect('attendence.bd')
        cur = con.cursor()
        users= cur.execute('''CREATE TABLE if not exists infos(Ip TEXT ,Port TEXT ,Api TEXT)''')
        cur.execute("INSERT INTO infos (Ip,Port,Api) VALUES(?,?,?)",(ip,port,api))
        con.commit()
        con.close
    
        
if __name__ == '__main__':        
#main
    app = QApplication(sys.argv)
    widget= QtWidgets.QStackedWidget()
    serverwindow = ServerWindow()
    inputwindow = InputWindow()
    widget.addWidget(serverwindow)
    widget.addWidget(inputwindow)
    widget.setFixedSize(400,450)
    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
    