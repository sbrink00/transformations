from display import *
from matrix import *
from draw import *
from transformations import *

screen = new_screen()
matrix = []
images = 100
add_square(matrix, 0, 200, 100, 300)
t = []
translate(t, XRES / images, 0, 0)
for i in range(images):
  print(i)
  if i != 0: matrix_mult(t, matrix)
  draw_lines(matrix, screen, DRAW_COLOR)
  save_extension(screen, "pic" + str(i) + ".png")
  clear_screen(screen)
