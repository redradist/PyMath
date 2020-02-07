class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__ne__(other)


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __hash__(self):
        return hash(self.x) ^ hash(self.y) ^ hash(self.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not self.__ne__(other)


class Point:
    def __init__(self, *coords):
        self.coords = coords

    def __hash__(self):
        hash_code = 0
        for coord in self.coords:
            hash_code ^= hash(coord)
        return hash_code

    def __eq__(self, other):
        return len(self.coords) == len(other.coords) and \
               (all(left == right for left, right in zip(self.coords, other.coords)) or
                all(left == right for left, right in zip(self.coords, reversed(other.coords))))

    def __ne__(self, other):
        return not self.__ne__(other)