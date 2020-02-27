from draw import *
from transformations import *

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2], [3, 4, 5, 6]]
scale(matrix, 3, 4, 5)
print(print_transform(matrix))

matrix1 = []
for i in range(10):
  add_point(matrix1, 0, 0, 0)

translate(matrix, 1, 1, 1)
matrix_mult(matrix, matrix1)
print(print_matrix(matrix1))
