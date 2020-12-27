import re

filepath = '07_data.txt'  
tree = []

def parse_row(row):
    if row.find("->") > -1:
      match = re.search('([a-z]*) \((\d+)\) -> ([a-z, ]*)', row)
      ret = []
      ret.append(match.group(1))
      ret.append(match.group(2))
      ret.append(match.group(3).replace(" ", "").split(','))
      return ret
    else:
      match = re.search('([a-z]*) \((\d+)\)', row)
      ret = []
      ret.append(match.group(1))
      ret.append(match.group(2))
      ret.append([])
      return ret

def count_child_weight(parent):
  global tree
  for i in tree:
    if i[0] == parent:
      if i[2] == []:
        return int(i[1])
      else:
        c = int(i[1])
        for y in i[2]:
          c = c+count_child_weight(y)
        return c

def traverse_children(parent, depth, path_so_far):
  global tree
  for i in tree:
    if i[0] == parent:
      if i[2] == []:
        #print path_so_far,
        dummy = 1
      else:
        path_so_far += parent
        path_so_far += " -> "
        c = int(i[1])
        for y in i[2]:
          c = c+count_child_weight(y)
        for y in i[2]:
          traverse_children(y, depth+1, path_so_far)

with open(filepath) as fp:  
   row = fp.readline().rstrip()
   while row:
     tree.append(parse_row(row))
     row = fp.readline().rstrip()


element_root = ''

for element in tree:
  found = 0
  element_name = element[0]
  for i in tree:
    for x in i[2]:
      if element_name == x:
        found = 1
  if found == 0:
    print "FOUND THE ROOT! %s" % element_name
    element_root = element_name


traverse_children(element_root, 0, '')
      


