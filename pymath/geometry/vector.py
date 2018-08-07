class Vector:
    """
    Class for representation Vector
    """
    def __init__(self, *values):
        self._values = list(values)

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self._values) != len(other._values):
                raise ValueError(f'{self} and {other} should be the same size [{len(self)} != {len(other)}]')
            return Vector(*(our_value * other_value for our_value, other_value in zip(self._values, other._values)))
        else:
            raise ValueError(f'{other} should be Vector')

    def __rmul__(self, other):
        return other.__mul__(self)

    def __eq__(self, other):
        return self._values == other._values

    def __ne__(self, other):
        return self.__eq__(other)

    def __len__(self):
        return len(self._values)
