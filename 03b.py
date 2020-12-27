w, h = 20, 20;
Matrix = [[0 for x in range(w)] for y in range(h)] 

#Initialize to zero
for x in range  (0, w):
  for y in range (0, h):
    Matrix[x][y] = 0


def my_value(y,x):
  print "y, x = %d, %d" % (y, x)
  total = 0
  total = total + Matrix[y-1][x-1]
  total = total + Matrix[y-1][x]
  total = total + Matrix[y-1][x+1]
  total = total + Matrix[y][x-1]
  total = total + Matrix[y][x]
  total = total + Matrix[y][x+1]
  total = total + Matrix[y+1][x-1]
  total = total + Matrix[y+1][x]
  total = total + Matrix[y+1][x+1]
  print total
  if total > 347991:
    exit()
  return total



i = 1


#Start location = 1
x = (w-1)/2
y = (h-1)/2
Matrix[y][x] = 1

x = x+1
i = i+1
Matrix[y][x] = 1


while True:
  #Keep moving up until there's space left
  while Matrix[y][x-1] !=0:
    i = i+1
    y = y-1
    Matrix[y][x] = my_value(y, x)

  #Keep moving left until there's space down:
  while Matrix[y+1][x] !=0:
    i = i+1
    x = x-1
    Matrix[y][x] = my_value(y, x)

  #Keep moving down until there's space right
  while Matrix[y][x+1] !=0:
    i = i+1
    y = y+1
    Matrix[y][x] = my_value(y, x)


  #Keep moving right until there's space up:
  while Matrix[y-1][x] !=0:
    i = i+1
    x = x+1
    Matrix[y][x] = my_value(y, x)






# Print matrix

for x in range  (0, w):
  for y in range (0, h):
    print Matrix[x][y],
    print " ",
  print " "


