from VectorsAndMatrices import *
from decimal import *
from fractions import Fraction

class Elimination:
    
    def eliminate(self, baseMatrix):
        """
        Goes diagonally down the matrix, stopping at each diagonal entry (with an entry underneath it) and making it a pivot 
        and all the entries directly below are used as multipliers. Elimination is done on each entry under the diagonal as the diagonal
        progresses to the right, until there are no more entries under each diagonal
        """
        eliminationMatrices = []
        for rowNum in range(baseMatrix.num_of_rows):
            for multiplierIndex in range(rowNum + 1, baseMatrix.num_of_rows):
                columnNum = rowNum
                pivot = baseMatrix.entries[rowNum][columnNum]
                multiplier = baseMatrix.entries[multiplierIndex][columnNum]
                eliminationRows = []
                for eliminationRowIndex in range(0, baseMatrix.num_of_rows):
                    if (eliminationRowIndex == multiplierIndex):
                        multiplierRow = (self.identityMatrix(baseMatrix.num_of_rows).entries[eliminationRowIndex])
                        multiplierRow[columnNum] = round(-multiplier/pivot, 5)
                        eliminationRows.append(multiplierRow)
                    else:
                        eliminationRows.append(self.identityMatrix(baseMatrix.num_of_rows).entries[eliminationRowIndex])
                elimMatrix = Matrix(eliminationRows)
                baseMatrix = elimMatrix.matrix_mult(baseMatrix)
                eliminationMatrices.append(elimMatrix)
                
        return eliminationMatrices
    
    def factor_matrix(self, baseMatrix):
        """
        Creates A = LU factorization, by finding the inverse of all the elimination matrices multiplied together and multiplying that by U
        """
        factorsList = []
        e_matrix = self.e_matrix(baseMatrix)
        l_matrix = self.inverse_matrix(e_matrix)
        u_matrix = e_matrix.matrix_mult(baseMatrix)
        factorsList.append(l_matrix)
        factorsList.append(u_matrix)
        return factorsList
        

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

    def e_matrix(self, baseMatrix):
        """
        Creates the E Matrix, a matrix of all the elimination matrices multiplied together. It does this by invoking
        each of the elimination matrices using the product of a previous elimination matrix multiplication.
        Returns the U matrix
        """
        eliminationMatrices = self.eliminate(baseMatrix)
        blankMatrix = self.identityMatrix(baseMatrix.num_of_rows)
        for x in range(len(eliminationMatrices) - 1, -1, -1):
            blankMatrix = eliminationMatrices[x].matrix_mult(blankMatrix)
        e_matrix = blankMatrix
        return e_matrix

    def solutionAugment(self, baseMatrix, solution):
        """
        Allows the solution to match the elimination steps done on the matrix in order to preserve equality. It does
        this by multiplying each of the elimination matrices with the parameter vector.
        Returns the solution vector having been multiplied by elimination matrices
        """
        eliminationMatrices = self.eliminate(baseMatrix)
        for x in range(0, len(eliminationMatrices)):
            solution = eliminationMatrices[x].vector_mult(solution)
        return solution

    def solveMatrix(self, baseMatrix, b_vector):
        """
        Uses the U matrix and solution vector to solve for vector whose product with the matrix is the solution vector.
        It loops through each entry of the eliminated matrix, multiplying their value with a corresponding c value 
        and than subtracting it from the other side. Than it divides the c value by the entry to isolate the solution
        Returns the vector whose product with baseMatrix produces the solution vector
        """

        eliminated_matrix = self.e_matrix(baseMatrix).matrix_mult(baseMatrix) #U matrix
        c_vector = self.solutionAugment(baseMatrix, b_vector)
        solutionSize = len(c_vector.components)
        c_vector.printVec()
        solutionList = [None] * solutionSize
        for variableRow in range(solutionSize - 1, -1, -1):
            for solutionNum in range(len(solutionList) - 1, 0, -1):
                if solutionList[solutionNum] != None:
                    tempValue = solutionList[solutionNum] * \
                        eliminated_matrix.entries[variableRow][solutionNum]
                    c_vector.components[variableRow] = c_vector.components[variableRow] - tempValue
            solutionList[variableRow] = round( \
                c_vector.components[variableRow] / eliminated_matrix.entries[variableRow][variableRow] , 2)
            
        result = Vector(solutionList)
        if self.checkSolution(baseMatrix, b_vector, result):
            print("Matrix result was checked and proven correct")
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
            tempList[x] = self.solveMatrix(baseMatrix, 
                                           self.identityMatrix(baseMatrix.num_of_columns).columnVecs[x]).components
        return Matrix(tempList).switchDimensions()

base = Matrix([[2, 1, 0], [1, 2, 1], [0, 1, 2]])
vec1 = Vector([4, 8, 9])
eliminate = Elimination()
eliminate.solveMatrix(base, Vector([4, 8, 9])).printVec()



