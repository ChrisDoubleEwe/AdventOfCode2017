length = 256

result_array = []


def decode(s):
  lengths_string = s
  lengths = []

  for c in lengths_string:
    lengths.append(ord(c))
  lengths.append(17)
  lengths.append(31)
  lengths.append(73)
  lengths.append(47)
  lengths.append(23)


  string = []

  for i in range(0, length):
    string.append(i)


  pos = 0
  skip = 0

  for z in range(0, 64):
   for l in lengths:
    new_string = string[:]
    for i in range(0, int(l)):
      a_pos = (pos + i) % length
      a_val = string[a_pos]
      b_pos = (pos+(int(l)-i-1)) % length
      b_val = string[b_pos]
      #print "Moving string[%d] (%s) to string[%d] (%s)" % (a_pos, a_val, b_pos, b_val)
      new_string[b_pos] = a_val
      #print "   new_string: %s" % new_string
      #print "   string:     %s" % string
    pos = (pos + skip + int(l)) % length
    skip += 1

    string = new_string

  outstring = ''
  for a in range(0, 16):
    out = int(string[a*16])
    for b in range(1, 16):
      index = (a*16) + b
      out = out ^ int(string[index])
    outstring += hex(out)[2:].zfill(2)
  
  #print outstring  
  
  # Convert hash to binary
  out_string = ''
  for b in outstring:
    out_string += str(bin(int(b, 16))[2:].zfill(4)).rstrip()

  return out_string



total_used = 0
for i in range(0, 128):
  lengths_string = 'hwlqcszp-' + str(i)
  #lengths_string = 'flqrgnkx-' + str(i)
  #print lengths_string
  decoded = decode(lengths_string)
  result_array.append(list(decoded))
  total_used += decoded.count('1')

print "PART ONE: Total used: %d" % total_used



# result_array(row, column)
size = 128
start_row = 3
start_col = 2

row = start_row
col = start_col

def printout():
  for row in result_array:
    row_str = ''
    for c in row:
      row_str += c
    print row_str

def fill_contiguous_row(row, col):
  fill_col = col + 1
  while (fill_col < size) and (result_array[row][fill_col] == '1'):
    result_array[row][fill_col] = 'x'
    fill_col += 1
  # Fill in all contiguous to the right
  fill_col = col - 1
  while (fill_col >= 0) and (result_array[row][fill_col] == '1'):
    result_array[row][fill_col] = 'x'
    fill_col -= 1

def traverse_region(row, col):
  result_array[row][col] = 'x'
  changes = 1
  while changes > 0:
    changes = 0
    fill_contiguous_row(row, col)
    # fill descending
    for r in range(row+1, size):
      for c in range(0, size):
        if (result_array[r-1][c] == 'x') and (result_array[r][c] == '1'):
          result_array[r][c] = 'x'
          changes += 1
          fill_contiguous_row(r, c)
    # fill ascending
    for r in range(size-2, -1, -1):
      for c in range(0, size):
        #print "r=%d, c=%d" % (r, c)
        if (result_array[r+1][c] == 'x') and (result_array[r][c] == '1'):
          result_array[r][c] = 'x'
          changes += 1
          fill_contiguous_row(r, c)
     
def replace_with_z():
  for r in range(0, size):
    for c in range(0, size):
      if result_array[r][c] == 'x':
        result_array[r][c] = '.'
 
total_groups = 0
for r in range(0, size):
  for c in range(0, size):
    if result_array[r][c] == '1':
      total_groups += 1
      traverse_region(r, c)
      #printout()

      replace_with_z()
      
print "PART TWO: " + str(total_groups)
