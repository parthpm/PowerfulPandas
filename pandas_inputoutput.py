#pandas can read a variety of file types using its pd.read_ methods

import pandas as pd
df=pd.read_csv('example.csv')

print(df)

#reading a excel file
df1=pd.read_excel('Excel_Sample.xlsx',sheet_name='sheet1')



