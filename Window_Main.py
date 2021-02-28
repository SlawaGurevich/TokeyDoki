# public imports
from PyQt5.QtWidgets import (
    QLabel,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QGridLayout
)
from PyQt5 import QtCore, QtGui
from datetime import datetime
import timeago

# project imports
from MainWindow import Ui_MainWindow

class Window_Main(QMainWindow, Ui_MainWindow):
    to_do_handler = None

    def __init__(self, to_do_handler, *args, **kwargs):
        super(Window_Main, self).__init__(*args, **kwargs)
        self.setupUi(self)
        print("Window_Main: __init__")

        self.to_do_handler = to_do_handler
        self.to_do_items = self.to_do_handler.get_to_do_items()
        self.now = datetime.now()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.create_items()
        self.show()

    def keyPressEvent(self, event):
        if 49 <= event.key() <= 57:
            pressed_number = event.key() - 48

            if pressed_number <= len(self.to_do_items):
                index = pressed_number - 1
                item = self.to_do_items[index]
                print(item)
                item["completed"] = not item["completed"]
                print(item)
                self.check_complete_and_style()

    def check_complete_and_style(self):
        for i, item in enumerate(self.to_do_items):
            layout_item = self.verticalLayout.itemAt(i).widget()
            title = layout_item.findChild(QLabel, "l_title")
            number = layout_item.findChild(QLabel, "l_id")
            font = title.font()
            
            if item["completed"]:
                font.setStrikeOut(True)
                title.setStyleSheet(".QLabel { color: #484848 }")
                number.setStyleSheet(number.styleSheet() + ".QLabel { color: #484848 }")
            else:
                font.setStrikeOut(False)
                title.setStyleSheet(".QLabel { color: #AAAAAA }")
                number.setStyleSheet(number.styleSheet() + ".QLabel { color: #AAAAAA }")
            title.setFont(font)
            number.setFont(font)

    def clean_up(self):
        print("clean up")
        for item in self.to_do_items:
            if item["completed"] is True:
                self.to_do_handler.remove_item(item)

    def create_items(self):
        for i, item in enumerate(self.to_do_items):
            wrapper = QWidget()
            wrapper.setFixedHeight(40)
            wrapper_layout = QGridLayout()
            wrapper_layout.setObjectName("wrapper_layout")

            wrapper_layout.setContentsMargins(0, 0, 0, 0)
            wrapper_layout.setSpacing(5)

            # id label
            l_id_style = ".QLabel { background-color: #282828; border-radius: 5; font-size: 18px; color: #b5b5b5; }"
            l_id = QLabel(f'{i+1}')
            l_id.setObjectName("l_id")

            if i == 0:
                l_id_style += ".QLabel { border-top-left-radius: 15 }"

            if i == len(self.to_do_handler.get_to_do_items())-1:
                l_id_style += ".QLabel { border-bottom-left-radius: 15 }"

            l_id.setStyleSheet(l_id_style)
            l_id.setFixedHeight(40)
            l_id.setFixedWidth(40)
            l_id.setMinimumWidth(40)
            l_id.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)

            l_date = QLabel(timeago.format(item["date"], self.now))
            l_date.setObjectName("l_date")
            l_date.setFixedHeight(40)
            l_date.setStyleSheet(".QLabel { color: #4B4B4B; }")

            # title label
            l_text_wrapper_style = ".QWidget { background-color: #282828; border-radius: 5; }"
            if i == 0:
                l_text_wrapper_style += ".QWidget { border-top-right-radius: 15 }"

            if i == len(self.to_do_items)-1:
                l_text_wrapper_style += ".QWidget { border-bottom-right-radius: 15 }"

            l_title = QLabel(item["title"])
            l_title.setObjectName("l_title")
            l_title.setFont(QtGui.QFont(".AppleSystemUIFont", 16))
            l_title.setStyleSheet(".QLabel { color: #b5b5b5; }")

            text_wrapper = QWidget()
            text_wrapper.setStyleSheet(l_text_wrapper_style)
            text_wrapper_layout = QHBoxLayout()
            text_wrapper_layout.setContentsMargins(10, 0, 10, 0)
            text_wrapper_layout.setSpacing(0)
            text_wrapper_layout.addWidget(l_title, 1)
            text_wrapper_layout.addWidget(l_date)
            text_wrapper.setLayout(text_wrapper_layout)

            # wrapper
            wrapper_layout.addWidget(l_id, 0, 0)
            wrapper_layout.addWidget(text_wrapper, 0, 1)
            wrapper.setLayout(wrapper_layout)

            layout = QHBoxLayout()
            layout.addWidget(wrapper, 1)
            self.verticalLayout.addWidget(wrapper)

        self.setFixedHeight(min(410, 50 + (len(self.to_do_items) - 1) * 45))
        print(min(505, 10 + len(self.to_do_items) * 45))
