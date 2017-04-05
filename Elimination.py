from VectorsAndMatrices import Matrix, Vector


def e21(baseMatrix):
    pivot = baseMatrix.entries[0][0]
    multiplier = baseMatrix.entries[1][0]
    e21 = Matrix( [identityMatrix(baseMatrix.num_of_rows).entries[0], [-multiplier/pivot, 1, 0], identityMatrix(3).entries[2]])
    return e21

def e31(baseMatrix):
    pivot = baseMatrix.entries[0][0]
    multiplier = baseMatrix.entries[2][0]
    print("multiplier/pivot: " + str(multiplier/pivot))
    e31 = Matrix( [identityMatrix(baseMatrix.num_of_rows).entries[0], identityMatrix(baseMatrix.num_of_rows).entries[1],
                   [-multiplier/pivot, 0, 1]])
    return e31

def e32(baseMatrix):
    pivot = baseMatrix.entries[1][1]
    multiplier = baseMatrix.entries[2][1]
    print("multiplier/pivot: " + str(multiplier/pivot))
    e32 = Matrix( [identityMatrix(baseMatrix.num_of_rows).entries[0], identityMatrix(baseMatrix.num_of_rows).entries[1],
                   [0, -multiplier/pivot, 1]])
    return e32

def identityMatrix(size):
    return Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

m1 = Matrix([[2, 4, -2], [4, 9,-3], [-2, -3, 7]])
m1.print()
m1 = e21(m1).matrix_mult(m1)
m1 = e31(m1).matrix_mult(m1)
e32(m1).print()
e32(m1).matrix_mult(m1).print()