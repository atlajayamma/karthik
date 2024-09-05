import pandas as p
df=p.read_csv(r"C:\Users\PALLAVI ATLA\OneDrive\Documents\Dataset 1\Dataset\titanic.csv")
info=df.info()
print("\n\n\n is_na:\n\n",df.isna().head(7))
is_null_su=df.isna().sum()
print("\n\n\n count of all missing values:\n\n",df.isna().sum())