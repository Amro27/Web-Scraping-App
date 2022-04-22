# uncompyle6 version 3.8.1.dev0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: frmResults.py
from MyLib import *
# from UiResults import Ui_MainWindow as Ui_frmResults
from UiTreeResults import Ui_MainWindow as Ui_frmResults

class Create(QMainWindow, Ui_frmResults):

    def btn_click(self):
        sender = self.sender()
        if sender.objectName() == 'actionAdd_Prices':
            urllib3.disable_warnings()
            i = self.tbl_data.columnCount()
            if i == 9:
                s = 0
            else:
                s = 2
            Xbars = []
            Hyper_Data = pd.read_sql_query('Select * from hyper_pos ', self.parent.parent.con)
            # Hyper_Data.to_dict()
            # print(Hyper_Data)

            Hyper_Data.SKU = Hyper_Data.SKU.astype(float)

            # Hyper_Data.SKU = Hyper_Data.SKU.str.replace(' ', '')
            #
            # Hyper_Data.set_index("SKU", drop=True, inplace=True)
            #
            # Hyper_Data = Hyper_Data.to_dict(orient="index")
            for row in range(self.tbl_data.rowCount()):
                bar = self.tbl_data.item(row, s).text()
                self.lbl2.setText('{} %  Add Price Processing'.format(round(row / self.tbl_data.rowCount() * 100, 2)))
                QCoreApplication.processEvents()
                if bar != '' and bar != '_':
                    # print(type(bar), bar)
                    # print(bar)
                    # bar = '2030300062074'

                    # Hyper_Data = pd.read_sql_query('Select * from hyper_pos where SKU = {}'.format(bar),
                    #                                self.parent.parent.con)
                    # if Hyper_Data['Product Original Price'].to_list() != []:
                    bar = bar.replace(' ', '')
                    SELL_PRICE = Hyper_Data[Hyper_Data.SKU == float(bar)]['Product Original Price'].to_list()[0]
                    BSELL_PRICE = Hyper_Data[Hyper_Data.SKU == float(bar)]['Product Discount Price'].to_list()[0]
                    # BSELL_PRICE = Hyper_Data[Hyper_Data.SKU == int(bar)]['Product Original Price'].to_list()[0]
                    # else:
                        # req = requests.get(('https://prd-wd.hyperone.com:44300/sap/bc/getsalesprice/Sales/{}/00001'.format(bar)), auth=requests.auth.HTTPBasicAuth(username='', password=''), verify=False).json()
                        # BSELL_PRICE = req['DATATABLE'][0]['BSELL_PRICE']
                        # SELL_PRICE = req['DATATABLE'][0]['SELL_PRICE']
                        # BSELL_PRICE = 0
                        # SELL_PRICE = 0
                        # print(bar)
                        # Xbars.append(bar)
                    BSELL_PRICE = round(float(BSELL_PRICE), 2)
                    SELL_PRICE = round(float(SELL_PRICE), 2)
                    self.tbl_data.item(row, s + 2).setText(f"{BSELL_PRICE:.2f}")
                    self.tbl_data.item(row, s + 3).setText(f"{SELL_PRICE:.2f}")
            # print(len(Xbars))
            # print(Xbars)
            self.lbl2.setText('')
            show_pop('Done', 'Prices have been added', QMessageBox.Information)
        if sender.objectName() == 'actionCopy_to_Clipboard':
            self.copySelection()
        if sender.objectName() == 'actionExport_to_Microsoft_Excel':
            excel = win32com.client.Dispatch('Excel.Application')
            wb = excel.Workbooks.Add()
            wbs = wb.Worksheets.Add()
            wbs.Name = 'MyNewSheet'

            columnHeaders = []
            for i in range(8):
                columnHeaders.append(self.TWCat.headerItem().text(i))

            checked = dict()
            root = self.TWCat.invisibleRootItem()
            signal_count = root.childCount()

            for i in range(signal_count):
                signal = root.child(i)
                checked_sweeps = list()
                num_children = signal.childCount()

                for n in range(num_children):
                    child = signal.child(n)

                    if child.checkState(0) == QtCore.Qt.Checked:
                        checked_sweeps.append(child)

                checked[signal.text(0)] = checked_sweeps

            # print(checked)

            rows = []

            for bar, value in checked.items():
                if value != []:
                    for item in value:
                        record = []
                        for i in range(8):
                            record.append(item.text(i))
                        rows.append(record)

            if len(rows) == 0:
                iterator = QTreeWidgetItemIterator(self.TWCat)

                while iterator.value():
                    item = iterator.value()
                    record = []
                    if len(item.text(7)) > 0:
                        for i in range(8):
                            record.append(item.text(i))
                            # print(record)
                    if len(record) > 0:
                        rows.append(record)
                    iterator += 1

                    # item = root.child(i)
                    # url = item.text(0)  # text at first (0) column
                    # print(url)
                    # item.setText(1, 'result from %s' % url)  # update result column (1)

            # selection = self.tbl_data.selectedIndexes()
            # if selection:
            #     rows = []
            #     record = []
            #     for idx in self.tbl_data.selectionModel().selectedRows():
            #         record = []
            #         for col in range(self.tbl_data.columnCount()):
            #             record.append(self.tbl_data.item(idx.row(), col).text())
            #
            #         rows.append(record)
            #
            # else:
            #     rows = []
            #     for row in range(self.tbl_data.rowCount()):
            #         record = []
            #         for col in range(self.tbl_data.columnCount()):
            #             record.append(self.tbl_data.item(row, col).text())
            #
            #         rows.append(record)
            #
            # columnHeaders = []
            # for j in range(self.tbl_data.model().columnCount()):
            #     columnHeaders.append(self.tbl_data.horizontalHeaderItem(j).text())

            # print(rows[0])

            wbs.Range(wbs.Cells(2, 1), wbs.Cells(len(rows) + 1, len(columnHeaders))).Value = rows
            wbs.Range(wbs.Cells(1, 1), wbs.Cells(1, len(columnHeaders))).Value = columnHeaders
            wbs.Columns.WrapText = False
            with Obj(wbs.Cells) as (c):
                c.HorizontalAlignment = -4108
                c.VerticalAlignment = -4108
            wbs.Columns.AutoFit()
            excel.Visible = True

        elif sender.text() == 'Exit':
            self.close()

    def copySelection(self):
        # selection = self.TWCat.selectedIndexes()
        # selection2 = self.TWCat.selectedItems()
        # columns = sorted((index.column() for index in selection))

        checked = dict()
        root = self.TWCat.invisibleRootItem()
        signal_count = root.childCount()

        for i in range(signal_count):
            signal = root.child(i)
            checked_sweeps = list()
            num_children = signal.childCount()

            for n in range(num_children):
                child = signal.child(n)

                if child.checkState(0) == QtCore.Qt.Checked:
                    checked_sweeps.append(child)

            checked[signal.text(0)] = checked_sweeps

        # print(checked)

        s = ''

        for bar, value in checked.items():
            if value != []:
                for i in range(8):
                    s += self.TWCat.headerItem().text(i) + '\t'
                s += '\n'
                # print(s)
                for item in value:
                    for i in range(8):
                        s += item.text(i) + '\t'
                    s += '\n'
                # s += '\n'
                # print(value[0].text(0))
                # print(self.TWCat.headerItem().text(0))

        if s == '':
            iterator = QTreeWidgetItemIterator(self.TWCat)

            for i in range(8):
                s += self.TWCat.headerItem().text(i) + '\t'
            s += '\n'

            while iterator.value():
                item = iterator.value()
                record = []
                if len(item.text(7)) != 0:
                #     continue
                # else:
                    for i in range(8):
                        s += item.text(i) + '\t'
                    s += '\n'
                        # print(record)
                # if len(record) > 0:
                #     rows.append(record)
                iterator += 1

        # if selection:
        #
        #     s = ''
        #     x = 1
        #     for i in range(0, self.TWCat.columnCount()):
        #         if self.TWCat.isColumnHidden(i) == False:
        #             s = s + self.TWCat.headerItem().text(i) + '\t'
        #             x += 1
        #
        #     s = s + '\n'
        #     for index in selection:
        #         col = index.column()
        #         if index.parent():
        #             bar = str(index.parent().data())
        #         else:
        #             bar = str('')
        #         if index.data():
        #             data = str(index.data())
        #         else:
        #             data = str('')
        #         if col == columns[(-1)]:
        #             s = s + bar + data + '\n'
        #         else:
        #             s = s + bar + data + '\t'

            self.parent.parent.clipboard().setText(s)

    #     selection = self.tbl_data.selectedIndexes()
    #     columns = sorted((index.column() for index in selection))
    #     if selection:
    #         s = ''
    #         x = 1
    #         for i in range(0, self.tbl_data.columnCount()):
    #             if self.tbl_data.isColumnHidden(i) == False:
    #                 s = s + self.tbl_data.horizontalHeaderItem(i).text() + '\t'
    #                 x += 1
    #
    #         s = s + '\n'
    #         for index in selection:
    #             col = index.column()
    #             if index.data():
    #                 data = str(index.data())
    #             else:
    #                 data = str('')
    #             if col == columns[(-1)]:
    #                 s = s + data + '\n'
    #             else:
    #                 s = s + data + '\t'
    #
    #         self.parent.parent.clipboard().setText(s)

    def doubleClickedItem(self, index):
        pass

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonDblClick:
            if source is self.TWCat.viewport():
                if event.buttons() == QtCore.Qt.RightButton:
                    item = self.TWCat.itemAt(event.pos())
                    import frmAddSKU
                    self.frm_AddSKU = frmAddSKU.Create(self)
                    self.frm_AddSKU.show()
                else:
                    if event.buttons() == QtCore.Qt.LeftButton:
                        item = self.TWCat.itemAt(event.pos())
                        # print(item.text(7))
                        # i = self.TWCat.columnCount() - 2
                        # url = self.TWCat.item(i).text()
                        url = item.text(7)
                        if len(url) > 0:
                            self.parent.Driver()
                            self.parent.driver.get(url)
        return super(Create, self).eventFilter(source, event)

    def __init__(self, parent=None):
        super(Create, self).__init__()
        self.parent = parent
        self.setupUi(self)
        self.TWCat = self.findChild(QTreeWidget, 'TWCat')
        # self.toolBar = self.findChild(QToolBar, 'toolBar')
        self.menubar = self.findChild(QMenuBar, 'menubar')
        # Add_toolbar(self, self.toolBar, QIcon(
        #     '.\\res\\01.png'), 'Scraping', False)
        # Add_toolbar(self, self.toolBar, QIcon('.\\res\\02.png'), 'Add', False)
        # Add_toolbar(self, self.toolBar, QIcon(
        #     '.\\res\\03.png'), 'Remove', False)
        # self.toolBar.addSeparator()
        # Add_toolbar(self, self.toolBar, QIcon(
        #     '.\\res\\09.png'), 'All Products', False)
        # self.read_db()
        # self.options = webdriver.ChromeOptions()
        # self.options.add_argument('--disable-infobars')
        # self.options.add_experimental_option(
        #     'excludeSwitches', ['enable-logging'])
        # self.driver = webdriver.Chrome(
        #     options=(self.options), executable_path='.\\chromedriver.exe')
        # self.driver = 0
        # with Obj(self) as (_):
        #     _.lbl1 = QLabel()
        #     _.lbl1.setText(
        #         u"<B>Web Scraping v0.01 \xa9 2021 <span style='color:Blue'>Hyper</span><span style='color:red'>One</span> Application Team. All rights reserved</B>")
        #     _.statusBar().addWidget(_.lbl1)
        # self.tbl_data = self.findChild(QTableWidget, 'tableWidget')
        self.TWCat.viewport().installEventFilter(self)
        self.TWCat.doubleClicked.connect(self.doubleClickedItem)
        self.actionCopy_to_Clipboard = self.findChild(QAction, 'actionCopy_to_Clipboard')
        self.actionExport_to_Microsoft_Excel = self.findChild(QAction, 'actionExport_to_Microsoft_Excel')
        # self.AddPrice = self.findChild(QAction, 'actionAdd_Prices')
        # self.AddPrice.triggered.connect(self.btn_click)
        self.Exit = self.findChild(QAction, 'act_Exit')
        self.Exit.triggered.connect(self.btn_click)
        self.actionCopy_to_Clipboard.triggered.connect(self.btn_click)
        self.actionExport_to_Microsoft_Excel.triggered.connect(self.btn_click)

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