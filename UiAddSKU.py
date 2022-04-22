# uncompyle6 version 3.8.1.dev0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: UiAddSKU.py
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName('Dialog')
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(331, 122)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('res/02.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(False)
        Dialog.setModal(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 18, 71, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName('label')
        self.btn_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_cancel.setGeometry(QtCore.QRect(119, 65, 93, 33))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap('753345.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon1)
        self.btn_cancel.setObjectName('btn_cancel')
        self.btn_save = QtWidgets.QPushButton(Dialog)
        self.btn_save.setGeometry(QtCore.QRect(219, 65, 93, 33))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap('753318.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon2)
        self.btn_save.setAutoExclusive(False)
        self.btn_save.setAutoDefault(False)
        self.btn_save.setDefault(True)
        self.btn_save.setObjectName('btn_save')
        self.txt_SKU = QtWidgets.QLineEdit(Dialog)
        self.txt_SKU.setGeometry(QtCore.QRect(81, 22, 230, 23))
        self.txt_SKU.setObjectName('txt_SKU')
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate('Dialog', 'Add SKU'))
        self.label.setText(_translate('Dialog', 'SKU'))
        self.btn_cancel.setText(_translate('Dialog', 'Cancel'))
        self.btn_save.setText(_translate('Dialog', 'Save'))
        self.txt_SKU.setPlaceholderText(_translate('Dialog', 'SKU'))