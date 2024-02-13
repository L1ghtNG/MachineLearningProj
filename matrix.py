import sys


def transpose(M):
    new = []
    for j in range(len(M[0])):
        rad = []
        for i in range(len(M)):
            rad.append(M[i][j])
        new.append(rad)
    return(new)

#f = [[1, 2], [3,4]]   
#print(transpose(f))


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
# bestäma formen på matrisenrna
    rows_A = len(A)
    cols_A = len(A[0])
    #rows_B = len(B)
    cols_B = len(B[0])
# Ställ in resultatmatrisen på nollor.
    result = [[0 for row in range(cols_B)] for col in range(rows_A)]
# gå igenom A:s rader
    for s in range(rows_A):
# Gå igenom B:s kolonner
        for j in range(cols_B):
# gå igenom B:s rader
            for k in range(cols_A):
                result[s][j] += A[s][k] * B[k][j]

    return result


#h = [[1, 1],[2, 4]]

#f = [[1, 2], [3,4]] 

#g = [[3, 2 , 1],[2, 3, 4]]
#d = [[5, 2],[3, 4],[1, 2]]
#print(matmul(g,d))

def invert(A):
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0] # skapa determinant med formel
    inverted = [[A[0][0]/det , -A[0][1]/det ],  
                [-A[1][0]/det, A[1][1]/det]] # samma formel där 'det' är determinant
    return inverted

#print(invert(h))

def loadtxt(filename):
    """
    Load numbers from a file into a matrix.
    
    Arguments:
    filename : str : name of the file containing space-separated numbers
    
    Returns:
    list of lists : matrix containing the loaded numbers
    """
    # Initialize an empty list to store the matrix
    matrix = []
    
    # Open the file and read lines
    with open(filename, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Strip leading and trailing whitespace, then split the line into numbers
            numbers = [float(num) for num in line.strip().split()]
            # Append the list of numbers to the matrix
            matrix.append(numbers)
    
    return matrix

# Example usage:
result = loadtxt("chirps.txt")
print(result)
