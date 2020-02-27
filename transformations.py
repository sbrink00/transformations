from matrix import *

def scale(matrix, x, y, z):
  ident(matrix)
  matrix[0][0] = x
  matrix[1][1] = y
  matrix[2][2] = z

def translate(matrix, x, y, z):
  ident(matrix)
  matrix[0][3] = x
  matrix[1][3] = y
  matrix[2][3] = z
