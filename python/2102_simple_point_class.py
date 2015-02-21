#! /usr/bin/python

import sys
import math

class Coordinate():
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return "<" + str(self.x) + "," + str(self.y) + ">"

  def distance(self, other):
    return math.sqrt(math.pow(self.x - other.x, 2.0) + math.pow(self.y - other.y, 2.0))


x_coordinate = int(sys.argv[1])
y_coordinate = int(sys.argv[2])
x2_coordinate = int(sys.argv[3])
y2_coordinate = int(sys.argv[4])

point = Coordinate(x_coordinate, y_coordinate)
point_two = Coordinate(x2_coordinate, y2_coordinate)
print point.distance(point_two)
