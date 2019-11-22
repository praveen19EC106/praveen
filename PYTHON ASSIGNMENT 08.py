import pandas as pd
df=pd.read_csv('C:\\Users\Lenovo\Documents\ICUP Assignment Problems\ICUP Assignment Problems\Problem statement 8\per_capita_income.csv')
print(df)
print()

df1=df.sort_values("Income per Capita",ascending=False)
print(df1)
print()

df2=df.head()
print(df2)
print()

df3=df.tail()
print(df3)
print()

df4=df.median(axis=0,skipna=True)
print("The median of",df4)
print()

df5=df.mean(axis=0,skipna=True)
print("The mean of",df5)
print()

df['Income per Capita (,000)']=df['Income per Capita'].apply(lambda row:row//1000)
print(df)
print()

df5=df['Income per Capita (,000)'].mode()
print("The mode of the column Income per Capita (,000) is",df5)

