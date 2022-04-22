# uncompyle6 version 3.5.0
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.5 (default, Nov 16 2020, 22:23:17)
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-44)]
# Embedded file name: Web Scraping.py
# Size of source mod 2**32: 12742 bytes
from MyLib import *
from threading import Thread
from UiWebScraping import Ui_MainWindow as Web_Scraping_Ui


class Create(QMainWindow, Web_Scraping_Ui):

    def run(self, url):
        self.driver.get(url)

    def read_db(self):
        self.TWCat.clear()
        All = QtWidgets.QTreeWidgetItem(self.TWCat)
        All.setData(0, Qt.UserRole, 'root')
        All.setText(0, 'All')
        All.setFlags(All.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
        All.setIcon(0, QIcon('.\\res\\07.png'))
        self.parent.cur.execute(
            "SELECT data_urls.ID,data_urls.`Category Name`,data_urls.`Sub Category Name`,data_urls.URL FROM data_urls")
        # WHERE data_urls.`MAC address` = '{}';".format(self.parent.MACaddress))
            # "")

        data = self.parent.cur.fetchall()
        for row in data:
            item = None
            for _ in self.TWCat.findItems((row[1]), (Qt.MatchExactly | Qt.MatchRecursive), column=0):
                if _.data(0, Qt.UserRole) == "data_urls.`Category Name`='{}'".format(row[1]):
                    item = _
                    break

            if item == None:
                item = QtWidgets.QTreeWidgetItem(All)
                item.setData(0, Qt.UserRole,
                             "data_urls.`Category Name`='{}'".format(row[1]))
                item.setText(0, row[1])
                item.setFlags(item.flags() | Qt.ItemIsTristate |
                              Qt.ItemIsUserCheckable)
                item.setIcon(0, QIcon('.\\res\\07.png'))
            _ = QtWidgets.QTreeWidgetItem(item)
            _.setData(0, Qt.UserRole, 'ID={}'.format(row[0]))
            _.setText(0, row[2])
            _.setText(1, row[3])
            _.setFlags(_.flags() | Qt.ItemIsUserCheckable)
            _.setCheckState(0, Qt.Unchecked)
            _.setIcon(0, QIcon('.\\res\\04.png'))

        self.TWCat.expandAll()
        self.TWCat.resizeColumnToContents(0)

    def btn_click(self):
        sender = self.sender()
        if type(sender) == QAction:
            pass
        if sender.text() == 'Add':
            import frmAdd
            self.frm_Add = frmAdd.Create(self)
            self.frm_Add.show()
            currentItem = self.TWCat.currentItem()
            if currentItem:
                self.frm_Add.txt_cat_name.setText(currentItem.text(0))
        elif sender.text() == 'Remove':
            if QMessageBox.question(self, 'Remove', 'Are you sure ?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
                currentItem = self.TWCat.currentItem()
                if currentItem:
                    where = currentItem.data(0, Qt.UserRole)
                    if where == 'root':
                        self.parent.cur.execute(
                            "DELETE FROM data_urls WHERE data_urls.`MAC address` = '{}';".format(self.parent.MACaddress))
                    else:
                        self.parent.cur.execute("DELETE FROM data_urls WHERE {} AND data_urls.`MAC address` = '{}';".format(
                            where, self.parent.MACaddress))
                        # print("DELETE FROM data_urls WHERE {} AND data_urls.`MAC address` = '{}';".format(
                        #     where, self.parent.MACaddress))
                        self.parent.con.commit()
                        self.read_db()
                else:
                    show_pop('Error', 'There is no selection to delete',
                             QMessageBox.Critical)
        elif sender.text() == 'All Products':
            import frmResults
            self.frm_Results = frmResults.Create(self)
            self.TWCat = self.frm_Results.findChild(QTreeWidget, 'TWCat')
            _translate = QtCore.QCoreApplication.translate

            # self.Data = pd.read_sql_query(
            #     'SELECT   data.SKU,data.`Product Name`,data.`Product Original Price`,data.`Product Discount Price`,data.`Date Update`,data.Link,data.`Product Id` FROM data;',
            #     self.parent.con)

            # self.parent.cur.execute(
            #     'SELECT   data.SKU,data.`Product Name`,data.`Product Original Price`,data.`Product Discount Price`,data.`Date Update`,data.Link,data.`Product Id` FROM data;')

            self.parent.cur.execute(
                'SELECT data1.BAR AS SKU ,data.`Product Name`,data.`Product Original Price`,data.`Product Discount Price`,data.`Date Update`,data.Link,data.`Product Id` FROM data '
                'join data1 on data1.DESC = data.`Product Name`;')

            self.data = self.parent.cur.fetchall()

            Hyper_Data = pd.read_sql_query(
                'Select SKU, `Product Original Price`, `Product Discount Price` from hyper_pos ', self.parent.con)

            self.Names = ['SKU', 'Product Name', 'Product Original Price', 'Product Discount Price',
                          'Hyper Original Price', 'Hyper Discount Price', 'Date Update', 'Link']

            for i in range(len(self.Names)):
                self.TWCat.headerItem().setText(i, _translate('MainWindow', self.Names[i]))
                if self.Names[i] == 'Product Name':
                    self.TWCat.setColumnWidth(i, len(self.Names[i]) + 320)
                else:
                    self.TWCat.setColumnWidth(i, len(self.Names[i]) + 120)
                # self.TWCat.setExpanded(i, True)
            # self.TWCat.resizeColumnToContents(0)

            Data = pd.read_sql_query(
                'Select data1.BAR `SKU`, data.`Product Name`, data.`Product Original Price`, case when data.`Product Discount Price` = 0 then data.`Product Original Price` else data.`Product Discount Price` end `Product Discount Price`, data.`Date Update`, data.Link from data join data1 on data1.DESC = data.`Product Name`;',
                self.parent.con)

            Data['Product Discount Price'] = Data['Product Discount Price'].apply(
                lambda x: 0 if x == '' else x)

            Data['Product Original Price'] = Data['Product Original Price'].apply(
                lambda x: 0 if x == '' else x)

            Data.SKU = Data.SKU.str.replace('\n', '')

            bar_lst = sorted(list(Data.SKU.unique()))

            bar_lst.pop(0)

            bar_lst.append('')

            Hyper_Data.SKU = Hyper_Data.SKU.str.replace(' ', '').to_list()

            # Data_Dict = {}

            for bar in bar_lst:

                # if bar == bar_lst[2]:
                #     break

                # if '47245844000530' in bar:
                #     print(Hyper_Data[Hyper_Data.SKU == bar])

                if bar in Hyper_Data.SKU.to_list():
                    Hyper_Sell_Price = float(Hyper_Data[Hyper_Data.SKU == bar]['Product Original Price'].values[0])
                    Hyper_Prom_Price = float(Hyper_Data[Hyper_Data.SKU == bar]['Product Discount Price'].values[0])
                else:
                    Hyper_Sell_Price = 0
                    Hyper_Prom_Price = 0
                Data_lst = list(Data[Data.SKU == bar].values)

                bar_item = QtWidgets.QTreeWidgetItem(self.TWCat)
                bar_item.setText(0, bar)
                bar_item.setFlags(bar_item.flags() | Qt.ItemIsTristate |
                              Qt.ItemIsUserCheckable)

                for i in range(len(Data_lst)):
                    # print(Data_lst[i][1])
                    _ = QtWidgets.QTreeWidgetItem(bar_item)
                    _.setText(0, Data_lst[i][0])
                    _.setText(1, Data_lst[i][1])
                    _.setText(2, str(Data_lst[i][2]))
                    _.setText(3, str(Data_lst[i][3]))
                    _.setText(4, str(Hyper_Sell_Price))
                    _.setText(5, str(Hyper_Prom_Price))
                    _.setText(6, Data_lst[i][4].strftime("%d/%m/%Y"))
                    _.setText(7, Data_lst[i][5])
                    _.setFlags(_.flags() | Qt.ItemIsUserCheckable)
                    _.setCheckState(0, Qt.Unchecked)
                    # _.setText(2, self.Names[3])

                # _ = QtWidgets.QTreeWidgetItem(bar_item)
                # _.setText(1, self.Names[2])
                # _.setText(2, self.Names[3])

            self.TWCat.expandAll()
            self.TWCat.resizeColumnToContents(0)


            # item.setIcon(0, QIcon('.\\res\\07.png'))




            # self.TWCat.headerItem().setText(0, _translate('MainWindow', 'Category'))
            # self.TWCat.headerItem().setText(1, _translate('MainWindow', 'URL'))

            # tbl_data = self.frm_Results.tbl_data
            # tbl_data.setColumnCount(9)
            # tbl_data.setHorizontalHeaderLabels(['SKU', 'Product Name', 'HyperOne Original Price', 'HyperOne Discount Price',
            #                                    'Product Original Price', 'Product Discount Price', 'Date Update', 'Link', 'Product Id'])
            # tbl_data.hideColumn(8)
            # self.parent.cur.execute(
            #     'SELECT   data.SKU,data.`Product Name`,data.`Product Original Price`,data.`Product Discount Price`,data.`Date Update`,data.Link,data.`Product Id` FROM data;')
            # data = self.parent.cur.fetchall()
            # for row in data:
            #     _ = list(row)
            #     _.insert(2, '')
            #     _.insert(3, '')
            #     row = tuple(_)
            #     cell = tbl_data.rowCount()
            #     tbl_data.setRowCount(cell + 1)
            #     [tbl_data.setItem(cell, x, QTableWidgetItem(
            #         str(y).strip())) for x, y in enumerate(row)]
            #
            # with Obj(self.frm_Results) as (_):
            #     _.lbl1 = QLabel('Label: ')
            #     _.lbl1.setStyleSheet('border: 0; color:  blue;')
            #     _.lbl1.setText('{} found records'.format(
            #         _.tbl_data.rowCount()))
            #     _.lbl2 = QLabel('Label: ')
            #     _.lbl2.setStyleSheet('border: 0; color:  blue;')
            #     _.lbl2.setText('')
            #     _.statusBar().addWidget(_.lbl1)
            #     _.statusBar().addWidget(_.lbl2)
            #     _.show()
            self.frm_Results.show()
        elif sender.text() == 'Scraping':

            self.Driver()

            import frmResults1
            self.frm_Results = frmResults1.Create(self)
            self.frm_Results.tbl_data.setColumnCount(10)
            self.frm_Results.tbl_data.setHorizontalHeaderLabels(
                ['Host Name', 'Sub Category', 'SKU', 'Product Name', 'HyperOne Original Price', 'HyperOne Discount Price', 'Product Original Price', 'Product Discount Price', 'Link', 'Product Id'])
            self.frm_Results.tbl_data.hideColumn(9)
            self.cnt = 0

            def recurse(parent_item):
                for i in range(parent_item.childCount()):
                    child = parent_item.child(i)
                    grand_children = child.childCount()
                    if grand_children > 0:
                        recurse(child)
                    if child.checkState(0) == Qt.Checked:
                        hostname = ''
                        if child.text(1):
                            self.cnt += 1
                            hostname = urlparse(
                                child.text(1)).netloc.upper()
                            self.driver.get(child.text(1))
                            # print(hostname)
                        # print(hostname)
                        if hostname == 'WWW.CARREFOUREGYPT.COM':
                            Carrefouregypt(
                                self.driver, hostname, self.frm_Results.tbl_data, child.text(0), self.parent)
                        elif hostname == '2B.COM.EG':
                            TWO_B(self.driver, hostname, self.frm_Results.tbl_data, child.text(
                                0), self.parent)
                        elif hostname == 'CAIROSALES.COM':
                            Cairosales(
                                self.driver, hostname, self.frm_Results.tbl_data, child.text(0), self.parent)
                        elif hostname == 'BTECH.COM':
                            BTECH(self.driver, hostname, self.frm_Results.tbl_data, child.text(
                                0), self.parent)
                        elif hostname == 'WWW.JUMIA.COM.EG':
                            Jumia(self.driver, hostname, self.frm_Results.tbl_data, child.text(
                                0), self.parent)
                        elif hostname == 'WWW.AMAZON.EG':
                            Amazon(self.driver, hostname, self.frm_Results.tbl_data, child.text(
                                0), self.parent)

            recurse(self.TWCat.invisibleRootItem())
            if self.cnt == 0:
                show_pop('Error', 'There is no Checked to Scraping',
                         QMessageBox.Critical)
            else:
                with Obj(self.frm_Results) as (_):
                    _.lbl1 = QLabel('Label: ')
                    _.lbl1.setStyleSheet('border: 0; color:  blue;')
                    _.lbl1.setText('{} found records'.format(
                        _.tbl_data.rowCount()))
                    _.lbl2 = QLabel('Label: ')
                    _.lbl2.setStyleSheet('border: 0; color:  blue;')
                    _.lbl2.setText('')
                    _.statusBar().addWidget(_.lbl1)
                    _.statusBar().addWidget(_.lbl2)
                    _.show()
        elif sender.text() in ('Amazon', 'Souq', 'Carrefouregypt', '2B', 'Cairosales',
                               'Btech', 'Jumia'):

            self.Driver()

            URL = {'Amazon': 'https://www.amazon.eg/',  'Souq': 'https://deals.souq.com/',  'Carrefouregypt': 'https://www.carrefouregypt.com/mafegy/ar',
                   '2B': 'https://2b.com.eg/ar/',  'Cairosales': 'https://cairosales.com/',  'Btech': 'https://btech.com/',  'Jumia': 'https://www.jumia.com.eg/'}
            self.driver.get(URL[sender.text()])
        elif sender.text() == 'Exit':
            self.close()
        if sender.text() == 'Registration':
            pass

    def Driver(self):

        error = 'not connected to DevTools'

        try:

            if self.driver == 0:
                self.driver = webdriver.Chrome(options=(self.options),
                                               executable_path='.\\chromedriver.exe')

            elif error in self.driver.get_log('driver')[-1]['message']:
                # print('Browser window closed by user')
                self.driver = webdriver.Chrome(options=(self.options),
                                               executable_path='.\\chromedriver.exe')
            else:
                pass
                # print(self.driver.get_log('driver')[-1]['message'])

        except IndexError:
            pass

    def closeEvent(self, *args, **kwargs):
        try:
            try:
                self.driver.close()
                self.driver.quit()
            except Exception as e:
                try:
                    pass
                finally:
                    e = None
                    del e

        finally:
            sys.exit()

    def __init__(self, parent=None):
        super(Create, self).__init__()
        self.parent = parent
        self.setupUi(self)
        [self.findChild(QAction, _).triggered.connect(self.btn_click) for _ in ('URL_Amazon',
                                                                                'URL_Carrefouregypt',
                                                                                'URL_2B',
                                                                                'URL_Cairosales',
                                                                                'URL_Btech',
                                                                                'URL_Jumia',
                                                                                'act_Exit')]
        self.TWCat = self.findChild(QTreeWidget, 'TWCat')
        self.toolBar = self.findChild(QToolBar, 'toolBar')
        self.menubar = self.findChild(QMenuBar, 'menubar')
        Add_toolbar(self, self.toolBar, QIcon(
            '.\\res\\01.png'), 'Scraping', False)
        Add_toolbar(self, self.toolBar, QIcon('.\\res\\02.png'), 'Add', False)
        Add_toolbar(self, self.toolBar, QIcon(
            '.\\res\\03.png'), 'Remove', False)
        self.toolBar.addSeparator()
        Add_toolbar(self, self.toolBar, QIcon(
            '.\\res\\09.png'), 'All Products', False)
        self.read_db()
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--disable-infobars')
        self.options.add_experimental_option(
            'excludeSwitches', ['enable-logging'])
        # self.driver = webdriver.Chrome(
        #     options=(self.options), executable_path='.\\chromedriver.exe')
        self.driver = 0
        with Obj(self) as (_):
            _.lbl1 = QLabel()
            _.lbl1.setText(
                u"<B>Web Scraping v0.02 \xa9 2021 <span style='color:Blue'>Hyper</span><span style='color:red'>One</span> Application Team. All rights reserved</B>")
            _.statusBar().addWidget(_.lbl1)
        self.show()


class MyApp(QApplication):

    def __init__(self, *args):
        (super(MyApp, self).__init__)(*args)
        self.setStyle('Fusion')
        self.con = mysql.connect(host='192.168.1.83', user='ehasanin',
                                 passwd='123P@ssword', db='H1WebScrap', charset='utf8mb4')
        self.cur = self.con.cursor()
        self.cur.execute('SELECT  static_key.`Key` FROM static_key')
        data = self.cur.fetchall()
        # self.cur.execute("SELECT  `MAC address`, `Key` FROM registration where `User Name` = 'omarh' ")
        self.MACaddress = hex(uuid.getnode())
        self.Key = AESCipher('078652134').encrypt(
            hex(uuid.getnode()) + data[0][0]).decode('utf8')
        # data = self.cur.fetchall()
        # self.MACaddress = data[0][0]
        # self.Key = data[0][1]
        rows_count = self.cur.execute(
            "SELECT * FROM registration WHERE registration.`MAC address` = '{}';".format(self.MACaddress))
        data = self.cur.fetchall()
        self.Last_OTP_Sent = None
        if rows_count == 0:
            UserName = os.getlogin()
            ComputerName = win32api.GetComputerName()
            IpInfo = requests.get('http://ipinfo.io/json').text
            self.cur.execute("INSERT INTO registration (`Key`,`MAC address`, `User Name`,`Computer Name`,`Ip Info`) VALUES ('{}','{}', '{}','{}','{}');".format(
                self.Key, self.MACaddress, UserName, ComputerName, IpInfo[1:-1].strip()))
            self.con.commit()
            self.Count_OTP_Sent = 0
            self.Registered = 0
        else:
            self.Last_OTP_Sent = data[0][7]
            self.Count_OTP_Sent = data[0][8]
            self.Registered = data[0][4]
            if data[0][5] == 1 and self.Registered == 1 or self.Registered == 0 and self.Count_OTP_Sent >= 5:
                show_pop(
                    'banned', 'You have been banned from entering the program', QMessageBox.Critical)
                sys.exit()
        if self.Registered == 1:
            self.frm_Web_Scraping = Create(self)
        else:
            import frmRegistration
            self.frm_Registration = frmRegistration.Create(self)
            if self.frm_Registration.exec_() == 2:
                self.frm_Web_Scraping = Create(self)
            else:
                sys.exit()


if __name__ == '__main__':
    app = MyApp(sys.argv)
    sys.exit(app.exec_())
