from pymath.algebra.linear.matrix import Matrix


class Vector(Matrix):
    """
    Class for representation Normal Vector (Column Vector)
    """
    def __init__(self, *values):
        Matrix.__init__(self, len(values), 1, list(values))

    def __mul__(self, other):
        if isinstance(other, Vector):
            if other._num_cols == 1:
                return Vector(*(our_value * other_value for our_value, other_value in zip(self._values, other._values)))
            else:
                return sum(our_value*other_value for our_value, other_value in zip(self._values, other._values))
        elif isinstance(other, Matrix):
            return Matrix.__mul__(self, other)

    def __rmul__(self, other):
        return other.__mul__(self)

    def __len__(self):
        return len(self._values)


class VectorT(Vector):
    """
    Class for representation Transpose Vector (Row Vector)
    """
    def __init__(self, *values):
        Matrix.__init__(self, 1, len(values), list(values))

    def __mul__(self, other):
        if isinstance(other, Vector):
            if other._num_rows == 1:
                return Vector(*(our_value * other_value for our_value, other_value in zip(self._values, other._values)))
            else:
                return sum(our_value*other_value for our_value, other_value in zip(self._values, other._values))
        elif isinstance(other, Matrix):
            return Matrix.__mul__(self, other)

# Aliases
CVector = Vector
ColVector = Vector
RVector = VectorT
RowVector = VectorT