import pandas as pd
import numpy as np
from pandas import DataFrame as f
from pandas import Series as s

ar = np.arange(1,17).reshape(4,4)
print(ar)

#-------------------------------------

mar = np.ma.masked_array(ar, mask = ar%3== 0)

#-------------------------------------

far = f(mar)

print(far)

#-------------------------------------

sar = s(np.arange(1,17))
sar2 = np.ma.masked_array(sar, mask = sar%3 == 0)
print(sar2)
sar3 = s(sar2)

sar3.fillna(method = 'ffill', inplace = True)
print(sar3)

sar3.fillna(method = 'bfill', inplace = True)
print(sar3)


#-------------------------------------

f1 = f(ar, index = list('a b c d'.split()), columns = 'c1 c2 c3 c4'.split())
f2 = f1.reindex(list('abcde'))
f2 = f2.reindex(columns = 'c1 c2 c3 c4 c5'.split())
print(f1)
print(f2)

f3 = f2.reindex(list('abcde'), method = 'ffill')
print '========================'
print(f3)

#-------------------------------------

ar = np.arange(1,17).reshape(4,4)

far = f(ar, index = list('r1 r2 r3 r4'.split()), columns = list('c1 c2 c3 c4'.split()))

print(far)

print(far.iloc[0, 0])
x = far.iloc[0:1,0].values
ser = s(x)
print(ser)
fser = f(ser)
print(fser)


print(far.loc['c1','r1'])
x = far.loc['c1','r1']
ser = s(x)
print(ser)
fser = f(ser)
print(fser)

print(far.iloc[[-2,-1],[-2,-1]])


#--------------------------------------------------------

ar1 = np.arange(10,26).reshape(4,4)


far1 = f(ar, index = list('r1 r2 r3 r4'.split()), columns = list('c1 c2 c3 c4'.split()))
print(far)

faradd = far + far1
print(faradd)

faradd = far.add(far1, fill_value = 0)
print(faradd)

#--------------------------------------------------------

array = np.arange(1,13).reshape(3,4)
print(array)

obj = f(array)
s1 = s(obj.iloc[0,])
s2 = s(obj.iloc[:,0])
print(s1)
print(s2)

res1 = s1.subtract(s2, fill_value = 0)
res2 = s2.subtract(s1, fill_value = 0)
print(res1, res2)

