import math


def dist(x1,y1,x2,y2):
  return math.dist((x1,y1),(x2,y2))

def dist3d(x1,y1,z1,x2,y2,z2):
  dx = (x2 - x1)**2
  dy = (y2 - y1)**2
  dz = (z2 - z1)**2

  return math.sqrt(dx + dy + dz)

def degrees(a):
  return math.degrees(a)
