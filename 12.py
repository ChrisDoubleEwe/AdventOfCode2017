filepath = '12a_data.txt'

pipes = []

def unique_list(seq):
   # order preserving
   checked = []
   for e in seq:
       if e not in checked:
           checked.append(e)
   checked.sort()
   return checked

def group_count(id, already_seen):
  total = 0
  if id in already_seen:
    return 0
  else:
    total = 1
    already_seen.append(id)
    # Find row
    for p in pipes:
      if p[0] == id:
        for c in p[1]:
          total = total + group_count(c, already_seen)
    return total

def group_enum(id, already_seen):
  if id in already_seen:
    return ''
  else:
    already_seen.append(id)
    # Find row
    for p in pipes:
      if p[0] == id:
        for c in p[1]:
          groups = group_enum(c, already_seen)
          for g in groups:
            already_seen.append(g)
    return unique_list(already_seen)

with open(filepath) as fp:
   nodes = []
   row = fp.readline().rstrip()
   while row:
     sources = row.split(' <-> ')
     dest_string = "".join(sources[1].split())
     source = sources[0].rstrip()
     dests = dest_string.split(',')
     insert = []
     insert.append(source)
     insert.append(dests)
     nodes.append(source)
     for n in dests:
       nodes.append(n)

     pipes.append(insert)
     row = fp.readline().rstrip()

print nodes
nodes = unique_list(nodes)
print nodes


zero_total = group_count('0', [])



print "Starting"
all_groups = []
group_count = 0
node_count = len(nodes)
while len(nodes) > 0:
  n = nodes[0]
  node_count += -1
  print "Nodes: %d" % len(nodes)
  total = group_enum(n, [])
  print "  got group"
  if total not in all_groups:
    all_groups.append(total)
    group_count += 1
  print "  added to set"
  for z in total:
    nodes.remove(z)

print "PART ONE: " + str(zero_total)
print "PART TWO: Group Count = %d " % group_count
