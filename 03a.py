target = 347991

total = 1
steps = 0

for i in range (1, 900, 2):
  print "%d: %d" % (i, total)
  last = total
  total = (i*i)

  if total > target:
    print "%d: %d" % (i+1, total)

    print "--------"
    print "i = %d" % i
    print "last = %d" % last
    print "target = %d" % target

    # is number on right side?
    newlast = (last+1+((i-1)/2)-1)
    if target <= (last + (i-1)):
      print "On right stretch"
      # Down then left
      stepsA = abs(target - newlast)
      stepsB = ((i-1)/2)
      break
    if target <= (last + ((i-1)*2)):
      print "On upper stretch"
      # To middle, then down
      stepsA = abs(target - (newlast + (((i-1)/2)*2)))
      stepsB = ((i-1)/2) 
      break
    if target <= (last + ((i-1)*3)):
      print "On left stretch"
      # To middle, then down
      stepsA = abs(target - (newlast + (((i-1)/2)*4)))
      stepsB = ((i-1)/2)
      break
    if target <= (last + ((i-1)*4)):
      print "On lower stretch"
      # To middle, then down
      stepsA = abs(target - (newlast + (((i-1)/2)*6)))
      stepsB = ((i-1)/2)
      break
    break

print "Steps to middle: %d" % stepsA
print "Steps to center: %d" % stepsB

print "Steps = %d" % (stepsA + stepsB)
