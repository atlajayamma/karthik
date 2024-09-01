from matplotlib import pyplot as p
Q=["Q1","Q2","Q3","Q4"]
ssd=[200,230,350,400]
hdd=[250,240,320,250]
p.plot(Q,ssd,'^-',color='green')
p.plot(Q,hdd,'o-.b')
p.xlabel("quarters in 2022"),p.ylabel("sales units")
p.title("sdd & hdd sales in store")
p.legend(['sdd','hdd'])
p.show()
