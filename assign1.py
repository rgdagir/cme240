import json
import requests
import pprint 

BASE_ADDRESS = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey=G9V1BXZ85WN0VSTT&outputsize=compact&datatype=json"

def main():
    symbols = ["MSFT","AAPL","AMZN","FB","BRK.B","GOOG","GOOGL","JPM","JNJ","XOM","V","BAC","PG","INTC","CSCO","VZ","T","DIS","HD","CVX","PFE","MA","UNH","BA","WFC","CMCSA","MRK","KO","PEP","C","NFLX","MCD","WMT","ORCL","ADBE","PM","ABT","UNP","AVGO","PYPL","MMM","IBM","HON","CRM","ABBV","ACN","NVDA","MDT","NKE","UTX"]
    stock_highs = []
    for symbol in symbols:  
        hit_addr = BASE_ADDRESS + "&symbol=" + symbol
        req = requests.get(hit_addr)
        assert (req.status_code == 200)    
        local_highs = []
        json_req = req.json()
        pprint.pprint(json_req)
        for date in json_req["Time Series (Daily)"]:
            local_highs.append(json_req["Time Series (Daily)"][date]["2. high"])
        stock_highs.append(local_highs)
    print(stock_highs) 
        
def calculate_MLE_probabilities(arr_of_arr):
    results = np.zeros(len(arr_of_arr[0]))
    for elem in arr_of_arr:
        results = np.add(elem, results)
    results = results/len(arr_of_arr)
    return results

if __name__ == "__main__":
    main()
