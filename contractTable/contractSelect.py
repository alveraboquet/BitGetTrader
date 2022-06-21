
from PyQt5 import QtWidgets
from . import const as c
from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QToolButton, QHBoxLayout, QListWidget, QListWidgetItem, QStyle
from .customizeHeaders import CustomHeaders
from bitget.mix.market_api import MarketApi
import PyQt5.QtCore as QtCore
   
#Main Window
class ContractSelect(QWidget):
    """QWidget displaying contracts available for graphing"""
    def __init__(self, mAPI):
        super().__init__()
        self.left = 0
        self.top = 0
        self.width = 600
        self.height = 400
        self.setWindowTitle("Pair Select")
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color:#121212;")
        self.types = c.TYPES[0]

        self.lSelect = ""
        self.rSelect = ""

        self.headers = c.DEFAULT_HEADERS
        self.allHeaders = c.CONTRACT_HEADERS | c.TICKER_HEADERS
        self.unusedHeaders = { x : self.allHeaders[x] for x in set(self.allHeaders) - set(self.headers) }

        self.mAPI = mAPI
        self.table = self.buildTable()
        self.toolbar = self.buildToolbar()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)
   
        #Show window
        self.show()
   
    #Create table of 'self.types' type contracts based on headers specified in field 'self.headers'
    def buildTable(self):

        # Table Customization
        self.tableWidget = QTableWidget()
        
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        
        self.tableWidget.horizontalHeader().setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.horizontalHeader().setStyleSheet("::section{background-color:#3D3D3D; color: white;}")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.tableWidget.verticalHeader().setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.verticalHeader().setStyleSheet("::section{background-color:#3D3D3D; color: white;}")
        
        self.tableWidget.setStyleSheet("QWidget{background-color:#282828; color: white; alternate-background-color:#3D3D3D;}" + 
                                  "QTableWidget QTableCornerButton::section { background-color: #3D3D3D; }")
        
        self.getTableData()

        # Table Sorting
        self.tableWidget.setSortingEnabled(True)

        
        return self.tableWidget

    def getTableData(self):
        # Get list of contract dictionaries, union respective dictionaries
        contractsInfo = self.mAPI.contracts(self.types)["data"]
        tickersInfo = self.mAPI.tickers(self.types)["data"]
        for x in range(0,len(contractsInfo)):
            tickersInfo[x] = contractsInfo[x] | tickersInfo[x]

        self.tableWidget.setColumnCount(len(self.headers))
        self.tableWidget.setHorizontalHeaderLabels(self.headers.values())

        self.tableWidget.setRowCount(len(contractsInfo))
        # Filter out non-header items from combined tickersInfo
        # Append all header items to a respective dictionary within the contracts list.
        contracts = []
        for contract in tickersInfo:
            tempContract = {}
            for key, val in contract.items():
                if key in self.headers.keys():
                    tempContract[key] = val 
            contracts.append(tempContract)

        # Pack all contracts into table
        for index1 in range(0, len(contracts)):
            keys = list(self.headers.keys())
            for index2 in range(0, len(keys)):
                # Attempt to pack each value matching self.header keys into the table
                try:
                    newItem = QTableWidgetItem()
                    # Split symbol from type (e.g. BTCUSDT_UMCBL -> BTCUSDT)
                    if keys[index2] == "symbol":
                        newItem.setData(QtCore.Qt.DisplayRole, contracts[index1][keys[index2]].split("_")[0])
                    else:
                        newItem.setData(QtCore.Qt.DisplayRole, float(contracts[index1][keys[index2]]))
                    self.tableWidget.setItem(index1,index2,newItem)
                # If corresponding value cannot be found for key, pack N/A.
                except Exception as e:
                    self.tableWidget.setItem(index1,index2,QTableWidgetItem("N/A"))

    def buildToolbar(self):
        widget = QWidget()
        columnsButton = QToolButton()
        columnsButton.setText("Customize Headers")
        columnsButton.clicked.connect(self.buildHeaderUI)
        layout = QVBoxLayout(widget)
        layout.addWidget(columnsButton)
        widget.setLayout(layout)
        widget.setStyleSheet("QWidget{background-color:#282828; color: white;}")
        widget.setFixedHeight(50)
        return widget

    def applyHeaderChanges(self):
        self.headers = self.tempUsedHeaders
        self.unusedHeaders = self.tempUnusedHeaders
        self.headerWin.close()
        self.getTableData()

    def getHeaderFromVal(self, headerVal):
        for x in self.allHeaders.keys():
            if headerVal == self.allHeaders.get(x):
                return {x: headerVal}

    def getKeyFromPair(self, dictPair):
        for x in dictPair.keys():
            return x

    def makeUnused(self):
        row = self.usedList.currentRow()
        if isinstance(row, int):
            item = self.usedList.takeItem(row)
            headerVal = item.text()

            dictPair = self.getHeaderFromVal(headerVal)
            if dictPair not in self.tempUnusedHeaders.items():
                self.tempUnusedHeaders = self.tempUnusedHeaders | dictPair    
                self.unusedList.addItem(item)
                del self.tempUsedHeaders[self.getKeyFromPair(dictPair)]
                self.tempUnusedHeaders = { x : self.allHeaders[x] for x in set(self.allHeaders) - set(self.tempUsedHeaders) }

    def makeUsed(self):
        row = self.unusedList.currentRow()
        if row > -1:
            item = self.unusedList.takeItem(row)
            headerVal = item.text()

            dictPair = self.getHeaderFromVal(headerVal)
            if dictPair not in self.headers.items():
                self.tempUsedHeaders = self.tempUsedHeaders | dictPair   
                self.usedList.addItem(item)
                self.tempUnusedHeaders = { x : self.allHeaders[x] for x in set(self.allHeaders) - set(self.tempUsedHeaders) }

    def buildHeaderUI(self):
        self.headerWin = QWidget()
        self.topHeaderWin = QWidget()
        self.topHeaderLayout = QHBoxLayout()
        self.topHeaderWin.setLayout(self.topHeaderLayout)

        # populate used/unused headers list
        self.usedList = QListWidget()
        self.tempUsedHeaders = self.headers
        for x in self.tempUsedHeaders.values():
            tempItem = QListWidgetItem(x)
            self.usedList.addItem(tempItem)

        self.unusedList = QListWidget()
        self.tempUnusedHeaders = self.unusedHeaders
        for x in self.tempUnusedHeaders.values():
            tempItem = QListWidgetItem(x)
            self.unusedList.addItem(tempItem)
        
        self.topHeaderLayout.addWidget(self.usedList)
        self.topHeaderLayout.addWidget(self.unusedList)

        # create tool buttons window
        toolsWin = QWidget()
        toolsLayout = QHBoxLayout(toolsWin)

        # create tool buttons
        arrowRight = self.style().standardIcon(QStyle.SP_ArrowRight)
        makeUnusedButton = QPushButton(arrowRight,"Make Unused")
        makeUnusedButton.clicked.connect(self.makeUnused)
        toolsLayout.addWidget(makeUnusedButton)
        
        arrowLeft = self.style().standardIcon(QStyle.SP_ArrowLeft)
        makeUsedButton = QPushButton(arrowLeft,"Make Used")
        makeUsedButton.clicked.connect(self.makeUsed)
        toolsLayout.addWidget(makeUsedButton)        

        confirm = self.style().standardIcon(QStyle.SP_DialogApplyButton)
        applyButton = QPushButton(confirm,"Apply Changes")
        applyButton.clicked.connect(self.applyHeaderChanges)
        toolsLayout.addWidget(applyButton)

        cancel = self.style().standardIcon(QStyle.SP_DialogCancelButton)
        discardButton = QPushButton(cancel,"Discard Changes")
        discardButton.clicked.connect(self.headerWin.close)
        toolsLayout.addWidget(discardButton)

        toolsWin.setLayout(toolsLayout)
        
        layout = QVBoxLayout()
        layout.addWidget(self.topHeaderWin)
        layout.addWidget(toolsWin)
        self.headerWin.setLayout(layout)
        self.headerWin.show()