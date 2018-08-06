from pymath.algebra.linear.matrix import Matrix


class Vector(Matrix):
    """
    Class for representation Vector
    """
    def __init__(self, *values):
        Matrix.__init__(self, len(values), 1, list(values))

    def __mul__(self, other):
        return Vector(*(our_value*other_value for our_value, other_value in zip(self._values, other._values)))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __len__(self):
        return len(self._values)
