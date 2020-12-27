import math

map = []
infections = 0

with open ("22a_data.txt", "r") as myfile:
    for line in myfile:
      map.append(list(line.rstrip()))

print map
m_size = len(map[0])

print m_size
cur_x = ((m_size-1)/2)
cur_y = ((m_size-1)/2)

# 1= N ; 2=E ; 3=S ; 4=W
cur_dir = 1

def printout():
  print '------------'
  print m_size
  print "x = %d ; y = %d " % (cur_x, cur_y)
  for r in map:
    print ''.join(r)

def expand():
   global cur_x
   global cur_y
   global m_size

   for r in range(0, m_size):
     new = map[r]
     new.append('.')
     new.insert(0, '.')
     map[r] = new
   m_size += 2
   map.append(list('.'*m_size))
   map.insert(0, list('.'*m_size))
   cur_x += 1
   cur_y += 1
     
def turn_right():
  global cur_dir
  cur_dir += 1
  if cur_dir > 4:
    cur_dir = 1

def turn_left():
  global cur_dir
  cur_dir -= 1
  if cur_dir < 1:
    cur_dir = 4

def move_forward():
  global cur_x
  global cur_y
  # N
  if cur_dir == 1:
    if cur_y == 0:
      expand()
    cur_y -= 1
  # S
  if cur_dir == 3:
    if cur_y >= (m_size-1):
      expand()
    cur_y += 1
  # W
  if cur_dir == 4:
    if cur_x == 0:
      expand()
    cur_x -= 1
  # E
  if cur_dir == 2:
    if cur_x >= (m_size-1):
      expand()
    cur_x += 1

def doit():
  global infections
  print "x = %d ; y = %d ; m_size = %d" % (cur_x, cur_y, m_size)

  if map[cur_y][cur_x] == '#':
    turn_right()
    map[cur_y][cur_x] = '.'
    move_forward()
  else:
    turn_left()
    print "x = %d ; y = %d ; m_size = %d" % (cur_x, cur_y, m_size)
    map[cur_y][cur_x] = '#'
    infections += 1
    move_forward()



round = 1
while round < 10001:
  print "Round %d" % round
  round += 1

  doit()

  #printout()
print "Total infections: %d" % infections
