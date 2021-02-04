# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddNewWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddNewWindow(object):
    def setupUi(self, AddNewWindow):
        AddNewWindow.setObjectName("AddNewWindow")
        AddNewWindow.resize(800, 54)
        self.centralwidget = QtWidgets.QWidget(AddNewWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setStyleSheet(".QFrame {\n"
"    border-radius: 19;\n"
"    background-color: #3E3E3E;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.l_newId = QtWidgets.QLabel(self.frame)
        self.l_newId.setMinimumSize(QtCore.QSize(40, 40))
        self.l_newId.setMaximumSize(QtCore.QSize(40, 40))
        self.l_newId.setStyleSheet(".QLabel {\n"
"    border-top-left-radius: 15;\n"
"    border-top-right-radius: 5;\n"
"    border-bottom-right-radius: 5;\n"
"    border-bottom-left-radius: 15;\n"
"    background-color: #282828;\n"
"    color: #13B7E7;\n"
"}")
        self.l_newId.setAlignment(QtCore.Qt.AlignCenter)
        self.l_newId.setObjectName("l_newId")
        self.gridLayout.addWidget(self.l_newId, 0, 0, 1, 1)
        self.inputWrapper = QtWidgets.QFrame(self.frame)
        self.inputWrapper.setStyleSheet("#inputWrapper {\n"
"    background-color: #282828;\n"
"    border-top-left-radius: 5;\n"
"    border-top-right-radius: 15;\n"
"    border-bottom-right-radius: 15;\n"
"    border-bottom-left-radius: 5;\n"
"}")
        self.inputWrapper.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inputWrapper.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inputWrapper.setObjectName("inputWrapper")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.inputWrapper)
        self.horizontalLayout.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.i_toDoInput = QtWidgets.QLineEdit(self.inputWrapper)
        self.i_toDoInput.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.i_toDoInput.setFont(font)
        self.i_toDoInput.setStyleSheet(".QLineEdit {\n"
"    color: #13B7E7;\n"
"    line-height: 40;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.i_toDoInput.setObjectName("i_toDoInput")
        self.horizontalLayout.addWidget(self.i_toDoInput)
        self.l_enterIcon = QtWidgets.QLabel(self.inputWrapper)
        self.l_enterIcon.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily(".Apple Color Emoji UI")
        self.l_enterIcon.setFont(font)
        self.l_enterIcon.setAlignment(QtCore.Qt.AlignCenter)
        self.l_enterIcon.setObjectName("l_enterIcon")
        self.horizontalLayout.addWidget(self.l_enterIcon)
        self.gridLayout.addWidget(self.inputWrapper, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        AddNewWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddNewWindow)
        QtCore.QMetaObject.connectSlotsByName(AddNewWindow)

    def retranslateUi(self, AddNewWindow):
        _translate = QtCore.QCoreApplication.translate
        AddNewWindow.setWindowTitle(_translate("AddNewWindow", "MainWindow"))
        self.l_newId.setText(_translate("AddNewWindow", "#"))
        self.l_enterIcon.setText(_translate("AddNewWindow", "⮐"))
