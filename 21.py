import math
pattern = '.#./..#/###'

two = []
three = []

with open ("21a_data.txt", "r") as myfile:
    for line in myfile:
      if len(line.rstrip()) == 20:
        two.append(line.rstrip().split(' => '))
      else:
        three.append(line.rstrip().split(' => '))

def size(pattern):
  row = pattern.find('/')
  return row




def printout(pattern):
  #print
  #print
  #print pattern
  if size(pattern) % 2 == 0:
    spliton = 2
    #print "It's a 2x2 grid"
  else:
    #print "It's a 3x3 grid"
    spliton = 3

  ar = pattern.split('/')
  for r in range(0, len(ar)):
    row = ''
    for c in range(0, len(ar[0])):
      row+= str(ar[r][c])
      if (c+1) % spliton == 0:
        row+=" "
    print row
    if (r+1) % spliton == 0:
      print

def count_pixels(pattern):
  count = 0
  for c in pattern:
    if c == '#':
      count += 1
  return count

# Flip Horizontal
def flip_h(pattern):
  out = ''
  for r in pattern.split('/'):
    out_row = ''
    for c in r:
      out_row = c + out_row
    out = out + out_row + '/'
  out = out[:-1]
  return out

# Flip Vertical
def flip_v(pattern):
  out = ''
  for r in pattern.split('/'):
    out_row = r
    out = out_row + '/' + out 
  out = out[:-1]
  return out

# Rotate
def rotate(pattern):
  m = []
  out_str = ''
  for r in pattern.split('/'):
    m.append(list(r))
  for b in range(0, len(m)):
    for a in range(len(m)-1, -1, -1):
      out_str = out_str + m[a][b]
    out_str += '/'
  return out_str[:-1]
  

def match2(pattern):
  for p in two:
    x = p[0]

    for i in range(0, 4):
      if pattern == x or pattern == flip_h(x) or pattern == flip_v(x):
        #print "  matched on ",
        #print p
        return p[1]
      x = rotate(x)

def match3(pattern):
  for p in three:
    x = p[0]

    for i in range(0, 4):
      if pattern == x or pattern == flip_h(x) or pattern == flip_v(x):
        #print "  matched on ",
        #print p
        return p[1]
      x = rotate(x)
 
def compress_to_square(result):
  side = int(math.sqrt(len(result)))
  if side == 1:
      return result[0]
  row_str = ''

  row = 0
  num_grids = len(result)
  grid_size = len(result[0].split('/'))
  for row in range(0, grid_size * side):
    for i in range ((row // grid_size)*side, ((row // grid_size)*side)+side):
      row_num = row % grid_size
      row_str += result[i].split('/')[row_num]
    row_str += '/'
  row_str = row_str[:-1]
  return row_str

def expand2(pattern):
  m = []
  for r in pattern.split('/'):
    m.append(list(r))

  result = []
  expand_square = ''
  for a in range(0, size(pattern)/2):
    for b in range(0, size(pattern)/2):
      sub_square = m[a*2][b*2]+m[a*2][(b*2)+1]+'/'+m[(a*2)+1][(b*2)]+m[(a*2)+1][(b*2)+1]
      expand_square = match2(sub_square)
      result.append(expand_square)

  #Turn set of expanded squares back into single square
  #print "expand2-intermediate: ",
  #print result
  result = compress_to_square(result)
  return result
 
def expand3(pattern):
  m = []
  for r in pattern.split('/'):
    m.append(list(r))

  result = []
  expand_square = ''
  for a in range(0, size(pattern)/3):
    for b in range(0, size(pattern)/3):
      sub_square = m[a*3][b*3]+m[a*3][(b*3)+1]+m[a*3][(b*3)+2]+'/'+m[(a*3)+1][(b*3)]+m[(a*3)+1][(b*3)+1]+m[(a*3)+1][(b*3)+2]+'/'+m[(a*3)+2][(b*3)]+m[(a*3)+2][(b*3)+1]+m[(a*3)+2][(b*3)+2]
      expand_square = match3(sub_square)
      result.append(expand_square)

  #Turn set of expanded squares back into single square
  #print "expand3-intermediate: ",
  #print result
  result = compress_to_square(result)
  return result 

#print "Start"
#printout(pattern)

count = 0
while True:
  count += 1

  if count > 18:
    exit()

  print "Iteration %d" % count



  if size(pattern) % 2 == 0:
    pattern = expand2(pattern)
  else:
    pattern = expand3(pattern)

  #printout(pattern)
  print count_pixels(pattern)
