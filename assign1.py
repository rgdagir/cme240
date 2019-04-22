import json
import requests
import pprint 
import james_stein as js
import numpy as np

def main():
    stock_data = np.load("stock_data.npy")
    t_stock_data = np.transpose(stock_data)
    r = np.subtract(np.asarray(t_stock_data[len(t_stock_data) - 1], dtype = float),np.asarray(t_stock_data[0], dtype = float))
    (MLE_avg, MLE_var) = MLE_params(stock_data)
    s_and_p = np.mean(MLE_avg)
    beta = js.getBeta(r, t_stock_data, s_and_p)
    
def MLE_params(matrix):
    means = []
    variances = []
    
    for vector in matrix:
        vector_mean = np.mean(vector.astype(float))
        means.append(vector_mean)
        var = []
        for elem in vector:
            var.append((float(elem) - float(vector_mean))**2)
        variances.append(np.mean(var))
    return (means, variances)

if __name__ == "__main__":
    main()
