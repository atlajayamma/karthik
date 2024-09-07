import pandas as pd
d={
"first_name":["aryan","rohan","riya","yash","siddhant"],
"last_name":["singh","agarwal","shah","bhata","khanna"],
"type":["full_time","itern","full_time","part_time","full_time"],
"dept":["administation","technical","administation","technical","manageement"],
"yoe":[2,3,5,7,6],
"salary":[20000,5000,10000,10000,20000]
}
df=pd.DataFrame(d)
print(df)
av=df.pivot_table(index=['dept','type'],values="salary",aggfunc='mean')
print("average salary from each department:\n",av)
sm=df.pivot_table(index=['type'],values='salary',aggfunc=['sum','mean','count'])
sm_column=['total salary','mean salary','number of employees']
print("\n sum and mean of:\n",sm)
st=df.pivot_table(values='salary',index='type',aggfunc='std')
print("standard deviation:\n",st)