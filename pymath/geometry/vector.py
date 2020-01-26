from math import sqrt

from pymath.geometry.point import Point2D, Point3D


class Vector2D:
    def __init__(self, *values, start_point: Point2D = None, end_point: Point2D = None):
        if len(values) > 0:
            if start_point is not None or end_point is not None:
                raise ValueError(f'values and named points (start_point, end_point) could not be set at the same time !!')
            if len(values) != 2:
                raise ValueError(f'values should have only 2 value (dx and dy) !!')

            self.dx = values[0]
            self.dy = values[1]
        else:
            if start_point is None or end_point is None:
                raise ValueError(f'named points (start_point, end_point) should be set if values are not !!')

            self.dx = end_point.x - start_point.x
            self.dy = end_point.y - start_point.y

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return self.dx * other.dx + self.dy * other.dy
        else:
            raise ValueError(f'{other} should be Vector3D')

    def __rmul__(self, other):
        return other.__mul__(self)

    def __hash__(self):
        return hash(self.dx) ^ hash(self.dy)

    def __eq__(self, other):
        return self.dx == other.dx and self.dy == other.dy

    def __ne__(self, other):
        return not self.__ne__(other)

    def module(self):
        return sqrt(self.dx**2 + self.dy**2)


Point2D.__sub__ = lambda self, other: Vector2D(self.x - other.x, self.y - other.y)
Point2D.__rsub__ = lambda self, other: Vector2D(other.x - self.x, other.y - self.y)


class Vector3D:
    """
    Class for representation Vector
    """
    def __init__(self, *values, start_point: Point3D, end_point: Point3D):
        if len(values) > 0:
            if start_point is not None or end_point is not None:
                raise ValueError(f'values and named points (start_point, end_point) could not be set at the same time !!')
            if len(values) != 3:
                raise ValueError(f'values should have only 3 value (dx and dy) !!')

            self.dx = values[0]
            self.dy = values[1]
            self.dz = values[2]
        else:
            if start_point is None or end_point is None:
                raise ValueError(f'named points (start_point, end_point) should be set if values are not !!')

            self.dx = end_point.x - start_point.x
            self.dy = end_point.y - start_point.y
            self.dz = end_point.z - start_point.z

    def __mul__(self, other):
        if isinstance(other, Vector3D):
            return self.dx * other.dx + self.dy * other.dy + self.dz * other.dz
        else:
            raise ValueError(f'{other} should be Vector3D')

    def __rmul__(self, other):
        return other.__mul__(self)

    def __hash__(self):
        return hash(self.dx) ^ hash(self.dy) ^ hash(self.dz)

    def __eq__(self, other):
        return self.dx == other.dx and self.dy == other.dy and self.dz == other.dz

    def __ne__(self, other):
        return not self.__ne__(other)

    def module(self):
        return sqrt(self.dx**2 + self.dy**2 + self.dz**2)


Vector3D.__sub__ = lambda self, other: Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
Vector3D.__rsub__ = lambda self, other: Vector3D(other.x - self.x, other.y - self.y, other.z - self.z)
