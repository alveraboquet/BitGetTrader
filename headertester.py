import sys
from bitget.mix.market_api import MarketApi 
from PyQt5.QtWidgets import QApplication
from screener.headers import CustomHeaders
from screener.const import DEFAULT_HEADERS
app = QApplication(sys.argv)
app.setStyle('Fusion')
mAPI = MarketApi("bg_0d456f8fe40db4bcfc8300b4e6242b75","74de60c68c9ea07d20b13aa0c6d849668810fcb71993434a33469f65fc71152b","meyerClaire30", use_server_time=False, first=False)

c = CustomHeaders(DEFAULT_HEADERS)

sys.exit(app.exec_())