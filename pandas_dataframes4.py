# Index Levels
import pandas as pd
import numpy as np
from numpy.random import randn
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)

df=pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
print(df)

print(df.loc['G1'])
print(df.loc['G1'].loc[1]['A'])
df.index.names = ['Group','Num']
print(df)
print(df.xs(['G1',1]))

print(df.xs(1,level='Num'))