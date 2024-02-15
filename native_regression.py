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
Y=Y0[1]

#innan detta måste vi definera x och y utifrån matrisen vi får från loadtxt vilket står vad somm är x och y i instruktionerna 
Xp  = powers(X,0,1)
Yp  = powers(Y,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))