import sys


def transpose(M):
    new = []
    if M == []:
        return []
    else:
        for j in range(len(M[0])):
            rad = []
            for i in range(len(M)):
                rad.append(M[i][j])
            new.append(rad)
        return(new)



def powers(numbers, start, end):
    matrix = []  
    for num in numbers:
        row = [num ** i for i in range(start, end + 1)] # i rangen är både start och end numret inkluderat
        matrix.append(row) #delar upp matrixen i de rader som blir, hur delar man upp i raderna i resultatet?
    return matrix

#r = powers([2, 3, 4, 5, 6], 0, 6)

#print(r)

#for row in r:
#    print(row)

def matmul(A, B):
    if A == [] and B == []:
        return []
#bestäma formen på matrisenrna
    else:
        rows_A = len(A)
        cols_A = len(A[0])
        rows_B = len(B)
        cols_B = len(B[0])
        result = [[0 for row in range(cols_B)] for col in range(rows_A)] # Ställ in resultatmatrisen på nollor.
        for s in range(rows_A): #gå igenom A:s rader
            for j in range(cols_B): # Gå igenom B:s kolonner
               for k in range(cols_A): # gå igenom B:s rader
                    result[s][j] += A[s][k] * B[k][j]
        return result


#h = [[1, 1],[2, 4]]

f = [[1, 2], [3,4]] 

#g = [[3, 2 , 1],[2, 3, 4]]
#d = [[5, 2],[3, 4],[1, 2]]
j = []
k = []
#print(matmul(j,k))


def invert(A):
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0] # skapa determinant med formel
    inverted = [[A[1][1]/det, -A[0][1]/det], [-A[1][0]/det, A[0][0]/det]] # samma formel där 'det' är determinant
    return inverted

#print(f)
#print(invert(f))

def loadtxt(filename):
    matrix = []   
    with open(filename, 'r') as file:       
        for line in file:           
            numbers = [float(num) for num in line.strip().split()]
            matrix.append(numbers)
    return matrix


#result = loadtxt("chirps.txt")
#print(result)
