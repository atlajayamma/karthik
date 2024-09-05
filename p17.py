import pandas as p
df=p.read_csv(r"C:\Users\PALLAVI ATLA\OneDrive\Documents\Dataset 1\Dataset\titanic.csv")
print("before replacing:\n\n",df['age'].head(7))
print("\n median of age column:",df['age'].mean())
dp=df['age'].fillna(df['age'].median())
print("\n after replacing with median:\n\n",dp.head(7))
