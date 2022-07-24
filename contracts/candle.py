
from datetime import datetime
class Candle:

    def __init__(self, t:float=0, o:float=0, h:float=0, l:float=0, c:float=0, b:float=0, q:float=0):
        """ T -> Time, O -> Open, H -> High, L -> Low, C -> Close, B -> BaseVol, Q -> QuoteVol """
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