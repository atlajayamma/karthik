import pandas as p
import matplotlib.pyplot as m
d=p.read_csv('D:\\Dataset\\titanic.csv')
c=d["class"].value_counts()
co=['g','r','k']
m.bar(c.index,c.values, color=co,width=0.5)
m.xticks([0,1,2],['1st class','2nd class','3rd class'])
m.xlabel("classes")
m.ylabel("no of passengers")
m.title("no of passengers travelled in specific classes")
m.show()

 