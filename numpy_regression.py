from numpy import *
import sys
import matplotlib.pyplot as plt

inp_fileTwo= sys.argv[1]
T=(inp_fileTwo)
data = loadtxt(T)

def powers(numbers, start, end):
    matrix = []  
    for num in numbers:
        row = [num ** i for i in range(start, end + 1)] # i rangen är både start och end numret inkluderat
        matrix.append(row) #delar upp matrixen i de rader som blir, hur delar man upp i raderna i resultatet? 
        matris = array(matrix)
    return matris

def poly(a,x):
    y = 0 
    for h,j in enumerate(a):
        y = y + j * x**h
    return y 

n = int(sys.argv[2])

X=data[:,0]
Y=data[:,1] 
Xp  = powers(X,0,n)
Yp  = powers(Y,1,1)
Xpt = Xp.transpose()
a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
a = a[:,0]

ma = max(X) # bestäm största värdet i matris
mi = min(X) # minsta 
spc = int(ma - mi / 0.2) # space mellan punkter i graf

Y2 = []
X2 = linspace(mi,ma,spc).tolist()
for x in X2: 
    Y2.append(poly(a,x))

plt.plot(X,Y,'ro')
plt.plot(X2,Y2)
plt.show()