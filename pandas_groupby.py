import pandas as pd
# Create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
df=pd.DataFrame(data)
print(df)

bycompany=df.groupby('Company')
print(bycompany)
print(bycompany.mean())

print(df.groupby('Company').sum())
print(bycompany.min())
print(bycompany.count())

print(bycompany.describe())
print(bycompany.describe().transpose()['FB'])