#!/usr/bin/python

import sys

class SetOfIntegers():
  '''This class represents a set of integers. The integers are stored in a list. The list contains distinct integers.
  '''
  def __init__(self):
    self.values = []

  def __str__(self):
    self.values.sort()
    return '{' + ''.join([str(e) for e in self.values]) + '}'

  def insertElement(self, element):
    if not element in self.values:
      self.values.append(element)

  def removeElement(self, element):
    try:
      return self.values.remove(element)
    except:
      raise ValueError()
