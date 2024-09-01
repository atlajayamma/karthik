from matplotlib import pyplot as plt
us=[12,32,16,45]
la=["asus","dell","lenovo","hp"]
e=[0,0,0,0.04]
c=["g","c","#880000","#473c88"]
plt.pie(us,labels=la,startangle=50,explode=e,colors=c,autopct='%1.2f%%')
plt.show()

