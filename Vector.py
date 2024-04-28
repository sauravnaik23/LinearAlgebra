from typing import List
import numpy as np
import matplotlib.pyplot as plt

class Vector:
    def __init__(self, cord: List | np.array):
        self.cord = np.array(cord)
        self.dimension = len(cord)

    def __repr__(self):
        return (str(list(self.cord)))

    def __add__(self, vec):
        if isinstance(vec, Vector):
            if self.dimension == vec.dimension:
                return Vector(self.cord + vec.cord)
            else:
                raise ValueError("Dimension of the vector must be same")
        else:
             raise TypeError("vec should be an object of class Vector")

    def __sub__(self, vec):
        if isinstance(vec, Vector):
            if self.dimension == vec.dimension:
                return Vector(self.cord - vec.cord)
            else:
                raise ValueError("Dimension of the vector must be same")
        else:
             raise TypeError("vec should be an object of class Vector")

    def __getitem__(self, item:int):
        return self.cord[item]

    def projection_on_vec(self,vec):
        if isinstance(vec, Vector):
            # ratio = (self.cord @ vec.cord)/vec.magnitude()**2
            # or
            ratio = (self.cord @ vec.cord)/(vec.cord @ vec.cord)
            projection_vector = Vector(ratio * vec.cord)
            return projection_vector, ratio
        else:
            raise TypeError("vec should be an object of class Vector")

    def magnitude(self):
        return np.linalg.norm(self.cord)

    def unit_vec(self):
        num = self.cord
        denom = self.magnitude()
        return Vector(num/denom)

    def is_perpendicular_to(self,vec):
        if isinstance(vec, Vector):
            res = self.cord @ vec.cord
            if res:
                return False
            return True

        else:
            raise TypeError("vec should be an object of class Vector")

    def plot_2D_vector(self, start = None,label = None, color = 'green'):
        if (self.dimension == 2):
            if not start:
                start = [0] * self.dimension
            if len(start) == self.dimension:
                if label:
                    plt.quiver(*start, *self.cord, scale = 10, color = color, label = label)

                else:
                    plt.quiver(*start, *self.cord, scale = 10, color = color,
                               label = f"Vector(x:{round(self.cord[0],2)} | y: {round(self.cord[1],2)})")
                plt.legend()

            else:
                raise ValueError("start should have the same dimension as the vector")
        else:
            raise ValueError("Can only plot 2D vectors")