import pandas as pd
import numpy as np
from numpy.random import randn
np.random.seed(101)

df=pd.DataFrame(randn(5,4),'A B C D E'.split(),'W X Y Z'.split())
print(df)
### Conditional Selection

#An important feature of pandas is conditional selection
#using bracket notation, very similar to numpy:

print(df>0,end='\n\n')
print(df[df>0])

print(df['W']>0)
print(df[df['W']>0])
print(df[df['W']>0]['X'])

print(df[df['W']>0][['Y','X']])

print(df[(df['W']>0) & (df['X']>0)])
