class Vector:
    """
    Class for representation Vector
    """
    def __init__(self, *values):
        self._values = list(values)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(*(our_value * other_value for our_value, other_value in zip(self._values, other._values)))
        else:
            raise ValueError(f'{other} should be Vector')

    def __rmul__(self, other):
        return other.__mul__(self)

    def __len__(self):
        return len(self._values)
