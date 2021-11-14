from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QProgressBar, QComboBox
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __int__(self):
        super(UI, self).__int__()

        uic.loadUi('YT_downloaderUi.ui', self)

        self.show()

app = QApplication(sys.argv)
UiWindow = UI()
app.exec_()
