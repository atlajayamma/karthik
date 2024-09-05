import pandas as p
df=p.read_csv(r"C:\Users\PALLAVI ATLA\OneDrive\Documents\Dataset 1\Dataset\titanic.csv")
print("before filling null values:\n\n",df.isna().sum())
df=df.fillna(0)
print("\n\n after filling null values:\n\n",df.isna().sum())
