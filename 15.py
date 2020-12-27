genA = 65
genB = 8921
genA = 591
genB = 393

genA_factor = 16807
genB_factor = 48271


count = 0
for i in range(0, 40000000):
  if i % 100000 == 0:
    print i
  nextA = genA * genA_factor % 2147483647
  nextB = genB * genB_factor % 2147483647
 
  #print "  %d    %d" % (nextA, nextB)

  genA = nextA
  genB = nextB
 
  genA_bin = str(bin(genA)[2:].zfill(32))
  genB_bin = str(bin(genB)[2:].zfill(32))
  #print genA_bin
  #print genB_bin

  if genA_bin[-16:] == genB_bin[-16:]:
    #print "MATCH!"
    count = count+1

print "Toal matches: %d" % count


