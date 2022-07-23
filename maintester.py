import sys
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
app.setStyle('Fusion')


# Screener Tests
#from screener.screener import Screener
#from bitget.mix.market_api import MarketApi 
#mAPI = MarketApi("bg_0d456f8fe40db4bcfc8300b4e6242b75","74de60c68c9ea07d20b13aa0c6d849668810fcb71993434a33469f65fc71152b","meyerClaire30", use_server_time=False, first=False)
#c = Screener(mAPI)

# Tracker Tests
from tracker.trackerGUI import TrackerGUI
t = TrackerGUI()

sys.exit(app.exec_())