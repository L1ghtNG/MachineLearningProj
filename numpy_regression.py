from numpy import *
import sys

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
#r = powers([2, 3, 4, 5, 6], 0, 6)

#print(r)
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
    for y in range[:x]:
         

plt.plot(X,Y,'ro')
plt.plot(X,Y2)
plt.show()