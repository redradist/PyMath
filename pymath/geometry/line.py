from abc import ABC

from pymath.geometry.point import Point2D, Point3D


class _Line(ABC):
    def __hash__(self):
        return hash(self.start_point) ^ hash(self.end_point)

    def __eq__(self, other):
        return self.start_point == other.start_point and self.end_point == other.end_point

    def __ne__(self, other):
        return not self.__eq__(other)


class Line2D(_Line):
    def __init__(self, start_point: Point2D, end_point: Point2D):
        self.start_point = start_point
        self.end_point = end_point


class Line3D(_Line):
    def __init__(self, start_point: Point3D, end_point: Point3D):
        self.start_point = start_point
        self.end_point = end_point
