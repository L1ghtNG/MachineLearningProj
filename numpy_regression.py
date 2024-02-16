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

n = int(sys.argv[2])

def main():
    pass

X=data[:,0]
Y=data[:,1] 
Xp  = powers(X,0,n)
Yp  = powers(Y,1,1)
Xpt = Xp.transpose()

a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
a = a[:,0]


def poly(a,x):
    y = 0 
    for h,j in enumerate(a):
        y = y +  j * x**h
    return y 

Y2 = poly(a,X)

# använd funktionen min och max för att hitta största och minsta värdet i listan
# sätt sedan n = differens mellan max och min / 0,2



linspace(X[0],X[-1],n).tolist()
plt.plot(X,Y,'ro')
plt.plot(X,Y2)
plt.show()