# uncompyle6 version 3.8.1.dev0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: frmResults.py
from MyLib import *
from UiResults import Ui_MainWindow as Ui_frmResults

class Create(QMainWindow, Ui_frmResults):

    def btn_click(self):
        try:
            sender = self.sender()
            if sender.objectName() == 'actionAdd_Prices':
                urllib3.disable_warnings()
                i = self.tbl_data.columnCount()
                if i == 9:
                    s = 0
                else:
                    s = 2
                for row in range(self.tbl_data.rowCount()):
                    bar = self.tbl_data.item(row, s).text()
                    self.lbl2.setText('{} %  Add Price Processing'.format(round(row / self.tbl_data.rowCount() * 100, 2)))
                    QCoreApplication.processEvents()

                    if bar in ['', '0', '_']:
                        self.tbl_data.item(row, s + 1).setText('0')
                        self.tbl_data.item(row, s + 3).setText('0')
                        self.tbl_data.item(row, s + 4).setText('0')

                    # elif len(bar) > 1:
                    #
                    #     req = requests.get(
                    #         ('https://prd-wd.hyperone.com:44300/sap/bc/getsalesprice/Sales/{}/00001'.format(bar)),
                    #         auth=requests.auth.HTTPBasicAuth(username='H1WEBSCRAP', password='H1WS123'),
                    #         verify=False).json()

                    else:
                        Desc = self.Old_Data.query("BARCODE.str.contains('%s')"%(bar)).DESC.to_list()[-1]
                        SELL_PRICE = self.Old_Data.query("BARCODE.str.contains('%s')"%(bar)).SELL_PRICE.to_list()[-1]
                        BSELL_PRICE = self.Old_Data.query("BARCODE.str.contains('%s')"%(bar)).PROM_PRICE.to_list()[-1]

                        self.tbl_data.item(row, s + 1).setText(Desc)
                        self.tbl_data.item(row, s + 3).setText(f'{float(SELL_PRICE):,}')
                        self.tbl_data.item(row, s + 4).setText(f'{float(BSELL_PRICE):,}')


                    # SELL_PRICE = self.Old_Data[self.Old_Data.BARCODE == bar].SELL_PRICE.to_list()[0]
                    # BSELL_PRICE = self.Old_Data[self.Old_Data.BARCODE == bar].PROM_PRICE.to_list()[0]


                    # if bar != '' and bar != '_':
                    #     req = requests.get(('https://prd-wd.hyperone.com:44300/sap/bc/getsalesprice/Sales/{}/00001'.format(bar)), auth=requests.auth.HTTPBasicAuth(username='H1WEBSCRAP', password='H1WS123'), verify=False).json()
                    #     BSELL_PRICE = req['DATATABLE'][0]['BSELL_PRICE']
                    #     SELL_PRICE = req['DATATABLE'][0]['SELL_PRICE']
                    #     BSELL_PRICE = round(float(BSELL_PRICE), 2)
                    #     SELL_PRICE = round(float(SELL_PRICE), 2)
                    #     self.tbl_data.item(row, s + 2).setText(f"{BSELL_PRICE:.2f}")
                    #     self.tbl_data.item(row, s + 3).setText(f"{SELL_PRICE:.2f}")

                self.lbl2.setText('')
                show_pop('Done', 'Prices have been added', QMessageBox.Information)
            if sender.objectName() == 'actionCopy_to_Clipboard':
                self.copySelection()
            if sender.objectName() == 'actionExport_to_Microsoft_Excel':
                excel = win32com.client.Dispatch('Excel.Application')
                wb = excel.Workbooks.Add()
                wbs = wb.Worksheets.Add()
                wbs.Name = 'MyNewSheet'
                selection = self.tbl_data.selectedIndexes()
                if selection:
                    rows = []
                    record = []
                    for idx in self.tbl_data.selectionModel().selectedRows():
                        record = []
                        for col in range(self.tbl_data.columnCount()):
                            record.append(self.tbl_data.item(idx.row(), col).text())

                        rows.append(record)

                else:
                    rows = []
                    for row in range(self.tbl_data.rowCount()):
                        record = []
                        for col in range(self.tbl_data.columnCount()):
                            record.append(self.tbl_data.item(row, col).text())

                        rows.append(record)

                columnHeaders = []
                for j in range(self.tbl_data.model().columnCount()):
                    columnHeaders.append(self.tbl_data.horizontalHeaderItem(j).text())

                wbs.Range(wbs.Cells(2, 1), wbs.Cells(len(rows) + 1, len(columnHeaders))).Value = rows
                wbs.Range(wbs.Cells(1, 1), wbs.Cells(1, len(columnHeaders))).Value = columnHeaders
                wbs.Columns.WrapText = False
                with Obj(wbs.Cells) as (c):
                    c.HorizontalAlignment = -4108
                    c.VerticalAlignment = -4108
                wbs.Columns.AutoFit()
                excel.Visible = True
        except Exception as e:
            print('5')
            show_pop('Error', str(e),
                     QMessageBox.Critical)
            self.parent.close()

    def copySelection(self):
        selection = self.tbl_data.selectedIndexes()
        columns = sorted((index.column() for index in selection))
        if selection:
            s = ''
            x = 1
            for i in range(0, self.tbl_data.columnCount()):
                if self.tbl_data.isColumnHidden(i) == False:
                    s = s + self.tbl_data.horizontalHeaderItem(i).text() + '\t'
                    x += 1

            s = s + '\n'
            for index in selection:
                col = index.column()
                if index.data():
                    data = str(index.data())
                else:
                    data = str('')
                if col == columns[(-1)]:
                    s = s + data + '\n'
                else:
                    s = s + data + '\t'

            self.parent.parent.clipboard().setText(s)

    def doubleClickedItem(self, index):
        pass

    def eventFilter(self, source, event):
        try:
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                if source is self.tbl_data.viewport():
                    if event.buttons() == QtCore.Qt.RightButton:
                        item = self.tbl_data.itemAt(event.pos())
                        import frmAddSKU1
                        self.frm_AddSKU = frmAddSKU1.Create(self)
                        self.frm_AddSKU.show()
                    else:
                        if event.buttons() == QtCore.Qt.LeftButton:
                            item = self.tbl_data.itemAt(event.pos())
                            i = self.tbl_data.columnCount() - 1
                            url = self.tbl_data.item(item.row(), i).text()
                            if len(url) > 0:
                                self.parent.Driver()
                                self.parent.driver.get(url)
            return super(Create, self).eventFilter(source, event)
        except Exception as e:
            print('7')
            show_pop('Error', str(e),
                     QMessageBox.Critical)
            self.parent.close()

    def __init__(self, parent=None):
        try:
            super(Create, self).__init__()
            self.parent = parent
            self.Old_Data = pd.read_sql_query('Select * from hyper_pos', parent.parent.con)
            Mapping = {'SKU': 'BARCODE',
                       'Product Name': 'DESC',
                       'Product Original Price': 'SELL_PRICE',
                       'Product Discount Price': 'PROM_PRICE',
                       'Branch': 'BRANCH'}
            self.Old_Data.rename(columns=Mapping, inplace=True)
            self.Old_Data.BARCODE = self.Old_Data.BARCODE.apply(lambda x: x.replace(' ', ''))
            self.setupUi(self)
            self.tbl_data = self.findChild(QTableWidget, 'tableWidget')
            self.tbl_data.viewport().installEventFilter(self)
            self.tbl_data.doubleClicked.connect(self.doubleClickedItem)
            self.actionCopy_to_Clipboard = self.findChild(QAction, 'actionCopy_to_Clipboard')
            self.actionExport_to_Microsoft_Excel = self.findChild(QAction, 'actionExport_to_Microsoft_Excel')
            self.AddPrice = self.findChild(QAction, 'actionAdd_Prices')
            self.AddPrice.triggered.connect(self.btn_click)
            self.actionCopy_to_Clipboard.triggered.connect(self.btn_click)
            self.actionExport_to_Microsoft_Excel.triggered.connect(self.btn_click)
        except Exception as e:
            print('6')
            show_pop('Error', str(e),
                     QMessageBox.Critical)
            self.parent.close()

    def addTableRow(self, table, row_data):
        row = table.rowCount()
        table.setRowCount(row + 1)
        col = 0
        for item in row_data:
            cell = QTableWidgetItem(str(item))
            cell.setTextAlignment(Qt.AlignHCenter)
            if cell.text() == 'None':
                cell.setText('(null)')
            table.setItem(row, col, cell)
            col += 1