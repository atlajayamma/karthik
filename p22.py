import pandas as p
import numpy as n
df=p.read_csv(r"C:\Users\PALLAVI ATLA\OneDrive\Documents\Dataset 1\Dataset\titanic.csv")
print(df.isna().sum())
df=df.replace({n.nan:-1})
print("\n\n\n")
print(df.isna().sum())
