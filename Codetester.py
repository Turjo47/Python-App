import os
import sys 
import sqlite3
# from ui_input import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton,QTextBrowser,QMenuBar,QMenu,QAction,QStatusBar,QLineEdit,QWidget,QDialog,QTableWidget
from PyQt5.uic import loadUi

con = sqlite3.connect('attendence.bd')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS infos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            port TEXT,
            api TEXT
            )''')
            # # con.commit()
con.commit()
con.close()



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
        # Ip= self.Ip_lineEdit.text()
        # Port=self.Port_lineEdit.text()
        # Api=self.Api_lineEdit.text()
        self.okButton.clicked.connect(self.passinfo)
        self.saveButton.clicked.connect(self.save_it)
        # self.serverwindow = ServerWindow()
    def passinfo(self):
        widget.setFixedSize(400,450)
        widget.setCurrentIndex(widget.currentIndex()-1)
        # self.serverwindow.displayinfo()
    def save_it(self):
        con = sqlite3.connect('attendence.bd')
        cur = con.cursor() 
        users =[]
        for index in range(self.Ip_lineEdit):
            users.append(self.Ip_llineEdit.users(index))
        for user in users:
            cur.execute("INSERT INTO infos VALUES(:user)",
                       {
                        'user':user.text(),
                        }
                        )
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
   