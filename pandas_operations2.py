
import pandas as pd
import numpy as np
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi',np.nan]})
print(df)
#Get column and index names:
print(df.columns)
print(df.index)

#sort dataframes
print(df.sort_values('col2'))

# Find Null Values or Check for Null Values
print(df.isnull())

## Drop rows with NaN Values
print(df.dropna())
print(df.drop('col1',axis=1))

#FILL THE NAN VALUES
print(df.fillna('Fill all'))

#pivot table
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)

print(df)
print(df.pivot_table(values='D',index=['A','B'],columns='C'))
