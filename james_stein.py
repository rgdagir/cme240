import numpy as np


""" 
This program uses the James-Stein estimator
to predict stock prices given some assumptions.
Author: Felipe Meneses
"""

"""
Gets the sum of squared errors in the prices list.
args: prices (list of prices in the stock portfilio),
market (price of the market)
"""
def getS(prices, market):
    s = 0
    for price in prices:
        s += (price - market)**2
    return s


"""
Returns the variance of the prior distribution of beta.
args: prices (list of prices in the stock portfolio)
return: (1 / (a + sigma)) (variance of prior)
"""
def getA(prices, market):
    aS = getS(prices, market) / (len(prices) - 3)
    a = aS - getSigma(prices)
    return a



"""
Returns the variance of a normal distribution, given
a list of its values.
"""
def getSigma(prices):
    mean = np.mean(prices)
    sigma = 0
    for price in prices:
        sigma += (price - mean) ** 2
    return sigma / len(prices)

"""
Returns the beta of a stock.
args: prices (list of returns in portfolio given time), 
market (observed return of market given time), 
r (observed return of stock given time)
"""
def getBeta(r, prices, market):
    sigma = getSigma(prices)
    vBeta = getA(prices, market)
    beta = r * (vBeta / (sigma + market*vBeta)) + sigma / (sigma + market * vBeta)
    return beta

"""
Returns the predicted returns given previous returns.
args: prices (list of returns in portfolio given time), 
market (observed return of market given time), 
r (observed return of stock given time t)
"""
def getReturn(r, prices, market1, market2):
    return market2 * getBeta(r, prices, market1)

"""
Returns squared error of the prediction.
args: rs (return of stock after a time 2t), 
prices (list of returns in portfolio given time), 
market1 (observed return of market given time t),
market2 (same, but 2t), 
r (observed return of stock given time t)
"""
def getSquaredError(rs, r, prices, market1, market2):
    return (rs - getReturn(r, prices, market1, market2))**2

