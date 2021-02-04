from AddNewWindow import Ui_AddNewWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import Qt, QtCore
from PyQt5.QtCore import pyqtSignal
from datetime import datetime


class Window_AddNew(QMainWindow, Ui_AddNewWindow):
    closed = pyqtSignal()

    def __init__(self, to_do_item_handler, *args, **kwargs):
        super(Window_AddNew, self).__init__(*args, **kwargs)
        self.setupUi(self)
        print("Window_AddNew: __init__")

        shadow_effect = Qt.QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(5)
        shadow_effect.setOffset(0)

        self.to_do_item_handler = to_do_item_handler

        self.setGraphicsEffect(shadow_effect)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui()
        self.add_interactions()

        self.show()

    def ui(self):
        next_id = len(self.to_do_item_handler.get_to_do_items()) + 1
        self.l_newId.setText(f'{next_id}')

    def add_interactions(self):
        self.i_toDoInput.returnPressed.connect(self.add_item)

    def add_item(self):
        item = {
            "date": datetime.now(),
            "title": self.i_toDoInput.text()
        }

        self.to_do_item_handler.add_item(item)
        self.i_toDoInput.setText("")
        print(self.to_do_item_handler.get_to_do_items())
        self.close()
