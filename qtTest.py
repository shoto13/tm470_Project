import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLabel
from selenium import webdriver
from tkinter import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time


# app = QApplication(sys.argv)
# window = QWidget()
# window.setWindowTitle('PyQt App')
# window.setGeometry(100,100,280,80)
# window.move(60,15)
#
# layout = QHBoxLayout()
# layout.addRow('Enterl URL:', QLineEdit())
# layout.addWidget(QPushButton('left'))
# layout.addWidget(QPushButton('center'))
# layout.addWidget(QPushButton('right'))
# window.setLayout(layout)
#
#
# window.show()
# sys.exit(app.exec_())


# LOAD URL FUNCTION
def url_button_clicked():
    url = urlString.get()

    #make sure URL has correct prefix
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + urlString.get()

    msg = f'Your entered URL {url} has been displayed'

    driver.get(url)
    showinfo(
        title='Information',
        message=msg
    )


msg = ""


class Dialog(QDialog):
    """Dialog."""
    def __init__(self, parent=None):

        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('QDialog')
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow('Enter URL:', QLineEdit())
        dlgLayout.addLayout(formLayout)
        btn1 = QPushButton('Get Website')
        btn2 = QPushButton('Flip page')
        btn3 = QPushButton('Recolour text')
        btn4 = QPushButton('Zoom page in')
        btn5 = QPushButton('Zoom page out')
        btn6 = QPushButton('Toggle JavaScript on/off')

        btn1.clicked.connect(self.greeting)  # Connect clicked to greeting()
        btn2.clicked.connect(self.farewell)  # Connect clicked to greeting()

        dlgLayout.addWidget(btn1)
        dlgLayout.addWidget(btn2)

        global msg
        msg = QLabel('')
        dlgLayout.addWidget(msg)

        self.setLayout(dlgLayout)

        def greeting(self):
            """Slot function."""
            if msg.text():
                msg.setText("")
            else:
                msg.setText("Hello World!")

        def farewell(self):
            if msg.text():
                msg.setText("")
            else:
                msg.setText("Goodbye World!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())

options = Options()

PATH = "/home/vxv/chromedriver"

driver = webdriver.Chrome(
    executable_path=PATH,
    options=options
)



