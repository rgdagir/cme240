import json
import requests
import pprint 
import james_stein
import numpy as np

def main():
    stock_data = np.load("stock_data.npy")
    t_stock_data = np.transpose(stock_data)
    (MLE_avg, MLE_var) = MLE_params(stock_data)
    beta = getBeta(r, t_stock_data, )
    
def MLE_params(matrix):
    means = []
    variances = []
    
    for vector in matrix:
        vector_mean = np.mean(vector)
        means.append(vector_mean)
        var = []
        for elem in vector:
            var.append((elem - vector_mean)**2)
        variances.append(np.mean(var))
    return (means, variances)

if __name__ == "__main__":
    main()
