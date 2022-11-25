import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton,QTextBrowser,QMenuBar,QMenu,QAction,QStatusBar,QLineEdit,QWidget,QDialog,QTableWidget
from PyQt5.uic import loadUi


class ServerWindow(QMainWindow):
    def __init__(self):
        super(ServerWindow,self).__init__()
        loadUi("localserver.ui",self)
        self.actionAdd_New.triggered.connect(self.displayinfo)
        self.load_info
        # self.inputinfo= InputWindow()
        
    def displayinfo(self):
        widget.setFixedSize(400,180)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.show()
    def load_info(self):
        
        infos=[{"IP":self.Ip_lineEdit.show(),"Port":self.Port_lineEdit.show(),"API":self.Api_lineEdit.show()}]
        row= 0
        self.tableWidget.setRowCount(len(infos))
        for info in infos:
            self.tableWidget.setItem(row,0, QtWidgets.QTableWidgetItem(info["IP"]))
            self.tableWidget.setItem(row,1, QtWidgets.QTableWidgetItem(info["Port"]))
            self.tableWidget.setItem(row,2, QtWidgets.QTableWidgetItem(info["API"]))
            row = row+1
            self.show()
class InputWindow(QMainWindow):       
    def __init__(self):
        super(InputWindow,self).__init__()
        loadUi("input.ui",self)
        # self.Ip_lineEdit= QLineEdit()
        # self.Port_lineEdit= QLineEdit()
        # self.Api_lineEdit= QLineEdit()
        self.serverwindow=ServerWindow()
        self.saveButton.clicked.connect(self.serverwindow.load_info)
    def passinfo(self):
        widget.setFixedSize(400,450)
        widget.setCurrentIndex(widget.currentIndex()-1)
        self.serverwindow.ip_input.setText(self.Ip_lineEdit.text())
        self.serverwindow.port_input.setText(self.Port_lineEdit.text())
        self.serverwindow.api_input.setText(self.Api_lineEdit.text())
        self.serverwindow.load_info()
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