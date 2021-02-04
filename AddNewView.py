from AddNewWindow import Ui_AddNewWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import Qt, QtCore
from datetime import datetime

class AddNewView(QMainWindow, Ui_AddNewWindow):
    def __init__(self, to_do_item_handler, *args, **kwargs):
        super(AddNewView, self).__init__(*args, **kwargs)
        shadow_effect = Qt.QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(5)
        shadow_effect.setOffset(0)

        self.to_do_item_handler = to_do_item_handler

        self.setGraphicsEffect(shadow_effect)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.add_interactions()
        self.show()

    def add_interactions(self):
        self.toDoInput.returnPressed.connect(self.add_item)
        # self.toDoInput.key .connect(self.key_pressed)

    def key_pressed(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Escape:
            self.hide()

    def add_item(self):
        item = {}
        item["date"] = datetime.now()
        item["title"] = self.toDoInput.text()
        self.to_do_item_handler.add_item(item)
        self.toDoInput.setText("")
        print(self.to_do_item_handler.get_to_do_items())
        self.hide()

