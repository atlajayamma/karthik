import pandas as p
df=p.read_csv(r"C:\Users\PALLAVI ATLA\OneDrive\Documents\Dataset 1\Dataset\titanic.csv")
print("before replacing:\n\n",df['age'].head(7))
print("\n mean of age column:",df['age'].mean())
dp=df['age'].fillna(df['age'].mean())
print("\n after replacing with mean:\n\n",dp.head(7))
