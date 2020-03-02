from draw import *
from transformations import *
from display import *

t = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
t1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
m = new_matrix()
c = [0, 255, 0]
screen = new_screen()
matrix = []
s = 100
add_square(matrix, (XRES - s) / 2, (YRES - s) / 2, (XRES + s) / 2, (YRES + s) / 2)
draw_lines(matrix, screen, c)
save_extension(screen, "1.png")
#scale then translate = translate * scale then scale * edge
#first then second = second * first then first * edge
