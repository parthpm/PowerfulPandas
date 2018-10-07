import pandas as pd
import numpy as np
d={'A':[1,np.nan,2],'B':[np.nan,np.nan,3],'C':[4,5,6]}

df=pd.DataFrame(d)
print(df)
print(df.dropna())
print(df.dropna(axis=1))
print(df.dropna(thresh=2))
print(df)
print(df.fillna('fill here'))

print(df['A'].fillna(value=df['A'].mean()))
