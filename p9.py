import pandas as pd
from functools import reduce
data={'numbers':[1,2,3,4,],'letters':['a','b','c','d']}
df=pd.DataFrame(data)
sq=df['numbers'].map(lambda x:x**2)
ev=list(filter(lambda x:x%2==0,df['numbers']))
po=reduce(lambda x,y:x*y,df['numbers'])
print("data frames",df)
print("map for squaring:",sq)
print("reduce for product:",po)
