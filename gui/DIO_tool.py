# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Print.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, SIGNAL)
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
        self.pin0_groupbox = QGroupBox(Form)
        self.pin0_groupbox.setObjectName(u"pin0_groupbox")
        self.pin0_groupbox.setGeometry(QRect(30, 10, 341, 211))
        self.outputinput_groupBox = QGroupBox(self.pin0_groupbox)
        self.outputinput_groupBox.setObjectName(u"outputinput_groupBox")
        self.outputinput_groupBox.setGeometry(QRect(10, 20, 120, 80))
        self.output_radioButton = QRadioButton(self.outputinput_groupBox)
        self.output_radioButton.setObjectName(u"output_radioButton")
        self.output_radioButton.setGeometry(QRect(20, 20, 83, 18))
        self.input_radioButton = QRadioButton(self.outputinput_groupBox)
        self.input_radioButton.setObjectName(u"input_radioButton")
        self.input_radioButton.setGeometry(QRect(20, 50, 83, 18))
        self.input_radioButton.setChecked(True)
        self.opconfiguration_groupBox = QGroupBox(self.pin0_groupbox)
        self.opconfiguration_groupBox.setObjectName(u"opconfiguration_groupBox")
        self.opconfiguration_groupBox.setEnabled(False)
        self.opconfiguration_groupBox.setGeometry(QRect(180, 20, 120, 80))
        self.high_radiobutton = QRadioButton(self.opconfiguration_groupBox)
        self.high_radiobutton.setObjectName(u"high_radiobutton")
        self.high_radiobutton.setGeometry(QRect(20, 20, 83, 18))
        self.low_radioButton = QRadioButton(self.opconfiguration_groupBox)
        self.low_radioButton.setObjectName(u"low_radioButton")
        self.low_radioButton.setGeometry(QRect(20, 50, 83, 18))
        self.low_radioButton.setChecked(True)
        self.ipconfiguration_groupBox = QGroupBox(self.pin0_groupbox)
        self.ipconfiguration_groupBox.setObjectName(u"ipconfiguration_groupBox")
        self.ipconfiguration_groupBox.setGeometry(QRect(180, 120, 120, 80))
        self.pur_radioButton = QRadioButton(self.ipconfiguration_groupBox)
        self.pur_radioButton.setObjectName(u"pur_radioButton")
        self.pur_radioButton.setGeometry(QRect(20, 20, 83, 18))
        self.highimpedance_radioButton = QRadioButton(self.ipconfiguration_groupBox)
        self.highimpedance_radioButton.setObjectName(u"highimpedance_radioButton")
        self.highimpedance_radioButton.setGeometry(QRect(20, 50, 83, 18))
        self.highimpedance_radioButton.setChecked(True)
        self.pinname_lineedit = QLineEdit(self.pin0_groupbox)
        self.pinname_lineedit.setObjectName(u"pinname_lineedit")
        self.pinname_lineedit.setEnabled(False)
        self.pinname_lineedit.setGeometry(QRect(10, 140, 113, 20))
        self.defaultname_checkBox = QCheckBox(self.pin0_groupbox)
        self.defaultname_checkBox.setObjectName(u"defaultname_checkBox")
        self.defaultname_checkBox.setGeometry(QRect(10, 170, 121, 18))
        self.defaultname_checkBox.setChecked(True)
        self.path_lineEdit = QLineEdit(Form)
        self.path_lineEdit.setObjectName(u"path_lineEdit")
        self.path_lineEdit.setGeometry(QRect(30, 240, 351, 20))
        self.generate_pushButton = QPushButton(Form)
        self.generate_pushButton.setObjectName(u"generate_pushButton")
        self.generate_pushButton.setGeometry(QRect(30, 270, 351, 21))

        self.retranslateUi(Form)
        QObject.connect(self.output_radioButton,SIGNAL("clicked(bool)"),self.opconfiguration_groupBox.setEnabled)
        QObject.connect(self.output_radioButton,SIGNAL("clicked(bool)"),self.ipconfiguration_groupBox.setDisabled)
        QObject.connect(self.input_radioButton,SIGNAL("clicked(bool)"),self.opconfiguration_groupBox.setDisabled)
        QObject.connect(self.input_radioButton,SIGNAL("clicked(bool)"),self.ipconfiguration_groupBox.setEnabled)
        QObject.connect(self.defaultname_checkBox,SIGNAL("clicked(bool)"),self.pinname_lineedit.setDisabled)
        
        self.generate_pushButton.clicked.connect(self.GenerateFunction)
        
        QMetaObject.connectSlotsByName(Form)
    # setupUi
    
    def GenerateFunction(self):
        MFIC_Handler=open(self.path_lineEdit.text()+ r'\MFIC.h','w')
        DIO_Handler=open(self.path_lineEdit.text()+ r'\DIO_config.h','w')
        
        if self.output_radioButton.isChecked():
          if self.high_radiobutton.isChecked():
            DIO_Handler.write('#define DIO_u8PIN0_MODE  DIO_u8OUTPUT_HIGH')
          else:
            DIO_Handler.write('#define DIO_u8PIN0_MODE  DIO_u8OUTPUT_LOW')
        else:
          if self.pur_radioButton.isChecked():
            DIO_Handler.write('#define DIO_u8PIN0_MODE  DIO_u8INPUT_PULLUP')
          else:
            DIO_Handler.write('#define DIO_u8PIN0_MODE  DIO_u8INPUT_HIGH_IMPEDANCE')
        
        if self.defaultname_checkBox.isChecked():
          MFIC_Handler.write('#define DIO_u8PIN0  0')
        else:
          MFIC_Handler.write('#define  ' + self.pinname_lineedit.text() +  '  0')
            
        MFIC_Handler.close()
        DIO_Handler.close()
    # GenerateFunction
    
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Simple Tool", None))
        self.pin0_groupbox.setTitle(QCoreApplication.translate("Form", u"pin 0 configuration", None))
        self.outputinput_groupBox.setTitle(QCoreApplication.translate("Form", u"mode", None))
        self.output_radioButton.setText(QCoreApplication.translate("Form", u"output", None))
        self.input_radioButton.setText(QCoreApplication.translate("Form", u"input", None))
        self.opconfiguration_groupBox.setTitle(QCoreApplication.translate("Form", u"output configuration", None))
        self.high_radiobutton.setText(QCoreApplication.translate("Form", u"high", None))
        self.low_radioButton.setText(QCoreApplication.translate("Form", u"low", None))
        self.ipconfiguration_groupBox.setTitle(QCoreApplication.translate("Form", u"input configuration", None))
        self.pur_radioButton.setText(QCoreApplication.translate("Form", u"pur", None))
        self.highimpedance_radioButton.setText(QCoreApplication.translate("Form", u"high impedance", None))
        self.pinname_lineedit.setText(QCoreApplication.translate("Form", u"enter pin name", None))
        self.defaultname_checkBox.setText(QCoreApplication.translate("Form", u"use default name", None))
        self.path_lineEdit.setText(QCoreApplication.translate("Form", u"enter output path", None))
        self.generate_pushButton.setText(QCoreApplication.translate("Form", u"generate", None))
    # retranslateUi


app = QApplication(sys.argv)
Widget = QWidget()
Form = Ui_Form()
Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())

