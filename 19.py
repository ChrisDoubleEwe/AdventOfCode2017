import os
import time
map = []
o_map = []
trace = []
map_width = 0
map_height = 0

total_steps = 1

def printout():
  return
  size = 8
  os.system('clear')

  s_y = y - size
  for my_y in range(s_y, s_y+size+size):
    if my_y < 0:
      print
      continue
    if my_y > map_height:
      print
      continue
    row = map[my_y]
    s_x = x -size
    row_str = ''  
    for my_x in range(s_x, s_x+size+size):
      if my_x < 0:
          row_str += ' '
          continue
      if my_x > map_width-1:
          row_str += ' '
          continue
      row_str += map[my_y][my_x]
    print row_str


  print
  print 
  print

  print "map_height = %d ; map_width = %d" % (map_height, map_width)
  print "x = %d ; y = %d" % (x, y)
  print "dir_x = %d ; dir_y = %d" % (dir_x, dir_y)


  print trace
  time.sleep(.5)

with open ("19a_data.txt", "r") as myfile:
    for line in myfile:
        l_list = list(line[:-1])
        o_list = list(line[:-1])

        map_height += 1
        map.append(l_list)
        o_map.append(o_list)
        if len(l_list) > map_width:
          map_width = len(l_list)
    map_height -= 1

# Get starting point
x = 0
y = 0
dir_y = 1
dir_x = 0

for c in map[0]:
  if c != "|":
     x+= 1
  if c == "|":
     break 

#x = 151
#y = 28
#dir_y = -1
#dir_x = 0

map[y][x] = "*"

printout()

def move():
  global x
  global y
  global dir_x
  global dir_y
  global total_steps

  total_steps += 1
  map[y][x] = o_map[y][x]
  y = y+dir_y
  x = x+dir_x
  map[y][x] = "*"
  if o_map[y][x] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    #if o_map[y][x] == 'P':
    #  print "x = %d" % x
    #  print "y = %d" % y
    #  print "dir_y = %d" % dir_y
    #  print "dir_x = %d" % dir_x
    #  exit()
    trace.append(o_map[y][x])
  printout()

# Where next?
while True:
  while o_map[y][x] != '+' and o_map[y][x] != ' ':
    if o_map[y+dir_y][x+dir_x] == ' ':
      #print "END"
      print ''.join(trace)
      print total_steps
      exit()
    else:
      move()

  # At a junction, where next?
  # If we were travelling up or down, look left and right:
  new_dir_y = 99
  new_dir_x = 99
  if dir_y != 0 and x > 0:
    if o_map[y][x-1] != ' ':
      new_dir_x = -1
      new_dir_y = 0
  if dir_y != 0 and x < map_width:
    if o_map[y][x+1] != ' ':
      new_dir_x = 1
      new_dir_y = 0
  if dir_x != 0 and y > 0:
    if o_map[y-1][x] != ' ':
      new_dir_x = 0
      new_dir_y = -1
  if dir_x != 0 and y < map_height:
    if o_map[y+1][x] != ' ':
      new_dir_x = 0
      new_dir_y = 1
  dir_x = new_dir_x
  dir_y = new_dir_y
  move()
