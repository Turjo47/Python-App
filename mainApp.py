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
        self.displayinfo
        
    def displayinfo(self):
        widget.setFixedSize(400,180)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.show()
    
class InputWindow(QMainWindow):       
    def __init__(self):
        super(InputWindow,self).__init__()
        loadUi("input.ui",self)
        self.serverwindow=ServerWindow()
        self.okButton.clicked.connect(self.passinfo)
        self.saveButton.clicked.connect(self.add_database)
        self.serverwindow = ServerWindow()
    def passinfo(self):
        widget.setFixedSize(400,450)
        widget.setCurrentIndex(widget.currentIndex()-1)
        # self.serverwindow.displayinfo()
    def add_database(self):
        try:
            con = sqlite3.connect('attendence.bd')
            cur = con.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS infos(
            ip TEXT,
            port INTEGER,
            api TEXT
            )''')
            # con.commit()
            # print(ip+port+api)
            cur.exeute("INSERT INTO infos (ip,port,api) VALUES ('%s','%s','%s'')" % ( ''.join(self.Ip_lineEdit.text()),
                                                                                  ''.join(self.Port_lineEdit.int()),
                                                                                  ''.join(self.Api_lineEdit.text())))
            con.commit()
            con.close()
        except:
            pass
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