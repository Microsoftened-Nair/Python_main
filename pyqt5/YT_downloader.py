from PyQt5 import QtCore, QtGui, QtWidgets
import YT_downloader_module

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(634, 630)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../OneDrive/Pictures/Icons/YouTube_downloader.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(44, 48, 56);\n"
"background-color: qlineargradient(spread:pad, x1:0.0696965, y1:0.915, x2:1, y2:0, stop:0 rgba(0, 93, 255, 255), stop:0.880597 rgba(26, 255, 255, 255));\n"
"")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Heading = QtWidgets.QLabel(self.centralwidget)
        self.Heading.setGeometry(QtCore.QRect(10, 10, 491, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Heading.setFont(font)
        self.Heading.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: qlineargradient(spread:pad, x1:0.965, y1:0.591, x2:0.035, y2:0.6075, stop:0 rgba(0, 93, 255, 255), stop:0.880597 rgba(26, 255, 255, 255));\n"
"\n"
"")
        self.Heading.setObjectName("Heading")
        self.Link_label = QtWidgets.QLabel(self.centralwidget)
        self.Link_label.setGeometry(QtCore.QRect(20, 110, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        self.Link_label.setFont(font)
        self.Link_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(34, 37, 255);")
        self.Link_label.setObjectName("Link_label")
        self.Dir_label = QtWidgets.QLabel(self.centralwidget)
        self.Dir_label.setGeometry(QtCore.QRect(20, 220, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(22)
        self.Dir_label.setFont(font)
        self.Dir_label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(34, 37, 255);")
        self.Dir_label.setObjectName("Dir_label")
        self.L_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.L_entry.setGeometry(QtCore.QRect(20, 160, 421, 41))
        self.L_entry.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.154542, y1:0.193, x2:1, y2:1, stop:0 rgba(10, 62, 255, 255), stop:1 rgba(255, 255, 255, 0));")
        self.L_entry.setFrame(False)
        self.L_entry.setObjectName("L_entry")
        self.Dir_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.Dir_entry.setGeometry(QtCore.QRect(20, 280, 421, 41))
        self.Dir_entry.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.154542, y1:0.193, x2:1, y2:1, stop:0 rgba(10, 62, 255, 255), stop:1 rgba(255, 255, 255, 0));")
        self.Dir_entry.setFrame(False)
        self.Dir_entry.setObjectName("Dir_entry")
        self.Vid_title = QtWidgets.QLabel(self.centralwidget)
        self.Vid_title.setGeometry(QtCore.QRect(20, 380, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.Vid_title.setFont(font)
        self.Vid_title.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(34, 37, 255);")
        self.Vid_title.setObjectName("Vid_title")
        self.Vid_Length = QtWidgets.QLabel(self.centralwidget)
        self.Vid_Length.setGeometry(QtCore.QRect(20, 340, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.Vid_Length.setFont(font)
        self.Vid_Length.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(34, 37, 255);")
        self.Vid_Length.setObjectName("Vid_Length")
        self.L_size = QtWidgets.QLabel(self.centralwidget)
        self.L_size.setGeometry(QtCore.QRect(20, 420, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.L_size.setFont(font)
        self.L_size.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(34, 37, 255);")
        self.L_size.setObjectName("L_size")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 570, 621, 23))
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("color: rgb(34, 37, 255);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.Download_button = QtWidgets.QPushButton(self.centralwidget)
        self.Download_button.setGeometry(QtCore.QRect(250, 470, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.Download_button.setFont(font)
        self.Download_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Download_button.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.154542, y1:0.193, x2:1, y2:1, stop:0 rgba(10, 62, 255, 255), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(0, 255, 247);")
        icon = QtGui.QIcon.fromTheme("1")
        self.Download_button.setIcon(icon)
        self.Download_button.setIconSize(QtCore.QSize(20, 30))
        self.Download_button.setAutoDefault(False)
        self.Download_button.setDefault(False)
        self.Download_button.setFlat(False)
        self.Download_button.setObjectName("Download_button")
        self.Dir_go = QtWidgets.QPushButton(self.centralwidget)
        self.Dir_go.setGeometry(QtCore.QRect(440, 280, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.Dir_go.setFont(font)
        self.Dir_go.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.154542, y1:0.193, x2:1, y2:1, stop:0 rgba(10, 62, 255, 255), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(0, 255, 247);")
        self.Dir_go.setFlat(False)
        self.Dir_go.setObjectName("Dir_go")
        self.link_go = QtWidgets.QPushButton(self.centralwidget)
        self.link_go.setEnabled(True)
        self.link_go.setGeometry(QtCore.QRect(440, 160, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.link_go.setFont(font)
        self.link_go.setAcceptDrops(False)
        self.link_go.setAutoFillBackground(False)
        self.link_go.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.154542, y1:0.193, x2:1, y2:1, stop:0 rgba(10, 62, 255, 255), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(0, 255, 247);")
        self.link_go.setCheckable(False)
        self.link_go.setFlat(False)
        self.link_go.setObjectName("link_go")
        self.Quality_box = QtWidgets.QComboBox(self.centralwidget)
        self.Quality_box.setGeometry(QtCore.QRect(400, 470, 73, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.Quality_box.setFont(font)
        self.Quality_box.setEditable(False)
        self.Quality_box.setFrame(False)
        self.Quality_box.setObjectName("Quality_box")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YT Downloader"))
        self.Heading.setText(_translate("MainWindow", "YouTube Downloader"))
        self.Link_label.setText(_translate("MainWindow", "Enter link:"))
        self.Dir_label.setText(_translate("MainWindow", "Enter Directory:"))
        self.Vid_title.setText(_translate("MainWindow", "Video title: "))
        self.Vid_Length.setText(_translate("MainWindow", "Video Length: "))
        self.L_size.setText(_translate("MainWindow", "Filesize:"))
        self.Download_button.setText(_translate("MainWindow", "Download"))
        self.Dir_go.setText(_translate("MainWindow", "Browse.."))
        self.link_go.setText(_translate("MainWindow", "GO"))
    def go(self):
        pass

    def browse(self):
        pass

    def download(self):
        pass

    def option(self):
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
