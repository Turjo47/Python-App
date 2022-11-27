import os
import sys 
import sqlite3
# from ui_input import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton,QTextBrowser,QMenuBar,QMenu,QAction,QStatusBar,QLineEdit,QWidget,QDialog,QTableWidget
from PyQt5.uic import loadUi


class ServerWindow(QMainWindow):
    def __init__(self):
        super(ServerWindow,self).__init__()
        loadUi("localserver.ui",self)
        self.actionAdd_New.triggered.connect(self.add_bd)
        self.add_bd()
        
    def add_bd(self):
        widget.setFixedSize(400,180)
        # con = sqlite3.connect('attendence.bd')
        # cur = con.cursor()
        # cur.execute('''CREATE TABLE IF NOT EXISTS infos(
        #     id INTEGER PRIMARY KEY AUTOINCREMENT,
        #     ip TEXT,
        #     port TEXT,
        #     api TEXT
        #     )''')
        # con.commit()
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.show()
    
class InputWindow(QMainWindow):       
    def __init__(self):
        super(InputWindow,self).__init__()
        loadUi("input.ui",self)
        # self.serverwindow=ServerWindow()
        Ip= self.Ip_lineEdit.text()
        Port=self.Port_lineEdit.text()
        Api=self.Api_lineEdit.text()
        self.okButton.clicked.connect(self.passinfo)
        self.saveButton.clicked.connect(self.add_database)
        # self.serverwindow = ServerWindow()
    def passinfo(self):
        widget.setFixedSize(400,450)
        
        widget.setCurrentIndex(widget.currentIndex()-1)
        # self.serverwindow.displayinfo()
    def add_database(self):
        
            con = sqlite3.connect('attendence.bd')
            cur = con.cursor()
            users= cur.execute('''CREATE TABLE if not exists infos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT NOT NULL,
            port TEXT NOT NULL,
            api TEXT NOT NULL
            )''')
            # # con.commit()
            sql= """INSERT INTO infos(ip,port,api) VALUES (?,?,?)"""
            cur.execute(sql)
            cur.execute("SELECT rowwid,* FORM infos")
            items = cur.fetchall()
            for item in items:
                print(items)
            con.commit()
            con.close()
        
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
   