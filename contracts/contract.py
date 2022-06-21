class Contract:

    def __init__(self, contract, ticker): 
        self.symbol = contract[0]
        self.maker = contract[1]
        self.taker = contract[2]
        self.feeRate = contract[3]
        self.openCost = contract[4]
        self.quote = contract[5]
        self.base = contract[6]
        self.buyRatio = contract[7]
        self.sellRatio = contract[8]
        self.marginCoins = contract[9]
        self.minTradeNum = contract[10]
        self.priceEndStep = contract[11]
        self.volumePlace = contract[12]
        self.pricePlace = contract[13]

        self.last = ticker[1]
        self.bestAsk = ticker[2]
        self.bestBid = ticker[3]
        self.high24h = ticker[4]
        self.low24h = ticker[5]
        self.timechecked = ticker[6]
        self.baseVolume = ticker[7]
        self.quoteVolume = ticker[8]
        self.usdtVolume = ticker[9]




