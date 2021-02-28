# This Python file uses the following encoding: utf-8
import sys
import resources

from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QMenu,
    QSystemTrayIcon
)

from PyQt5 import QtGui

from Window_AddNew import Window_AddNew
from Window_Main import Window_Main

from ToDoItemHandler import ToDoItemHandler
from KeyboardListener import KeyboardListener


class App:
    keyboard_listener = None
    to_do_handler = None
    window_main = None
    window_add_new = None

    def __init__(self):
        self.keyboard_listener = KeyboardListener()
        self.to_do_handler = ToDoItemHandler()
        self.add_signals()

    def add_signals(self):
        self.keyboard_listener.add.connect(self.toggle_add_new_window)
        self.keyboard_listener.main.connect(self.toggle_main_window)
        self.keyboard_listener.escape.connect(self.hide_all_windows)

    def hide_main_window(self):
        self.window_main.clean_up()
        self.window_main.close()

    def hide_add_new_window(self):
        self.window_add_new.close()

    def toggle_add_new_window(self):
        self.hide_all_windows()
        if not self.window_add_new:
            self.window_add_new = Window_AddNew(self.to_do_handler)
        else:
            if not self.window_add_new.isVisible():
                self.window_add_new = Window_AddNew(self.to_do_handler)
            else:
                self.hide_add_new_window()

    def toggle_main_window(self):
        self.hide_all_windows()
        if not self.window_main:
            self.window_main = Window_Main(self.to_do_handler)
        else:
            if not self.window_main.isVisible():
                self.window_main = Window_Main(self.to_do_handler)
            else:
                self.hide_main_window()

    def hide_all_windows(self):
        if self.window_main:
            self.hide_main_window()

        if self.window_add_new:
            self.hide_add_new_window()


if __name__ == "__main__":
    print("test")
    application = QApplication(sys.argv)
    print("one")
    application.setQuitOnLastWindowClosed(False)

    application.setStyle('Fusion')


    status_bar_icon = QtGui.QIcon(":/icons/assets/icon_status_bar.png")
    tray = QSystemTrayIcon()
    tray.setIcon(status_bar_icon)
    tray.setVisible(True)

    print("half")
    menu = QMenu()
    action = QAction("A menu item")
    menu.addAction(action)

    tray.setContextMenu(menu)

    main = App()
    application.exec_()

