import sys
from matrix import *
from draw import *
from display import *
from transformations import *

edge = []
transform = []
filename = sys.argv[1]
lines = []
screen = new_screen()

def genLines():
  global lines
  f = open(filename, "r")
  lines = f.readlines()
  for i in range(len(lines)): lines[i] = lines[i][:-1]
  f.close()

def executeCommands():
  global lines, edge, transforms
  x = 0
  while x < len(lines):
    if lines[x] == "line":
      p = [int(x) for x in lines[x + 1].split(" ")]
      add_edge(edge, p[0], p[1], p[2], p[3], p[4], p[5])
      x += 1
    elif lines[x] == "ident":
      ident(matrix)
    elif lines[x] == "scale":
      f = [int(x) for x in lines[x + 1].split(" ")]
      scale = []
      scale(scale, f[0], f[1], f[2])
      transform_mult(scale, transform)
      x += 1
    elif lines[x] == "move":
      f = [int(x) for x in lines[x + 1].split(" ")]
      move = []
      translate(move, f[0], f[1], f[2])
      transform_mult(move, transform)
      x += 1
    elif lines[x] == "apply":
      matrix_mult(transform, edge)
    elif lines[x] == "display":
      screen = new_screen()
      draw_lines(edge, screen, DEFAULT_COLOR)
      display(screen)
    elif lines[x] == "save":
      screen = new_screen()
      draw_lines(edge, screen, DEFAULT_COLOR)
      save_extension(screen, lines[x + 1])
      x += 1
    x += 1

genLines()
executeCommands()
