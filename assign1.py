import json
import requests
import pprint 

BASE_ADDRESS = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey=G9V1BXZ85WN0VSTT&outputsize=compact&datatype=json"

def main():
    symbols = ["AAPL", "MFST"]
    data = {}
    for symbol in symbols:  
        hit_addr = BASE_ADDRESS + "&symbol=" + symbol
        req = requests.get(hit_addr)
        highs = {}
        assert (req.status_code == 200)    
        json_req = req.json()
        for date in json_req["Time Series (Daily)"]:
            highs[date] = float(json_req["Time Series (Daily)"][date]["2. high"])
        data[symbol] = highs
    print(data)
        
if __name__ == "__main__":
    main()