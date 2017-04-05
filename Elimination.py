from VectorsAndMatrices import Matrix, Vector


def e21(baseMatrix):
    pivot = baseMatrix.entries[0][0]
    multiplier = baseMatrix.entries[1][0]
    e21 = Matrix( [identityMatrix(baseMatrix.num_of_rows).entries[0], [-multiplier/pivot, 1, 0], identityMatrix(3).entries[2]])
    return e21

def e31(baseMatrix):
    pivot = baseMatrix.entries[0][0]
    multiplier = baseMatrix.entries[2][0]
    e31 = Matrix( [identityMatrix(baseMatrix.num_of_rows).entries[0], identityMatrix(baseMatrix.num_of_rows).entries[1],
                   [-multiplier/pivot, 0, 1]])
    return e31

def e32(baseMatrix):
    pivot = baseMatrix.entries[1][1]
    multiplier = baseMatrix.entries[2][1]
    e32 = Matrix( [identityMatrix(baseMatrix.num_of_rows).entries[0], identityMatrix(baseMatrix.num_of_rows).entries[1],
                   [0, -multiplier/pivot, 1]])
    return e32

def identityMatrix(size):

    tempList = [0] * size
    rowList = [None] * size
    for x in range(0, size):
        tempList[x] = 1
        rowList[x] = list(tempList)
        tempList[x] = 0
    return Matrix(rowList)

def u_matrix(baseMatrix):
    m1 = e21(baseMatrix).matrix_mult(baseMatrix)
    m2 = e31(m1).matrix_mult(m1)
    return e32(m2).matrix_mult(m2)

m1 = Matrix([[2, 4, -2], [4, 9,-3], [-2, -3, 7]])
m2 = u_matrix(m1)
m2.print()