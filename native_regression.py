import matrix as m
import sys
inp_fileTwo= open(sys.argv[1], encoding="utf-8")
T=str(inp_fileTwo)
Matrix=m.loadtxt(T)
inp_fileTwo.close()