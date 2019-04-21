import json
import time
import requests
import pprint
from numpy import asarray, savetxt

BASE_ADDRESS = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey=UCCG2CLTX6D3UJT8&outputsize=compact&datatype=json"

def main():
    symbols = ["MSFT","AAPL","AMZN","FB","BRK.B","GOOG","GOOGL","JPM","JNJ","XOM","V","BAC","PG","INTC","CSCO","VZ","T","DIS","HD","CVX","PFE","MA","UNH","BA","WFC","CMCSA","MRK","KO","PEP","C","NFLX","MCD","WMT","ORCL","ADBE","PM","ABT","UNP","AVGO","PYPL","MMM","IBM","HON","CRM","ABBV","ACN","NVDA","MDT","NKE","UTX"]
    stock_highs = []
    for i in range(len(symbols)):
        print(str(i)+"...")
        if ((i != 0) & (i % 4 == 0)):
            time.sleep(61) # sleep for a minute because alphavantage is ass
        hit_addr = BASE_ADDRESS + "&symbol=" + symbols[i]
        response = requests.get(hit_addr)
        assert (response.status_code == 200)
        local_highs = []
        response = response.json()
        pprint.pprint(response)
        for date in response["Time Series (Daily)"]:
            local_highs.append(response["Time Series (Daily)"][date]["2. high"])
        stock_highs.append(local_highs)
    print(stock_highs)
    savetxt("stock_data.csv", asarray(stock_highs), delimiter=",")

if __name__ == "__main__":
    main()
