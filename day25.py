import pandas as pd
import numpy as np

from pandas import DataFrame as f

ef1 = pd.read_csv("emp.csv")
print(ef1)

ar = []
for i in range(0,9):
    ar.append(filter(lambda x: x.isdigit(), ef1.iloc[i,-1]))
    
print(ar)

ef11 = ef1.iloc[:,:-1]
print(len(ef11))

'''ef1['ephno'] = ef11

print(ef1)

'''
