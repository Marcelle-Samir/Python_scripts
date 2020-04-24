# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Print.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.Print_pushbutton = QPushButton(Form)
        self.Print_pushbutton.setObjectName(u"Print_pushbutton")
        self.Print_pushbutton.setGeometry(QRect(50, 200, 301, 81))
        self.Text_lineedit = QLineEdit(Form)
        self.Text_lineedit.setObjectName(u"Text_lineedit")
        self.Text_lineedit.setGeometry(QRect(50, 30, 301, 151))

        self.retranslateUi(Form)
        self.Print_pushbutton.clicked.connect(self.MyFunction)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    def MyFunction(self):
      print(self.Text_lineedit.text())
      self.Text_lineedit.clear()
    # MyFunction
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Simple Tool", None))
        self.Print_pushbutton.setText(QCoreApplication.translate("Form", u"Print", None))
        self.Text_lineedit.setText(QCoreApplication.translate("Form", u"           MOHSEN MESH BYSALLLLLLEM BONUSSS !!!!!", None))
    # retranslateUi
    
    
    
    
app = QApplication(sys.argv)
Widget = QWidget()
Form = Ui_Form()
Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())



