import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('D:\\Dataset\\titanic.csv')
print(data)
a_s=data[data['survived']==1]['age']
an_s=data[data['survived']==0]['age']
plt.hist(a_s,color='orange',alpha=0.5,label="survived")
plt.hist(an_s,color='pink',alpha=1,label="not survived")
plt.xlabel('age')
plt.ylabel('frequency')
plt.title('age distribution of survived and not survived pasengers')
plt.legend()
plt.show()