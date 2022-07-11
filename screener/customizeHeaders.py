from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QWidget, QListWidget, QListWidgetItem, QStyle
from . import const as c


class CustomHeaders(QWidget):
    """description of class"""
    def __init__(self, headers):
        super().__init__()
        self.allHeaders = c.CONTRACT_HEADERS | c.TICKER_HEADERS
        self.usedHeaders = headers
        self.initialUsed = self.usedHeaders
        
        self.unusedHeaders = { x : self.allHeaders[x] for x in set(self.allHeaders) - set(self.usedHeaders) }
        self.initialUnused = self.unusedHeaders

        self.buildUI()
        self.show()

    def buildUI(self):
        topWin = QWidget()
        topLayout = QHBoxLayout()
        topWin.setLayout(topLayout)

        # populate used/unused headers list
        used = QListWidget()
        for x in self.usedHeaders.values():
            tempItem = QListWidgetItem(x)
            used.addItem(tempItem)

        unused = QListWidget()
        for x in self.unusedHeaders.values():
            tempItem = QListWidgetItem(x)
            unused.addItem(tempItem)
        
        topLayout.addWidget(used)
        topLayout.addWidget(unused)

        # create tool buttons window
        toolsWin = QWidget()
        toolsLayout = QHBoxLayout(toolsWin)

        # create tool buttons
        arrowRight = self.style().standardIcon(QStyle.SP_ArrowRight)
        makeUnused = QPushButton(arrowRight,"Make Unused")
        toolsLayout.addWidget(makeUnused)
        
        arrowLeft = self.style().standardIcon(QStyle.SP_ArrowLeft)
        makeUsed = QPushButton(arrowLeft,"Make Used")
        toolsLayout.addWidget(makeUsed)        

        confirm = self.style().standardIcon(QStyle.SP_DialogApplyButton)
        applyButton = QPushButton(confirm,"Apply Changes")
        toolsLayout.addWidget(applyButton)

        cancel = self.style().standardIcon(QStyle.SP_DialogCancelButton)
        discardButton = QPushButton(cancel,"Discard Changes")
        discardButton.clicked.connect(self.close)
        toolsLayout.addWidget(discardButton)

        toolsWin.setLayout(toolsLayout)
        
        layout = QVBoxLayout()
        layout.addWidget(topWin)
        layout.addWidget(toolsWin)
        self.setLayout(layout)