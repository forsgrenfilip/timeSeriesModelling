# -*- coding: utf-8 -*-
def MDEWMA(logReturns,lamb=0.96,covMatrix=0):
    '''
    input: logReturns for N number of stocks in time t-1,
           lamda=0.96 if nothing else specified
    altinput: covariance matrix for previous period
    output: NxN-covariance matrix for stocks in time t-1
    '''
    import numpy as np
    try:
        if covMatrix.any() != 0:
            covMatrix = (1-lamb) * np.matmul(logReturns.T, logReturns) + lamb*covMatrix
        else:
            covMatrix = (1-lamb)/(lamb*(1-lamb)) * lamb*np.matmul(logReturns.T, logReturns)
    except:
        if covMatrix != 0:
            covMatrix = (1-lamb) * np.matmul(logReturns.T, logReturns) * lamb*covMatrix
        else:
            covMatrix = (1-lamb)/(lamb*(1-lamb)) * lamb*np.matmul(logReturns.T, logReturns) 
    return covMatrix