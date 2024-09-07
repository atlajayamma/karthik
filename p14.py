import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("C:\Users\PALLAVI ATLA\OneDrive\Documents\Dataset 1\Dataset\titanic.csv")
print(data)
##Histogram
a_s=data[data['survived']==1]['age']
an_s=data[data['survived']==0]['age']
plt.hist(a_s,color='green',alpha=0.5,label="survived")
plt.hist(an_s,color='purple',alpha=1,label="not survived")
plt.xlabel('age')
plt.ylabel('frequency')
plt.title('age distribution of survived and not survived pasengers')
plt.legend()
plt.show()