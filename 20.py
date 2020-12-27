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

closest_particle = -1
stable_count = 0

while stable_count < 1000:
  print "----------------------"
  last_closest_particle = closest_particle
  move_particles()
  closest_particle = get_closest_particle()
  print  "  closest particle = %d" % closest_particle
  if closest_particle == last_closest_particle:
    stable_count += 1
  else:
    stable_count = 0

print "STABLE. Closest particle: %d " % closest_particle
  
