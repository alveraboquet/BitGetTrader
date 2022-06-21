
from datetime import datetime
class Candle:

    # T -> Time, O -> Open, H -> High, L -> Low, C -> Close, B -> BaseVol, Q -> QuoteVol
    def __init__(self, t: float, o: float, h: float, l: float, c: float, b: float, q: float):
        self.t = t
        self.o = o
        self.h = h
        self.l = l
        self.c = c
        self.b = b
        self.q = q
    
    def __str__(self):
        return ("Candle @ " + str(datetime.fromtimestamp(int(self.t)/1000))
                +"\no: $" +str(self.o) +"\nClose: $" +str(self.c)
                +"\nHigh: $" +str(self.h) +"\nLow: $" +str(self.l) 
                +"\nBase Volume: " +str(self.b) +"\nQuote Volume: $"
                +str(self.q) + "\n")