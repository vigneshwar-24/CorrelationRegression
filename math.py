import math
import numpy as np
import matplotlib.pyplot as plt
x = [25,28,35,32,31,36,29,38,34,32]
y = [43,46,49,41,36,32,31,30,33,39]

sx=sy=sxy=sx2=sy2=0
for i in range(0,10):
    sx +=x[i]
    sy +=y[i]
    sxy+=x[i]*y[i]
    sx2+=x[i]**2
    sy2+=y[i]**2
    
n=10
r = (n*sxy-sx*sy)/(math.sqrt(n*sx2-sx*2)*math.sqrt(n*sy2-sy*2))
print("The Correlation Coefficient is %.3f"%r)
byx=(n*sxy-sx*sy)/(n*sx2-sx**2)
xmean=sx/n
ymean=sy/n
print("the reg line Y on x : Y=%0.3f %0.3f(X-%0.3f)"%(ymean,byx,xmean))
plt.scatter(x,y)
def Reg(x):
    return ymean+byx*(x-xmean)
x=np.linspace(20,40,51)
y1=Reg(x)
plt.plot(x,y1,'r')
plt.xlabel("x-data")
plt.ylabel("y-label")
plt.legend(['REGRESSION LINE', 'DATA POINTS'])
plt.show()
