comps = []
with open ("24a_data.txt", "r") as myfile:
    for line in myfile:
        l = line.rstrip()
        r = []
        for p in l.split('/'):
          r.append(int(p))
        comps.append(r)
longest_length = 0
strongest_score = 0
strongest_bridge = []


def getCompatibleComps(pins, compList):
  result = []
  for comp in compList:
    if comp[0] == pins or comp[1] == pins:
      result.append(comp)
  return result


def finished(b):
  global strongest_score
  global strongest_bridge
  global longest_length
  score = 0
  for a in b:
    score+= a[0]
    score+= a[1]
  if len(b) >= longest_length:
    if score > strongest_score:
      print "FOUND STRONGEST BRIDGE, len=" + str(len(b)) + " ; score=" + str(score)
      strongest_bridge = b
      strongest_score = score
      longest_length = len(b)

def buildBridge(pins, compList, bridgeList):
  compatibleList = getCompatibleComps(pins, compList)
  if len(compatibleList) > 0:
    this_bridgeList = bridgeList[:]
    this_compList = compList[:]
    finished(bridgeList)
    for c in getCompatibleComps(pins, compList):
      new_bridgeList = this_bridgeList[:]
      new_compList = this_compList[:]
      new_bridgeList.append(c)
      new_compList.remove(c)
      if c[0] == pins:
        new_pins = c[1]
      else:
        new_pins = c[0]
      buildBridge(new_pins, new_compList, new_bridgeList)
  else:
    finished(bridgeList)
     



compList = comps[:]
bridgeList = []
pins = 0

buildBridge(pins, compList, bridgeList)

print "------------"
print strongest_bridge
print strongest_score
