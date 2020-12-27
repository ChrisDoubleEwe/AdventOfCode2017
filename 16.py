line = 'abcdefghijklmnop'
#line = 'abcde'

line_array = list(line)
line_length = len(line_array)

filepath = '16a_data.txt'

instr = []
input = ''
with open(filepath) as fp:
   row = fp.readline().rstrip()
   while row:
     input += row
     row = fp.readline().rstrip()

instr = input.split(',')


def spin(v):
  print "Spin: %d" % v
  while v > 0:
    i = line_array.pop()
    line_array.insert(0, i)
    v -= 1

def exchange(a, b):
  print "Exchange %d with %d" % (a, b)
  a_val = line_array[a]
  b_val = line_array[b]
  line_array[a] = b_val
  line_array[b] = a_val

def swap(a, b):
  print "Swap %s with %s" % (a, b)
  a_index = line_array.index(a)
  b_index = line_array.index(b)
  line_array[a_index] = b
  line_array[b_index] = a


print ''.join(line_array)
for i in instr:
  i_array = list(i)
  if i_array[0] == 's':
    print i
    s_val = ''.join(i_array[1:len(i_array)])
    spin(int(s_val))
  if i_array[0] == 'x':
    print i
    x_val = ''.join(i_array[1:len(i_array)])
    x_val_array = x_val.split('/')
    exchange(int(x_val_array[0]) , int(x_val_array[1]))
  if i_array[0] == 'p':
    print i
    swap(i_array[1], i_array[3])
  print ''.join(line_array)
