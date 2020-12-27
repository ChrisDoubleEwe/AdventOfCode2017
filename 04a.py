filepath = '04_data.txt'  
count = 0

cnt = 0
with open(filepath) as f:
  for row in f:
     print "Doing Row: " + str(row)
     valid = 1
     passx = []
     words = row.split()
     print words
     for word in words:
       print word
       if word in passx:
         print "  INVALID: " + word
         valid = 0
       else:
         passx.append(word)
     if valid == 1:
       count = count + 1


print "\n\n\n\n"
print "Total valid: %d" % count

