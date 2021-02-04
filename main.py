# This Python file uses the following encoding: utf-8
import sys
import resources

from PyQt5.QtWidgets import  (
    QAction,
    QApplication,
    QMainWindow,
    QMenu,
    QShortcut,
    QSystemTrayIcon
)

from PyQt5 import QtCore, Qt, QtGui

from MainWindow import Ui_MainWindow
from AddNewView import AddNewView

from ToDoItemHandler import ToDoItemHandler
from KeyboardListener import KeyboardListener

class MainWindow(QMainWindow, Ui_MainWindow):
    to_do_items = []

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.to_do_handler = ToDoItemHandler()
        self.keyboard_listener = KeyboardListener()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.create_items()
        self.add_signals()

    def add_signals(self):
        self.keyboard_listener.add.connect(self.show_add_new_window)
        self.keyboard_listener.main.connect(self.show_main_window)
        self.keyboard_listener.escape.connect(self.hide_all_windows)


    def create_items(self):
        self.removeMe_2.setParent(None)
        self.removeMe_4.setParent(None)
        self.removeMe_3.setParent(None)
        for todo in self.to_do_handler.get_to_do_items():
            print(todo)

    def hide_all_windows(self):
        if self.isVisible():
            self.hide()

        if self.addNewWindow:
            self.addNewWindow.close()
            self.addNewWindow = None

    def show_main_window(self):
        print("Show main window shortcut")
        if self.isVisible():
            self.hide()
        else:
            self.show()

    def show_add_new_window(self):
        print("Shortcut")
        if self.addNewWindow:
            self.addNewWindow = AddNewView(self.to_do_handler)
        else:
            self.addNewWindow.close()
            self.addNewWindow = None

if __name__ == "__main__":

    application = QApplication(sys.argv)
    application.setStyle('Fusion')
    application.setQuitOnLastWindowClosed(False)

    status_bar_icon = QtGui.QIcon(":/icons/assets/icon_status_bar.png")
    tray = QSystemTrayIcon()
    tray.setIcon(status_bar_icon)
    tray.setVisible(True)

    menu = QMenu()
    action = QAction("A menu item")
    menu.addAction(action)

    tray.setContextMenu(menu)

    window = MainWindow()      # 1. Instantiate ApplicationContext
    sys.exit(application.exec_())

