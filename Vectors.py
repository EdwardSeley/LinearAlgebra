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
                raise ValueError("Components must be integers or decimals")
        self.components = data
        self.dimension = len(data)

    def __len__(self):
        """
        Returns the number of components in the vector.
        """
        return self.dimension

    def print(self):
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
            raise ValueError("Vectors must have the same length")
        for x in range(0, len(self)):
            sum = self.components[x] * other.components[x]
        return Vector(sum)
    def length(self):
        """
        Takes the square root of the dotProduct of the vector with itself.
        Returns the length/magnitude of the vector
        """
        return math.sqrt(self.dotProduct(self))
    def components(self):
        """
        Returns list form of the vector
        """
        return self.components

