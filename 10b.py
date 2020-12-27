length = 256
lengths_string = '3, 4, 1, 5'
lengths_string = '130,126,1,11,140,2,255,207,18,254,246,164,29,104,0,224'
#lengths_string = '1,2,3'



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
    new_string[b_pos] = a_val
  pos = (pos + skip + int(l)) % length
  skip += 1

  string = new_string


outstring = ''
for a in range(0, 16):
  out = int(string[a*16])
  for b in range(1, 16):
    index = (a*16) + b
    out = out ^ int(string[index])
  this_outstring = hex(out)[2:]
  if len(this_outstring) < 2:
    this_outstring = '0'+this_outstring
  outstring += this_outstring


if len(outstring) < 32:
  outstring = '0'+outstring
print outstring

