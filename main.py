from draw import *
from transformations import *
from display import *

transform = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
transform1 = [x for x in transform]
m = new_matrix()
c = [0, 255, 0]
screen = new_screen()
matrix = new_matrix()
s = 100
add_square(matrix, (XRES - s) / 2, (YRES - s) / 2, (XRES + s) / 2, (YRES + s) / 2)

scale(transform, .5, .5, .5)
translate(transform1, 300, 300, 0)
print(print_transform(transform1) + "\n")
matrix_mult(transform, matrix)
print(print_matrix(matrix) + "\n")
matrix_mult(transform1, matrix)
print(print_matrix(matrix) + "\n")

draw_lines(matrix, screen, c)
save_ppm_ascii(screen, 'ascii.ppm')
