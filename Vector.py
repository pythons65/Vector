from utils import dist, degrees
import math


class Vector:
    def __call__(self):
        print(f"Vector [{self.__x},{self.__y}]")

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__mag = dist(0, 0, self.__x, self.__y)
        self.__direction = math.atan(self.__y / self.__x)

    def __len__(self):
        return dist(0, 0, self.__x, self.__y)

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
            v1 = Vector(x, y)
            return v1
        raise ValueError
    def __sub__(self, other):
        if isinstance(other, Vector):
            x = self.__x - other.co_ordinate()[0]
            y = self.__y - other.co_ordinate()[1]
            v1 = Vector(x, y)
            return v1
        raise ValueError
    def co_ordinate(self):
        return (self.__x, self.__y)
