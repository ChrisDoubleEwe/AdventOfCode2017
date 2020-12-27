# p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
import re

pattern = re.compile(r'=<\(.*\),\(.*\),\(.*\)>')
p = []

with open ("20a_data.txt", "r") as myfile:
    for line in myfile:
      x = []
      tuples = re.findall(r'<-?\d+,-?\d+,-?\d+>', line) 
      for tuple in tuples:
        group = tuple[1:-1]
        group_list = group.split(',')
        t = []
        for i in group_list:
          t.append(int(i))
        x.append(t)
      p.append(x)

def unique(seq): 
   print "incoming: ",
   print seq
   # order preserving
   checked = []
   for e in seq:
       if e not in checked:
           checked.append(e)
   print "  pre-sort: ",
   print checked
   checked.sort(reverse=True)
   print "  post-sort: ",
   print checked
   return checked

def get_closest_particle():
  default = 9999999999999999
  c_dist = default
  c_particle = -1
  for x in range(0, len(p)):
    distance = abs(p[x][0][0]) + abs(p[x][0][1]) + abs(p[x][0][2])
    if distance < c_dist:
      c_dist = distance
      c_particle = x
  if c_dist == default:
    print "Error! No closest particle found!"
    exit()
  return c_particle

def check_collisions():
  found_collision = 1
  while found_collision == 1:
    remove = []
    found_collision = 0
    for x in range(0, len(p)-1):
      for y in range(x+1, len(p)):
        if p[x][0][0] == p[y][0][0] and p[x][0][1] == p[y][0][1] and p[x][0][2] == p[y][0][2]:
          found_collision = 1
          remove.append(x)
          remove.append(y)
          print remove
    if found_collision == 1:
      remove = unique(remove)
      print remove
      for i in remove:
        print "    Collision detected. Removing particle %d" % i
        del p[i]

    
        

def count_particles():
  return len(p)

def move_particles():
  for x in range(0, len(p)): 
    # Update velocity with acceleration
    p[x][1][0] += p[x][2][0] 
    p[x][1][1] += p[x][2][1]
    p[x][1][2] += p[x][2][2]

    # Update position with velocity
    p[x][0][0] += p[x][1][0]
    p[x][0][1] += p[x][1][1]
    p[x][0][2] += p[x][1][2]

    print p[x]

p_count = -1
stable_count = 0

while stable_count < 100:
  print "----------------------"
  last_p_count = p_count
  move_particles()
  check_collisions()
  p_count = count_particles()
  print  "  p_count = %d" % p_count
  if p_count == last_p_count:
    stable_count += 1
  else:
    stable_count = 0

print "STABLE. Particle count: %d " % p_count
  
