from VectorsAndMatrices import Matrix, Vector


def e21(baseMatrix):
    pivot = baseMatrix.entries[0][0]
    multiplier = baseMatrix.entries[1][0]
    e21 = Matrix( [identityMatrix(baseMatrix.num_of_rows).entries[0], [-multiplier/pivot, 1, 0], identityMatrix(3).entries[2]])
    return e21

def e21(baseMatrix):
    pivot = baseMatrix.entries[0][0]
    multiplier = baseMatrix.entries[1][0]
    e21 = Matrix( [identityMatrix(baseMatrix.num_of_rows).entries[0], [-multiplier/pivot, 1, 0], identityMatrix(3).entries[2]])
    return e21

def e31(baseMatrix):
    pivot = baseMatrix.entries[0][0]
    multiplier = baseMatrix.entries[2][0]
    e31 = Matrix( [identityMatrix(baseMatrix.num_of_rows).entries[0],
                identityMatrix(baseMatrix.num_of_rows).entries[1],
                [-multiplier/pivot, 0, 1]])
    return e31

def e32(baseMatrix):
    pivot = baseMatrix.entries[1][1]
    multiplier = baseMatrix.entries[2][1]
    e32 = Matrix([identityMatrix(baseMatrix.num_of_rows).entries[0],
                   identityMatrix(baseMatrix.num_of_rows).entries[1],
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

def solutionAugment(baseMatrix, solution):
    vec1 = e21(baseMatrix).vector_mult(solution)
    matrix_one = e21(baseMatrix).matrix_mult(baseMatrix)
    vec2 = e31(matrix_one).vector_mult(vec1)
    matrix_two = e31(matrix_one).matrix_mult(matrix_one)
    solution_vec = e32(matrix_two).vector_mult(vec2)
    return solution_vec

def solveMatrix(baseMatrix, solution):
    eliminated_matrix = u_matrix(baseMatrix)
    eliminated_solution = solutionAugment(baseMatrix, solution)
    x3 = eliminated_solution.components[2]/eliminated_matrix.entries[2][2]
    x2 = (eliminated_solution.components[1]  -  eliminated_matrix.entries[1][2] * x3)/eliminated_matrix.entries[1][1]
    x1 = (eliminated_solution.components[0] - eliminated_matrix.entries[0][1] * x2
          - eliminated_matrix.entries[0][2]* x3)/eliminated_matrix.entries[0][0]
    return Vector([x1, x2 ,x3])
