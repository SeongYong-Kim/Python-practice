import random as rd

def GenerateMatrix3():
    row1 = [rd.randrange(1, 10) for i in range(3)]
    row2 = [rd.randrange(1, 10) for i in range(3)]
    row3 = [rd.randrange(1, 10) for i in range(3)]
    matrix = [row1, row2, row3]

    return matrix

def TransposeMatrix(A):
    B = GenerateMatrix3()
    for i in range(len(A)):#column
        for j in range(len(A[0])):#row1
            B[j][i] = A[i][j]

    return B

def ProductMatrix(A,B):
    result = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(B[0])):#B row
        for j in range(len(A)):#A column
            result[j][i] = A[j][0]*B[0][i]+A[j][1]*B[1][i]+A[j][2]*B[2][i]

    return result

A = GenerateMatrix3()
B = GenerateMatrix3()
C = ProductMatrix(A,B)
C_tp = TransposeMatrix(C)

print("A = ", A)
print("B = ", B)
print("C = ", C)
print("C transpose = ", C_tp)
