# Write program to check upper triangular matrix
import array
# Function to check lower triangular matrix

def cLowerTriangular(mat, c):
    for i in range(len(mat)):
        for j in range((i+1), c):
            if mat[i][j] != 0:
                return False
            
    return True

# Function to check uppper triangular matrix 


def cUpperTriangular(mat):
    for i in range(1, len(mat)):
        for j in range(i):
            if mat[i][j] != 0:
                return False
    return True

mat = []
decision = 0
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

for i in range(r):
    row = []
    for j in range(c):
        element = int(input("Enter elements of matrix: "))
        row.append(element)
    mat.append(row)

if r==c:              
    if cUpperTriangular(mat):
        print ("Above matrix is upper triangular matrix")
    else:
        print ("Above matrix is not upper triangular matrix")

    if cLowerTriangular(mat, c):
        print ("Above matrix is lower triangular matrix")
    else:
        print ("Above matrix is not lower triangular matrix")
else:
    print("Please enter row and columns equal i.e. n*n formate\nTry again!")






