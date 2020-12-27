length = 256
#lengths_string = '3, 4, 1, 5'
lengths_string = '187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216'
lengths_string = '130,126,1,11,140,2,255,207,18,254,246,164,29,104,0,224'
lengths = lengths_string.split(',')
string = []

for i in range(0, length):
  string.append(i)

print lengths
print string

pos = 0
skip = 0

for l in lengths:
  print "Doing length %s" % l
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
  print string

a = int(string[0])
b = int(string[1])

print "Final result: %d" % (a*b)
