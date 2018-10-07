# DataFrames are the workhorse of pandas and are directly inspired by the
# R programming language. We can think of a DataFrame
# as a bunch of Series objects put together to share the same index.

import pandas as pd
import numpy as np
from numpy.random import randn
np.random.seed(101)  #to ontain same random nos as of instructor

df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
print(df)
print(df['W'])
print(type(df['W']))

# Pass a list of column names
print(df[['W','X']])

#Creating a new column:
df['new'] = df['W'] + df['Y']
print(df)
df.drop('new',axis=1,inplace=True)
df.drop('E',inplace=False)#inplace=True for permananet
print(df)
print(df.shape)
print(df.dropna())

#selecting rows
print(df.loc['A'])
print(df.iloc[0])

#selecting subsets of cols and rows
print(df.loc['A']['X'])
print(df.loc[['A','C'],['X','Y']])
print(df.iloc[:,:-1].values)
print(df.iloc[:,:-1])
print(type(df.iloc[:,:-1].values))
print(type(df.iloc[:,:-1]))

