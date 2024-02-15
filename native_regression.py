import matrix as m
import sys
inp_fileTwo= open(sys.argv[1], encoding="utf-8")
T=str(inp_fileTwo)
Matrix=m.loadtxt(T)
inp_fileTwo.close()
#denna ska ta position [alla][1] för y vice versa med x
#installera numpy först
numpy.transpose()
X=0
Y=0

#innan detta måste vi definera x och y utifrån matrisen vi får från loadtxt vilket står vad somm är x och y i instruktionerna 
Xp  = m.powers(X,0,1)
Yp  = m.powers(Y,1,1)
Xpt = m.transpose(Xp)

[[b],[m]] = m.matmul(m.invert(m.matmul(Xpt,Xp)),m.matmul(Xpt,Yp))