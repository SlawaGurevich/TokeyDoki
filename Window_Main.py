# public imports
from PyQt5.QtWidgets import (
    QMainWindow,
)
from PyQt5 import QtCore


# project imports
from MainWindow import Ui_MainWindow

class Window_Main(QMainWindow, Ui_MainWindow):
    to_do_handler = None

    def __init__(self, to_do_handler, *args, **kwargs):
        super(Window_Main, self).__init__(*args, **kwargs)
        self.setupUi(self)
        print("Window_Main: __init__")

        self.to_do_handler = to_do_handler

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.create_items()
        self.show()

    def create_items(self):
        self.removeMe_2.setParent(None)
        self.removeMe_4.setParent(None)
        self.removeMe_3.setParent(None)
        for todo in self.to_do_handler.get_to_do_items():
            print(todo)
