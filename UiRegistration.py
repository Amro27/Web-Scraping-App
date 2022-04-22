# uncompyle6 version 3.8.1.dev0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: UiRegistration.py
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frm_Registration(object):

    def setupUi(self, frm_Registration):
        frm_Registration.setObjectName('frm_Registration')
        frm_Registration.setWindowModality(QtCore.Qt.ApplicationModal)
        frm_Registration.resize(371, 134)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('res/11.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frm_Registration.setWindowIcon(icon)
        self.txt_OTP = QtWidgets.QLineEdit(frm_Registration)
        self.txt_OTP.setGeometry(QtCore.QRect(114, 30, 230, 23))
        self.txt_OTP.setObjectName('txt_OTP')
        self.label = QtWidgets.QLabel(frm_Registration)
        self.label.setGeometry(QtCore.QRect(27, 25, 71, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName('label')
        self.btn_Registration = QtWidgets.QPushButton(frm_Registration)
        self.btn_Registration.setEnabled(False)
        self.btn_Registration.setGeometry(QtCore.QRect(252, 74, 93, 33))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap('753318.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Registration.setIcon(icon1)
        self.btn_Registration.setAutoExclusive(False)
        self.btn_Registration.setAutoDefault(False)
        self.btn_Registration.setDefault(True)
        self.btn_Registration.setObjectName('btn_Registration')
        self.btn_SendOTP = QtWidgets.QPushButton(frm_Registration)
        self.btn_SendOTP.setEnabled(True)
        self.btn_SendOTP.setGeometry(QtCore.QRect(114, 74, 93, 33))
        self.btn_SendOTP.setIcon(icon1)
        self.btn_SendOTP.setAutoExclusive(False)
        self.btn_SendOTP.setAutoDefault(False)
        self.btn_SendOTP.setDefault(True)
        self.btn_SendOTP.setObjectName('btn_SendOTP')
        self.retranslateUi(frm_Registration)
        QtCore.QMetaObject.connectSlotsByName(frm_Registration)

    def retranslateUi(self, frm_Registration):
        _translate = QtCore.QCoreApplication.translate
        frm_Registration.setWindowTitle(_translate('frm_Registration', 'Web Scraping Registration'))
        self.txt_OTP.setPlaceholderText(_translate('frm_Registration', 'OTP Code'))
        self.label.setText(_translate('frm_Registration', 'OTP Code:'))
        self.btn_Registration.setText(_translate('frm_Registration', 'Registration'))
        self.btn_SendOTP.setText(_translate('frm_Registration', 'Send OTP'))