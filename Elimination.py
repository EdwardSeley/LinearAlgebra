from VectorsAndMatrices import Matrix, Vector
from decimal import *

class Elimination:
    def e21(self, baseMatrix):
        """
        Makes an elimination matrix that ignores the first row,
        subtracts the first row from the second while canceling out position 21,
        and ignores the last row.
        Returns elimination matrix e21
        """
        pivot = baseMatrix.entries[0][0]
        multiplier = baseMatrix.entries[1][0]
        if (baseMatrix.num_of_columns == 3):
            e21 = Matrix( [self.identityMatrix(baseMatrix.num_of_rows).entries[0],
                        [round(-multiplier/pivot, 5), 1, 0],
                        self.identityMatrix(3).entries[2]])
        else:
            e21 = Matrix([self.identityMatrix(baseMatrix.num_of_rows).entries[0],
                        [round(-multiplier / pivot, 5), 1]])
        return e21

    def e31(self, baseMatrix):
        """
        Makes an elimination matrix that ignores the first row,
        ignores the second row,
        and subtracts the first row from the third while canceling out position 31.
        Returns elimination matrix e31
        """
        pivot = baseMatrix.entries[0][0]
        multiplier = baseMatrix.entries[2][0]
        e31 = Matrix( [self.identityMatrix(baseMatrix.num_of_rows).entries[0],
                    self.identityMatrix(baseMatrix.num_of_rows).entries[1],
                    [round(-multiplier/pivot, 5), 0, 1]])
        return e31

    def e32(self, baseMatrix):
        """
        Makes an elimination matrix that ignores the first row,
        ignores the second row,
        and subtracts the third row from the second while canceling out position 32.
        Returns elimination matrix e32
            """
        pivot = baseMatrix.entries[1][1]
        multiplier = baseMatrix.entries[2][1]
        e32 = Matrix([self.identityMatrix(baseMatrix.num_of_rows).entries[0],
                    self.identityMatrix(baseMatrix.num_of_rows).entries[1],
                    [0, round(-multiplier/pivot, 5), 1]])
        return e32

    def identityMatrix(self, size):
        """
        Makes an identity matrix that puts a 1 wherever the column number matches the row number.
        Returns identity matrix with matching dimensions as that of base matrix
        """
        tempList = [0] * size
        rowList = [None] * size
        for x in range(0, size):
            tempList[x] = 1
            rowList[x] = list(tempList)
            tempList[x] = 0
        return Matrix(rowList)

    def u_matrix(self, baseMatrix):
        """
        Creates a U Matrix, a matrix of all the elimination matrices multiplied together. It does this by invoking
        each of the elimination matrices using the product of a previous elimination matrix multiplication.
        Returns the U matrix
        """
        m1 = self.e21(baseMatrix).matrix_mult(baseMatrix)
        if (baseMatrix.num_of_columns == 2):
            return m1
        m2 = self.e31(m1).matrix_mult(m1)
        return self.e32(m2).matrix_mult(m2)

    def solutionAugment(self, baseMatrix, solution):
        """
        Allows the solution to match the elimination steps done on the matrix in order to preserve equality. It does
        this by multiplying each of the elimination matrices with the parameter vector.
        Returns the solution vector having been multiplied by elimination matrices
        """

        vec1 = self.e21(baseMatrix).vector_mult(solution)
        if (baseMatrix.num_of_columns == 2):
            return vec1
        matrix_one = self.e21(baseMatrix).matrix_mult(baseMatrix)
        vec2 = self.e31(matrix_one).vector_mult(vec1)
        matrix_two = self.e31(matrix_one).matrix_mult(matrix_one)
        solution_vec = self.e32(matrix_two).vector_mult(vec2)
        return solution_vec

    def solveMatrix(self, baseMatrix, solution):
        """
        Uses the U matrix and solution vector to solve for vector whose product with the matrix is the solution vector.
        Returns the vector who product with baseMatrix produces the solution vector
        """

        eliminated_matrix = self.u_matrix(baseMatrix)
        eliminated_solution = self.solutionAugment(baseMatrix, solution)

        if (baseMatrix.num_of_columns == 2):
            x2 = eliminated_solution.components[1]/eliminated_matrix.entries[1][1]
            x1 = (eliminated_solution.components[0] - eliminated_matrix.entries[0][1] * x2)/eliminated_matrix.entries[0][0]
            return Vector([round(x1, 3), round(x2, 3)])
        else:
            x3 = eliminated_solution.components[2]/eliminated_matrix.entries[2][2]
            x2 = (eliminated_solution.components[1]  -  eliminated_matrix.entries[1][2] * x3)/eliminated_matrix.entries[1][1]
            x1 = (eliminated_solution.components[0] - eliminated_matrix.entries[0][1] * x2
                - eliminated_matrix.entries[0][2]* x3)/eliminated_matrix.entries[0][0]
        result = Vector([round(x1, 3), round(x2, 3), round(x3, 3)])
        if self.checkSolution(baseMatrix, solution, result):
            print("Matrix result was checked and proven true")
        else:
            print("Matrix result was checked and proven false")
        return result

    def checkSolution(self, baseMatrix, solution, result):
        """
        Checks whether the result of 'SolveMatrix' is correct by multiplying the result with the original matrix and
        seeing if it is equal to provided solution.
        Returns a boolean regarding whether the 'SolveMatrix' is successful
        """
        if baseMatrix.vector_mult(result).compare_vec(solution):
            return True
        return False

    def inverse_matrix(self, baseMatrix):
        """
        Finds the inverse by eliminating the matrix and solving for each column of the identity matrix.
        Returns inverse matrix
        """
        tempList = [0] * baseMatrix.num_of_columns
        for x in range (0, baseMatrix.num_of_columns):
            tempList[x] = self.solveMatrix(baseMatrix, self.identityMatrix(baseMatrix.num_of_columns)
                                           .columnVecs[x]).components
        return Matrix(tempList).switchDimensions()
