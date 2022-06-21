from contracts.contract import Contract
from . import const as c

def getContractsInfo(mAPI, types):
    return mAPI.contracts(types)["data"]

def getTickersInfo(mAPI, types):
    return mAPI.tickers(types)["data"]



    tempContract = Contract()
    #for x in data2:
    #    temp2 = [x[1] for x in list(x.items())]
    #    temp2[0] = temp2[0].split("_")[0]
    #    tickerParams.append(temp)
    #for n in range(0,len(contractParams)):
    #    contracts.append(Contract(contractParams[n],tickerParams[n]))
    return contracts
