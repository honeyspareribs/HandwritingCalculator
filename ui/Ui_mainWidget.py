# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\毕业设计\project1.0\ui\mainWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
from PyQt5 import QtCore, QtGui, QtWidgets
from control.paintWidget import paintWidget

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.paintWidget = paintWidget(Form)
        self.paintWidget.setObjectName("paintwidget")
        self.paintWidget.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.verticalLayout.addWidget(self.paintWidget)
        
        self.toolbar = QtWidgets.QWidget(Form)
        self.toolbar.setObjectName("toolbar")
        
        self.gridLayout = QtWidgets.QGridLayout(self.toolbar)
        self.gridLayout.setObjectName("gridLayout")
        
        self.recognizeButton = QtWidgets.QPushButton(self.toolbar)
        self.recognizeButton.setObjectName("recogizeButton")
        self.recognizeButton.setMinimumSize(QtCore.QSize(200, 50))
        self.gridLayout.addWidget(self.recognizeButton, 3, 1, 1, 1)
        self.calculateButton = QtWidgets.QPushButton(self.toolbar)
        self.calculateButton.setObjectName("calculateButton")
        self.calculateButton.setMinimumSize(QtCore.QSize(200, 50))
        self.gridLayout.addWidget(self.calculateButton, 4, 1, 1, 1)
        self.clearButton = QtWidgets.QPushButton(self.toolbar)
        self.clearButton.setMinimumSize(QtCore.QSize(200, 50))
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 5, 1, 1, 1)
        
        self.textEdit = QtWidgets.QTextEdit(self.toolbar)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.textEdit.setFont(QtGui.QFont("Times New Roman", 42))
        self.gridLayout.addWidget(self.textEdit, 3, 0, 3, 1)
        self.verticalLayout.addWidget(self.toolbar)
        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 1)

        self.recognizeButton.clicked.connect(self.recognize)
        self.calculateButton.clicked.connect(self.calculate)
        self.clearButton.clicked.connect(self.clear_all)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.recognizeButton.setFont(QtGui.QFont("宋体", 30))
        self.calculateButton.setFont(QtGui.QFont("宋体", 30))
        self.clearButton.setFont(QtGui.QFont("宋体", 30))
        self.recognizeButton.setText(_translate("Form", "识  别"))
        self.calculateButton.setText(_translate("Form", "计  算"))
        self.clearButton.setText(_translate("Form", "清  除"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.showMaximized()
    sys.exit(app.exec_())


