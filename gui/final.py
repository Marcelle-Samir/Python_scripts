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

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(814, 439)
        self.pin0_groupbox = QGroupBox(Form)
        self.pin0_groupbox.setObjectName(u"pin0_groupbox")
        self.pin0_groupbox.setGeometry(QRect(30, 10, 441, 211))
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
        self.pur_radioButton.setGeometry(QRect(10, 20, 83, 18))
        self.highimpedance_radioButton = QRadioButton(self.ipconfiguration_groupBox)
        self.highimpedance_radioButton.setObjectName(u"highimpedance_radioButton")
        self.highimpedance_radioButton.setGeometry(QRect(10, 50, 111, 18))
        self.highimpedance_radioButton.setChecked(True)
        self.pinname_lineedit = QLineEdit(self.pin0_groupbox)
        self.pinname_lineedit.setObjectName(u"pinname_lineedit")
        self.pinname_lineedit.setEnabled(False)
        self.pinname_lineedit.setGeometry(QRect(10, 140, 113, 20))
        self.defaultname_checkBox = QCheckBox(self.pin0_groupbox)
        self.defaultname_checkBox.setObjectName(u"defaultname_checkBox")
        self.defaultname_checkBox.setGeometry(QRect(10, 170, 121, 18))
        self.defaultname_checkBox.setChecked(True)
        self.PORT_comboBox = QComboBox(self.pin0_groupbox)
        self.PORT_comboBox.setObjectName(u"PORT_comboBox")
        self.PORT_comboBox.setGeometry(QRect(310, 50, 62, 22))
        self.PIN_comboBox = QComboBox(self.pin0_groupbox)
        self.PIN_comboBox.setObjectName(u"PIN_comboBox")
        self.PIN_comboBox.setGeometry(QRect(310, 120, 62, 22))
        self.lineEdit = QLineEdit(self.pin0_groupbox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(310, 20, 111, 20))
        self.lineEdit_2 = QLineEdit(self.pin0_groupbox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(310, 80, 111, 20))
        self.path_lineEdit = QLineEdit(Form)
        self.path_lineEdit.setObjectName(u"path_lineEdit")
        self.path_lineEdit.setGeometry(QRect(500, 60, 281, 20))
        self.generate_pushButton = QPushButton(Form)
        self.generate_pushButton.setObjectName(u"generate_pushButton")
        self.generate_pushButton.setGeometry(QRect(520, 90, 241, 121))

        self.retranslateUi(Form)
        self.output_radioButton.clicked.connect(self.opconfiguration_groupBox.setEnabled)
        self.output_radioButton.clicked.connect(self.ipconfiguration_groupBox.setDisabled)
        self.input_radioButton.clicked.connect(self.opconfiguration_groupBox.setDisabled)
        self.input_radioButton.clicked.connect(self.ipconfiguration_groupBox.setEnabled)
        self.defaultname_checkBox.clicked.connect(self.pinname_lineedit.setDisabled)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Simple Tool", None))
        self.pin0_groupbox.setTitle(QCoreApplication.translate("Form", u"Pin Configuration", None))
        self.outputinput_groupBox.setTitle(QCoreApplication.translate("Form", u"Mode", None))
        self.output_radioButton.setText(QCoreApplication.translate("Form", u"Output", None))
        self.input_radioButton.setText(QCoreApplication.translate("Form", u"Input", None))
        self.opconfiguration_groupBox.setTitle(QCoreApplication.translate("Form", u"Output Configuration", None))
        self.high_radiobutton.setText(QCoreApplication.translate("Form", u"High", None))
        self.low_radioButton.setText(QCoreApplication.translate("Form", u"Low", None))
        self.ipconfiguration_groupBox.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.pur_radioButton.setText(QCoreApplication.translate("Form", u"PUR", None))
        self.highimpedance_radioButton.setText(QCoreApplication.translate("Form", u"High Impedance", None))
        self.pinname_lineedit.setText(QCoreApplication.translate("Form", u"Enter Pin Name", None))
        self.defaultname_checkBox.setText(QCoreApplication.translate("Form", u"Use Default Name", None))
        self.PORT_comboBox.setItemText(0, QCoreApplication.translate("Form", u"PORTA", None))
        self.PORT_comboBox.setItemText(1, QCoreApplication.translate("Form", u"PORTB", None))
        self.PORT_comboBox.setItemText(2, QCoreApplication.translate("Form", u"PORTC", None))
        self.PORT_comboBox.setItemText(3, QCoreApplication.translate("Form", u"PORTD", None))

        self.lineEdit.setText(QCoreApplication.translate("Form", u"Choose Port Number", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"Choose Pin Number", None))
        self.path_lineEdit.setText(QCoreApplication.translate("Form", u"Enter Output Path", None))
        self.generate_pushButton.setText(QCoreApplication.translate("Form", u"Generate", None))
    # retranslateUi

