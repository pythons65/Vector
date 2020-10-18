from utils import dist, degrees, dist3d
import math


class Vector:
    def __call__(self):
        print(f"Vector [{self.__x},{self.__y},{self.__z}]")

    def __init__(self, x, y, z=0):
        self.__x = x
        self.__y = y
        self.__z = z
        self.__mag = dist3d(0, 0, 0, self.__x, self.__y, self.__z)
        self.__direction = math.atan(self.__y / self.__x)

    def __len__(self):
        return dist3d(0, 0, 0, self.__x, self.__y, self.__z)

    def __xor__(self, angleType):
        angle = math.atan(self.__y / self.__x)
        if angleType == "R":
            return angle
        elif angleType == "D":
            return degrees(angle)

    def __add__(self, other):
        if isinstance(other, Vector):
            x = self.__x + other.co_ordinate()[0]
            y = self.__y + other.co_ordinate()[1]
            z = self.__z + other.co_ordinate()[2]
            v1 = Vector(x, y, z)
            return v1
        raise ValueError

    def __sub__(self, other):
        if isinstance(other, Vector):
            x = self.__x - other.co_ordinate()[0]
            y = self.__y - other.co_ordinate()[1]
            z = self.__z - other.co_ordinate()[2]
            v1 = Vector(x, y, z)
            return v1
        raise ValueError

    def co_ordinate(self):
        return (self.__x, self.__y, self.__z)
