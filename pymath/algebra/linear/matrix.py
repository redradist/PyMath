class Matrix:
    """
    Class for representation Matrix
    """
    def __init__(self, num_rows, num_cols, values):
        if num_rows == 0:
            raise ValueError(f'num_rows should not be equal zero !!')
        if num_cols == 0:
            raise ValueError(f'num_cols should not be equal zero !!')
        if len(values) != num_rows * num_cols:
            raise ValueError(f'Lenght of values should be equal {num_rows * num_cols} !!')

        self._num_rows = num_rows
        self._num_cols = num_cols
        self._values = list(values)

    def __mul__(self, other):
        if type(other) is Matrix:
            if self._num_cols != other._num_rows:
                raise ValueError(f'Cannot multiple {self} with {other}')
            result_values = []
            index = 0
            sum = 0
            index_row = 0
            index_col = 0
            el_per_row0 = len(self._values) // self._num_rows
            el_per_row1 = len(other._values) // other._num_rows
            while index_row < self._num_rows and index_col < other._num_cols:
                value0 = self._values[index_row * el_per_row0 + index]
                value1 = other._values[index * el_per_row1 + index_col]
                sum += value0 * value1
                index += 1
                if index >= self._num_cols or index >= other._num_rows:
                    assert index == self._num_cols
                    assert index == other._num_rows
                    result_values.append(sum)
                    index = 0
                    sum = 0
                    index_col += 1
                    if index_col >= other._num_cols:
                        index_row += 1
                        if index_row < self._num_rows:
                            index_col = 0
            assert index_row == self._num_rows
            assert index_col == other._num_cols
            return Matrix(self._num_rows, other._num_cols, result_values)
        else:
            raise ValueError(f'{other} has invalid type !! Should be Vector or Matrix')

    def __rmul__(self, other):
        return other.__mul__(self)

    def __eq__(self, other):
        return self._num_rows == other._num_rows and \
               self._num_cols == other._num_cols and \
               self._values == other._values

    def __ne__(self, other):
        return not self.__eq__(other)


class Identity(Matrix):
    """

    """
    def __init__(self, num_rows, num_cols):
        values = []
        Matrix.__init__(self, num_rows, num_cols, *values)
