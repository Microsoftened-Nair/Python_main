from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel, QComboBox, QProgressBar, QMainWindow, QApplication
from PyQt5 import uic
import sys

class UI:
    def __int__(self):
        super(UI, self).__init__()
        uic.loadUi('YT_downloaderUi.ui', self)
        self.show()


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()





