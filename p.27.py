import pandas as pd
df=pd.read_csv(r"C:\Users\PALLAVI ATLA\OneDrive\\Documents\Dataset 1\\Dataset\\titanic.csv")
#Find the total number of missing values from each column.
print(df.isnull().sum())

