#More Index Details
import pandas as pd
import numpy as np
from numpy.random import randn
np.random.seed(101)

df=pd.DataFrame(randn(5,4),'A B C D E'.split(),'W X Y Z'.split())
print(df)

print(df.reset_index())

df['STATES']='CA NY WY OR CO'.split()
print(df)

df.set_index('STATES',inplace=True)
print(df)