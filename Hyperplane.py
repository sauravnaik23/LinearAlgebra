from typing import List
import numpy as np
import matplotlib.pyplot as plt
from Vector import Vector

class DimensionError(Exception):

  def __init__(self, message):
    self.message = message


class HyperPlane:
  '''
  Creates a n-dim hyperplane in the w1.x + w2.y+....wn.N + w0 = 0 format
  '''
  def __init__(self,
               w:List[float],
               c:float = 0.0):
    self.w = np.array(w)
    self.c = np.array(c)


  def dist_from_point(self,
                      point: List[float])->float:
    '''
    Given a point in n-dim space gives the shortest distance of the point
    from the hyperplane
    '''
    if not(len(point) == len(self.w)):
      raise DimensionError('Dimension mismatch for weight and point vector')
    num = np.dot(self.w,point) + self.c
    denom = np.linalg.norm(self.w)
    return num/denom


  def dist_from_origin(self)->float:
    '''
    Gives the shortest distance of the origin
    from the hyperplane
    '''
    # we are keeping the dimension of the origin the same as
    # the dimension of the wweight vector just for the ease of calculation
    origin = [0] * len(self.w)
    return self.dist_from_point(origin)


  def check_if_parallel(self, hyperplane):
    '''
    Checks whether the two hyperplanes are parallel
    '''
    if isinstance(hyperplane, HyperPlane):
        if len(self.w) != len(hyperplane.w):
          raise DimensionError
        ratios = self.w/hyperplane.w
        return np.all(ratios == ratios[0])
    raise ValueError("hyperplane should be an object of class Hyperplane")


  def dist_from_hyperplane(self,
                           hyperplane)->float:
    '''
    Gives the shortest distance between two hyperplanes if they are parallel
    '''
    if isinstance(hyperplane, HyperPlane):
    # first check whether the hyperplanes are parallel
        if self.check_if_parallel(hyperplane):
          # check if they lie on the same side of the origin
          # NOTE: this point could have been any point and not just origin
          points = [0] * len(self.w)
          # checking whether the ndim point lies in the same halfspace of both hyperplanes
          if self.check_halfspace(points) == hyperplane.check_halfspace(points):
            return abs(self.dist_from_origin() - hyperplane.dist_from_origin())
            # return abs(self.dist_from_point(points) - hyperplane.dist_from_point(points))
          return abs(self.dist_from_origin()) + abs(hyperplane.dist_from_origin())
          # return abs(self.dist_from_point(points)) + abs(hyperplane.dist_from_point(points))
        return "The hyperplanes are not parallel"
    raise ValueError("hyperplane should be an object of class Hyperplane")


  def check_halfspace(self,
                      point:List[float])->int:
    '''
    Checks which halfspace of the hyperplane the point belongs to
    Returns -1 for -ve and +1 for +ve halfspace
    '''
    if not(len(point) == len(self.w)):
      raise DimensionError('Dimension mismatch for weight and point vector')
    res = np.dot(self.w,point) + self.c
    # if res > 0:
    #   return 1
    # return -1
    return np.sign(res)

  def __repr__(self):
      lis = []
      for i in range(len(self.w)):
          lis.append('(' + str(round(self.w[i],2)) + ')' + 'x'+str(i + 1) + ' + ')
      lis.append(str(round(self.c,2)) + ' = 0')
      return ''.join(lis)

  def plot_2D_line(self):
    '''
    Plots 2D line
    '''
    if len(self.w)==2:
      # calculating the slope intercept form
      slope = -self.w[0]/self.w[1]
      intercept = -self.c/self.w[0]
      hplane_x = np.arange(0,11)
      hplane_y = slope*hplane_x + intercept
      plt.plot(hplane_x, hplane_y)
      # calculating the unit weight vector just
      # to scale down the length of vector
      weight_vec = Vector(self.w)
      unit_weight_vec = weight_vec.unit_vec()
      center_x = 5
      center_y = slope*center_x + intercept
      # plotting the unit weight vector
      unit_weight_vec.plot_2D_vector(start =[center_x, center_y],
                                     label = f"Vector(x:{round(weight_vec[0],2)} | y: {round(weight_vec[1],2)})")


  def plot_plane(self):
    pass

if __name__ == "__main__":

  p1 = HyperPlane([4,5],-13)
  p2 = HyperPlane([2,2.5],-18)

  print(p1.dist_from_hyperplane(p2))