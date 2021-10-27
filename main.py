from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import *
import sys
import mysql.connector
from sistema_de_login import Login_Window
from sistema_de_register import Register_Window

connection = mysql.connector.connect(host='localhost', user='root', password='x132131x', db='db_accounts')
cursor = connection.cursor()

class register_page(QMainWindow):
    def __init__(self, *args, **argvs):
        super(register_page, self).__init__(*args,**argvs)
        self.ui = Register_Window()
        self.ui.setupUi(self)
        self.ui.Bt_register.clicked.connect(self.open_login_window)


    def open_login_window(self):
        if self.ui.register() == False:
            self.window = login_page()
            self.hide()
            self.window.show()
            
            



class login_page(QMainWindow):
    def __init__(self, *args, **argvs):
        super(login_page, self).__init__(*args,**argvs)
        self.ui = Login_Window()
        self.ui.setupUi(self)
        self.ui.Bt_register.clicked.connect(self.open_register_window)
    
    def open_register_window(self):
        self.window = register_page()
        self.hide()
        self.window.show()






app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = login_page()
    window.show()
sys.exit(app.exec_())
