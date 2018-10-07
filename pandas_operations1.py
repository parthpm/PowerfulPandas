import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df)

#Info on Unique Values
print(df['col2'].unique())
print(df['col2'].nunique())
print(df['col2'].value_counts())

#conditional selection
print(df[(df['col1']>2) & (df['col2']==444)] )

#applying functions
print(df['col1'].sum())

def timestwo(x):
    return 2*x

print(df['col1'].apply(timestwo))
print(df['col2'].apply(lambda x:x*2))


print(df['col3'].apply(len))

#Permanently Removing a Column

print(df.drop('col1',axis=1))
#or del def['col1]

#Correlation data
print(df.corr())

