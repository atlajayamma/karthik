import pandas as p
df=p.read_csv(r"C:\\Users\\PALLAVI ATLA\\OneDrive\\Documents\\nan.csv")
print("\n before droping:\n")
df.info()
df=df.dropna(axis=0)
print("\n\n after droping:\n")
df.info()