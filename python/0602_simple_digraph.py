#! /usr/bin/python

class Vertex:
  '''
  This class represents a single vertex of a graph. A vertex has the following properties:
  outVertices, list: A collection of vertices connected to this vertex which are sinks
  inVertices, list: A collection of vertices connected to this vertex which are sources.
  '''
  def __init__ (self):
    self.inVertices = []
    self.outVertices = []

  def connectTo (self, vertex, isSource):
    '''
    This method connects this vertex to another vertex. isSource determines if this vertex is a source or sink.
    '''
    if isSource:
      self.outVertices.append(vertex)
      vertex.inVertices.append(self)
    else:
      self.inVertices.append(vertex)
      vertex.outVertices.append(self)

class Edge:
  '''
  An edge represents a directed edge; a connection between two vertices that starts at a source and ends at a destination. The edge is a list that holds its source at index 0 and destination at index 1.
  '''
  def __init__(self):
    self.source = None
    self.destination = None
    self.sourceId = 0
    self.destId = 1

  def representation(self):
    rep = []
    rep[0] = self.source
    rep[1] = self.destination
    return rep

  def addSource(self, vertex):
    self.source = vertex

  def addDestination(self, vertex):
    self.destination = vertex
