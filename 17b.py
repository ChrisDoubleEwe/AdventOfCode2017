step = 355

buf = []
buf.append(0)

pos = 0
for i in xrange(1, 50000001):
  if i % 50000 == 0:
    print i/50000
  for j in range(0, step):
    pos +=1
    if pos > len(buf)-1:
      pos = 0

  if pos+1 < len(buf):
    buf.insert(pos+1, i)
  else:
    buf.append(i)
  pos = pos + 1

index = buf.index(0)

print buf[index+1]
