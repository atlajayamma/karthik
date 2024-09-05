import pandas as p
df=p.read_csv(r"C:\Users\PALLAVI ATLA\OneDrive\Documents\Dataset 1\Dataset\titanic.csv")
print("before replacing:\n\n",df['age'].head(7))
print("\n mode of age column:",df['age'].mode())
dp=df['age'].fillna(df['age'].mode())
print("\n after replacing with mode:\n\n",dp.head(7))
