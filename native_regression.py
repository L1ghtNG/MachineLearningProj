from matrix import *
import sys
import matplotlib.pyplot as plt

inp_fileTwo= sys.argv[1]
T=str(inp_fileTwo)
matris=loadtxt(T)


#denna ska ta position [alla][1] för y vice versa med x
#installera numpy först

X0 = transpose(matris)
Y0 = transpose(matris)
X=X0[0]
Y=Y0[1]     # definera x och y utifrån matrisen vi får från loadtxt vilket står vad somm är x och y i instruktionerna 
Xp  = powers(X,0,1)
Yp  = powers(Y,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))

Y2 = b + m * X # får inte den att fungerna, den ska använda varje värde för X och skapa ett Y värde 
    

plt.plot(X,Y,'ro')  #sätter ut prickarna i grafen
plt.plot(X,Y2) # lägger ut linejen i grafen
plt.show()

#för att 'runna' koden ska du kopiera in 'python3 native_regression.py chirps.txt' i terminalen 