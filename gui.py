from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel , QPlainTextEdit
from PyQt5.QtGui import QIcon , QColor
from PyQt5.QtCore import pyqtSlot , QSize,Qt , QRect

import Twitter_crawling_code
import sys
 
class App(QMainWindow):
 
    def __init__(self):
        super(App,self).__init__()
        self.title = 'Sentiment Analysis of Hindi Tweets'
        self.left = 10
        self.top = 10
        self.width = 350
        self.height = 400

        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        #create textbox for displaying
        self.DisplayTextbox = QPlainTextEdit(self)
        self.DisplayTextbox.setLineWrapMode(200)
        self.DisplayTextbox.move(20, 20)
        self.DisplayTextbox.resize(280,200)
       

        # Create textbox fro entering
        self.EnterTextbox = QLabel(self)
        self.EnterTextbox = QLineEdit(self)
        self.EnterTextbox.move(20, 300)
        self.EnterTextbox.resize(280,40)

 
        # connect enter textbox to function on_click
        self.EnterTextbox.returnPressed.connect(self.on_click)

        self.show()
 
    @pyqtSlot()

    def on_click(self):
        
        textfromgui = self.EnterTextbox.text()

        pos,neg=Twitter_crawling_code.main(textfromgui)
        self.DisplayTextbox.setPlainText("POSISTIVE = "+str(pos)+"%\nNEGATIVE = "+str(neg)+"%")
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())