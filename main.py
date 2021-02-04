# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, Qt

from MainWindow import Ui_MainWindow
from AddNewView import AddNewView

from ToDoItemHandler import ToDoItemHandler

class MainWindow(QMainWindow, Ui_MainWindow):
    to_do_items = []

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.to_do_handler = ToDoItemHandler()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.addNewWindow = AddNewView(self.to_do_handler)
        self.addNewWindow.show()

    def create_items(self):
        self.removeMe_2.setParent(None)
        self.exampleId.setParent(None)
        for todo in self.to_do_handler.get_to_do_items():
            print(todo)


if __name__ == "__main__":
    application = QApplication(sys.argv)
    application.setStyle('Fusion')
    window = MainWindow()      # 1. Instantiate ApplicationContext
    window.show()
    sys.exit(application.exec_())

