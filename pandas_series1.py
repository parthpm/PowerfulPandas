#A Series is very similar to a NumPy array
# (in fact it is built on top of the NumPy array object).
#  What differentiates the NumPy array from a Series, is that a
#  Series can have axis labels, meaning it can be indexed by a label,
#  instead of just a number location. It also doesn't need
# to hold numeric data,
#  it can hold any arbitrary Python Object.
import numpy as np
import pandas as pd

labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([11,20,30])
d = {'a':10,'b':20,'c':30}
#creating Series
#list
print(pd.Series(data=my_list))
print(pd.Series(data=my_list,index=labels))

#numpy arrays
print(pd.Series(arr,labels))
#dictionary
print(pd.Series(d))

#**A pandas Series can hold a variety of object types:**
ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan'])
print(ser1)
print(ser1['USA'])