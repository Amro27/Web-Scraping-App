# uncompyle6 version 3.8.1.dev0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: frmAddSKU.py
from MyLib import *
from UiAddSKU import Ui_Dialog as Ui_frmAddSKU

class Create(QDialog, Ui_frmAddSKU):

    def __init__(self, parent=None):
        super(Create, self).__init__()
        self.parent = parent
        self.setupUi(self)
        self.setFixedSize(331, 122)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.btn_Cancel = self.findChild(QPushButton, 'btn_cancel')
        self.btn_save = self.findChild(QPushButton, 'btn_save')
        self.btn_Cancel.clicked.connect(self.btn_click)
        self.btn_save.clicked.connect(self.btn_click)
        self.i = self.parent.TWCat.columnCount()
        if self.i == 9:
            self.s = 0
        else:
            self.s = 2
        # self.row = self.parent.tbl_data.currentIndex().row()
        # self.txt_SKU.setText(self.parent.tbl_data.item(self.row, self.s).text())
        self.txt_SKU.setText(self.parent.TWCat.selectedItems()[0].text(0))
        self.txt_SKU.setFocusPolicy(Qt.StrongFocus)
        self.txt_SKU.setFocus()
        self.txt_SKU.selectAll()

    def btn_click(self):
        sender = self.sender()
        if sender.objectName() == 'btn_save':
            # Product_Id = self.parent.tbl_data.item(self.row, self.i - 1).text()
            Product_Id = self.parent.TWCat.selectedItems()[0].text(7)
            SKU = self.txt_SKU.text()
            if SKU is not None:
                # print(Product_Id)
                self.parent.parent.parent.cur.execute("UPDATE data SET SKU='{}' WHERE Link = '{}';".format(SKU, sqlescape(Product_Id)))
                self.parent.parent.parent.con.commit()
                # self.parent.tbl_data.item(self.row, self.s).setText(SKU)
                self.parent.TWCat.selectedItems()[0].setText(0, SKU)
                self.close()
        elif sender.objectName() == 'btn_cancel':
            self.close()