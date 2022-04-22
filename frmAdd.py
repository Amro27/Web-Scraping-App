# uncompyle6 version 3.8.1.dev0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: frmAdd.py
import MySQLdb
from MyLib import *
from UiAdd import Ui_Dialog as Ui_frmAdd

class Create(QDialog, Ui_frmAdd):

    def __init__(self, parent=None):
        super(Create, self).__init__()
        self.parent = parent
        self.setupUi(self)
        self.setFixedSize(382, 143)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.btn_Cancel = self.findChild(QPushButton, 'btn_cancel')
        self.btn_save = self.findChild(QPushButton, 'btn_save')
        self.txt_cat_name = self.findChild(QLineEdit, 'txt_cat_name')
        self.txt_sub_cat_name = self.findChild(QLineEdit, 'txt_sub_cat_name')
        self.txt_url = self.findChild(QLineEdit, 'txt_url')
        self.btn_Cancel.clicked.connect(self.btn_click)
        self.btn_save.clicked.connect(self.btn_click)
        self.txt_cat_name.setFocus()
        self.setTabOrder(self.btn_save, self.btn_Cancel)

    def btn_click(self):
        sender = self.sender()
        if sender.objectName() == 'btn_save':
            txt_cat_name = self.txt_cat_name.text()
            txt_sub_cat_name = self.txt_sub_cat_name.text()
            txt_url = self.txt_url.text()
            if not (txt_cat_name and txt_sub_cat_name and txt_url):
                show_pop('Error', 'Please fill in all the required fields', QMessageBox.Critical)
            else:
                self.parent.parent.cur.execute("INSERT INTO data_urls (`MAC address`, `Category Name`,`Sub Category Name`,URL) VALUES ('{}', '{}','{}','{}');".format(self.parent.parent.MACaddress, sqlescape(txt_cat_name), sqlescape(txt_sub_cat_name), sqlescape(txt_url)))
                self.parent.parent.con.commit()
                self.parent.read_db()
                self.close()
        if sender.objectName() == 'btn_cancel':
            self.close()