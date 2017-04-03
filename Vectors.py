class Vector:
    def __init__(self, data):
        if type(data) != list:
            raise ValueError("parameter must be a list")
        self.components = data
        self.length = len(data)
    def __len__(self):
        return self.length
    def print(self):
        print(self.components)
    def __add__(self, other):
        return 7
    def __sub__(self, other):
        return 7
    def __mul__(self, other):
        return 7

vec1 = Vector([5, 6, 9])


