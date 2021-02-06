# public imports
from PyQt5.QtWidgets import (
    QLabel,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QGridLayout
)
from PyQt5 import QtCore
from datetime import datetime

# project imports
from MainWindow import Ui_MainWindow

class Window_Main(QMainWindow, Ui_MainWindow):
    to_do_handler = None

    def keyPressEvent(self, event):
        print(event.key())

    def __init__(self, to_do_handler, *args, **kwargs):
        super(Window_Main, self).__init__(*args, **kwargs)
        self.setupUi(self)
        print("Window_Main: __init__")

        self.to_do_handler = to_do_handler
        self.now = datetime.now()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.create_items()
        self.show()

    def create_items(self):
        for i, item in enumerate(self.to_do_handler.get_to_do_items()):
            wrapper = QWidget()
            wrapper.setFixedHeight(40)
            wrapper_layout = QGridLayout()

            wrapper_layout.setContentsMargins(0, 0, 0, 0)
            wrapper_layout.setSpacing(5)

            # id label
            l_id_style = ".QLabel { background-color: #282828; border-radius: 5; }"
            l_id = QLabel(f'{i+1}')

            if i == 0:
                l_id_style += ".QLabel { border-top-left-radius: 15 }"

            if i == len(self.to_do_handler.get_to_do_items())-1:
                l_id_style += ".QLabel { border-bottom-left-radius: 15 }"

            l_id.setStyleSheet(l_id_style)
            l_id.setFixedHeight(40)
            l_id.setFixedWidth(40)
            l_id.setMinimumWidth(40)
            l_id.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)

            l_date = QLabel(str(self.now - item["date"]))
            l_date.setFixedHeight(40)

            # title label
            l_title_style = ".QWidget { background-color: #282828; border-radius: 5; }"
            if i == 0:
                l_title_style += ".QWidget { border-top-right-radius: 15 }"

            if i == len(self.to_do_handler.get_to_do_items())-1:
                l_title_style += ".QWidget { border-bottom-right-radius: 15 }"

            l_title = QLabel(item["title"])

            text_wrapper = QWidget()
            text_wrapper.setStyleSheet(l_title_style)
            text_wrapper_layout = QHBoxLayout()
            text_wrapper_layout.setContentsMargins(5, 0, 5, 0)
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

        self.setFixedHeight(min(410, 50 + (len(self.to_do_handler.get_to_do_items()) - 1) * 45))
        print(min(505, 10 + len(self.to_do_handler.get_to_do_items()) * 45))
