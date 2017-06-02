import math
"""
This class makes objects out of vectors and allows them to perform simple operations
"""


class Vector:

    def __init__(self, data):
        """
        Takes a list of integers and stores them in object.
        If the received parameter isn't a list comprising of integers or decimals, an error is raised.
        """
        if type(data) != list:
            raise ValueError("Parameter must be a list")
        for x in range(len(data)):
            if type(data[x]) != int and type(data[x]) != float:
                raise ValueError("Components must be integers or decimals. Item "
                                 + str(data[x]) + " of component number " + str(x) + " is type " + str(type(data[x])))
        self.components = data
        self.size = len(data)

    def __len__(self):
        """
        Returns the number of components in the vector.
        """
        return self.size

    def printVec(self):
        """
        Prints the components of the vector. Returns nothing.
        """
        print(self.components)

    def __add__(self, other):
        """
        Iterates through ethe respective components of both vectors and adds them together and the stores the result
        in a list.
        Returns the two vectors added together if they are of the same length. Otherwise an error is raised.
        """
        if len(self) != len(other):
            raise ValueError("Vectors must have the same length")
        addedComponents = []
        for x in range(0, len(self)):
            addedComponents.append(self.components[x] + other.components[x])
        return Vector(addedComponents)

    def __sub__(self, other):
        """
        Returns the first vector added to a negative second vector, resulting in subtraction.
        """
        return self + other.scalarMult(-1)

    def scalarMult(self, scalar):
        """
        Iterates through each component of the vector and multiplies it by the scalar and stores the result in a list
        Returns the scaled version of the vector.
        """
        if type(scalar) != int and type(scalar) != float:
            raise ValueError("Scalar must be an integer or decimal")
        scaledComponents = []
        for x in range(0, len(self)):
            scaledComponents.append(self.components[x] * scalar)
        return Vector(scaledComponents)

    def dotProduct(self, other):
        """
        Iterates through the respective components of both vectors and multiplies them together. It then adds that
        product to an integer 'sum' variable.
        Returns the dot product of both vectors.
        """
        if len(self) != len(other):
            raise ValueError("Vectors must have the same length. Vector 1 has length: " + str(len(self)) + " and Vector two has length: " + str(len(other)))
        dot_sum = 0
        for x in range(0, len(self)):
            dot_sum = dot_sum + self.components[x] * other.components[x]
        return round(dot_sum, 4)

    def matrix_mult(self, matrix):
        """
            Checks to see that the vector dimensions match the matrix row length. It takes the dot product of each
            row of the matrix and the vector
            Returns the product of a matrix and vector.
            """
        if len(self) != matrix.rowSize:
            raise ValueError("Vector size must equal matrix row length")
        tempList = []
        for x in range(matrix.columnSize):
            tempList.append(Vector(matrix.entries[x]).dotProduct(self))
        return Vector(tempList)

    def compare_vec(self, other):
        """
        Compares the two vectors by looping through each value and comparing them. If the two vectors' components
        are all equal, it returns true. Otherwise false is returned.
        """
        if len(self) != len(other):
            raise ValueError("Vectors must be equal lengths")
        for x in range (0, len(self)):
            if self.components[x] != other.components[x]:
                return False
        return True


    def length(self):
        """
        Takes the square root of the dotProduct of the vector with itself.
        Returns the length/magnitude of the vector
        """
        return math.sqrt(self.dotProduct(self))

    def components(self):
        """
        Returns the list form of the vector
        """
        return self.components

class Matrix:

    def __init__(self, data):
        """
        Checks whether the received parameter is a list of a list. Then it checks whether or not all of the rows are
        of the same size. Lastly it makes sure the values are integers or decimals. Then it stores the list and its
        dimensions into the object.
        """
        if type(data) != list:
            raise ValueError("Parameter must be a list")
        for x in range(0, len(data)):
            if type(data[x]) != list:
                print(str(len(data)))
                raise ValueError("Parameter must be a list of integer or decimal rows. "
                                 "the item number " + str(x) + " in the list is not a list. It is of type: "
                                 + str(type(data[x])))
            if len(data[x]) != len(data[0]):
                raise ValueError("Each row of the matrix must have the same size. " + "Row 1 has size " + str(len(data[0]))
                + " and row " + str(x + 1) + " has length " + str(len(data[x])))
            for y in range(0, len(data[x])):
                if type(data[x][y]) != int and type(data[x][y]) != float:
                    raise ValueError("Parameter must be a list of a integer or decimal rows. "
                                     + "The entry in row " + str(x) + "and column " + str(y)
                                     + "is not an integer or decimal")

        columnList = [None] * len(data)
        vecList = [None] * len(data[0])

        for a in range(0, len(data[0])): #iterates through number of rows
            for b in range(0, len(data)): #iterates through number of columns
                columnList[b] = data[b][a]
            vec = Vector(columnList)
            vecList[a] = vec
            columnList = [None] * len(data)

        self.columnVecs = vecList
        self.entries = data
        self.num_of_columns = len(data[0])
        self.num_of_rows = len(data)
        
    def isSquare(self):
        """
        Checks whether or not the matrix has the same number of columns as it does rows
        Returns a boolean
        """
        if self.num_of_rows == self.num_of_columns:
            return True
        else: 
            return False

    def __add__(self, other):
        """
        Checks that the two matrices have both the same row and column size. Then it iterates through each item and
        adds the respective entries together and stores them in a 2D list.
        Returns the matrix of the added entries
        """
        if self.num_of_columns != other.columnSize:
            raise ValueError("Cannot add matrices with different numbers of columns")
        if self.num_of_rows != other.rowSize:
            raise ValueError("Cannot add matrices with different numbers of row entries")
        addition_matrix = [ [0 for a in range(0, self.num_of_columns)] for b in range(0, self.num_of_rows) ]
        for x in range(0, self.num_of_rows):
            for y in range(0, self.num_of_columns):
                addition_matrix[x][y] = self.entries[x][y] + other.entries[x][y]
        return Matrix(addition_matrix)

    def scalar_mult(self, scalar):
        """
        Checks to see that the scalar is an integer or decimal. Then it makes a temporary list and fills it with
        scaled up entries of the matrix.
        Returns scaled matrix
        """
        if type(scalar) != int and type(scalar) != float:
            raise ValueError("Scalar must be an integer or decimal")
        scaled_matrix = [[0 for a in range(0, self.num_of_columns)] for b in range(0, self.num_of_rows)]
        for x in range(0, self.num_of_rows):
            for y in range(0, self.num_of_columns):
                scaled_matrix[x][y] = self.entries[x][y] * scalar
        return Matrix(scaled_matrix)

    def vector_mult(self, vector):
        """
        Checks to see that the vector dimensions match the matrix row length. It takes the dot product of each
        row of the matrix and the vector
        Returns the product of a matrix and vector.
        """
        if len(vector) != self.num_of_columns:
            raise ValueError("Vector size must equal matrix row length")
        temp_list = []
        for x in range(0, self.num_of_rows):
            temp_list.append(Vector(self.entries[x]).dotProduct(vector))
        return Vector(temp_list)

    def matrix_mult(self, other):
        """
        Checks whether or not the number of columns in the first matrix matches the number of rows in the second matrix.
        Loops through the columns of the second matrix and stores the dot product of each column with the first matrix
        in a list. After the list is complete, it is used to create a matrix and then that matrix's dimensions are
        changed.
        """
        if self.num_of_columns != other.num_of_rows:
            raise ValueError("Row size of 2nd Matrix must equal column size of first. Matrix 1 has a column number of " + str(self.num_of_columns) + " and Matrix 2 has a row number of " + str(other.num_of_rows) )

        horizontal_matrix = [None] * other.num_of_columns
        for x in range(0, other.num_of_columns):
            horizontal_matrix[x] = self.vector_mult(other.columnVecs[x]).components

        product_matrix = Matrix(horizontal_matrix).switchDimensions()
        return product_matrix

    def switchDimensions(self):
        """
        Loops through the rows within a loop of the columns (resets rows after it moves to the next column) and finds
        the corresponding members of the same column and puts them in a list. This list of same column members are then
        made a row by creating a list of each list of same column entries. The list is then converted into a matrix.
        """
        tempList = [None] * self.num_of_rows
        rowList = [None] * self.num_of_columns

        for x in range(self.num_of_columns):
            for y in range(0, self.num_of_rows):
                tempList[y] = self.entries[y][x]
            rowList[x] = tempList;
            tempList = [None] * self.num_of_rows

        return Matrix(rowList)

    def printMatrix(self):
        """
        After printing an empty line, it iterates through each entry and prints it. Once a row is complete,
        another empty line is made.
        Returns nothing
        """
        print('\n')
        for x in range(0, self.num_of_rows):
            for y in range(0, self.num_of_columns):
                print(self.entries[x][y], end=' ')
            print('\n')

    def zero_matrix(self):
        """
        returns a same dimension matrix filled with all zeros
        """
        return Matrix(self.num_of_rows * [self.num_of_columns * [0] ])

    def compare_matrix(self, other):
        """
        retuns a boolean regarding whether or not the two matrices are equal
        """
        if self.num_of_rows != other.num_of_rows or self.num_of_columns != other.num_of_columns:
            ValueError("Matrices must have the same dimensions")
        for x in range(self.num_of_rows):
            if(not Vector(self.entries[x]).compare_vec(Vector(other.entries[x]))):
                return False
        return True


        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
            
            
            
            
            
            