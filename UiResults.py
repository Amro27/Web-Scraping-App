# uncompyle6 version 3.8.1.dev0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: UiResults.py
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(823, 619)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('res/09.png'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName('verticalLayout')
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName('verticalLayout_2')
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(799, 569))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName('tableWidget')
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(49)
        self.tableWidget.verticalHeader().setDefaultSectionSize(37)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 823, 26))
        self.menubar.setObjectName('menubar')
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName('menuFile')
        MainWindow.setMenuBar(self.menubar)
        self.actionCopy_to_Clipboard = QtWidgets.QAction(MainWindow)
        self.actionCopy_to_Clipboard.setObjectName('actionCopy_to_Clipboard')
        self.actionExport_to_Microsoft_Excel = QtWidgets.QAction(MainWindow)
        self.actionExport_to_Microsoft_Excel.setObjectName('actionExport_to_Microsoft_Excel')
        self.actionAdd_Prices = QtWidgets.QAction(MainWindow)
        self.actionAdd_Prices.setObjectName('actionAdd_Prices')
        self.menuFile.addAction(self.actionCopy_to_Clipboard)
        self.menuFile.addAction(self.actionExport_to_Microsoft_Excel)
        self.menuFile.addAction(self.actionAdd_Prices)
        self.menubar.addAction(self.menuFile.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate('MainWindow', 'Results'))
        self.tableWidget.setSortingEnabled(True)
        self.menuFile.setTitle(_translate('MainWindow', 'File'))
        self.actionCopy_to_Clipboard.setText(_translate('MainWindow', 'Copy to Clipboard'))
        self.actionCopy_to_Clipboard.setShortcut(_translate('MainWindow', 'Ctrl+C'))
        self.actionExport_to_Microsoft_Excel.setText(_translate('MainWindow', 'Export to Microsoft Excel'))
        self.actionExport_to_Microsoft_Excel.setShortcut(_translate('MainWindow', 'Ctrl+E'))
        self.actionAdd_Prices.setText(_translate('MainWindow', 'Add Prices'))