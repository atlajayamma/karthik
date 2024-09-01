import numpy as n
import pandas as p
d={"day":[1,2,3,4,5,6,7,8,9,10],"steps":[4335,9552,7732,4584,5335,7552,8332,6504,8965,7689]}
dp=p.DataFrame(d)
dp["+1000 steps"]=dp["steps"]+1000
fi=dp[dp["+1000 steps"]>7000]["day"]
print("data frames:\n",dp)
print("\n days on which steps were>7000:\n",fi)
