filepath = '05_data.txt'  
count = 0
list = []
with open(filepath) as fp:  
   row = fp.readline()
   while row:
     list.append(int(row.rstrip()))
     count = count+1
     row = fp.readline()


instr_count = 1
print "\n\n\n\n"
print "Total count: %d" % count
print list

pc = 0
while True:
  instr = list[pc]
  print "instr_count=%d : pc=%d : instr=%d" % (instr_count, pc, instr)
  #print list
  if pc + instr >= count:
    print "ESCAPED!"
    print instr_count
    exit()
  list[pc] = instr +1
  pc = pc + instr
  instr_count = instr_count + 1



