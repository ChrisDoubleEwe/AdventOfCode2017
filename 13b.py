# lanes
#   0 - lane ID
#   1 - depth
#   2 - current_pos
#   3 - current_direction

packet_lane = -1
num_lanes = 0
index = 0
lanes = []
severity = 0
collisions = []

with open ("13a_data.txt", "r") as myfile:
    for line in myfile:
        line_array = line.split(':')
        row = []
        row_index = int(line_array[0].rstrip())
        while index < row_index:
          row.append(index)
          row.append(0)
          row.append(-1)
          row.append(0)
          lanes.append(row)
          row = []
          index += 1
        if row_index == index:
          row.append(row_index)
          row.append(int(line_array[1].rstrip())-1)
          row.append(0)
          row.append(1)
          lanes.append(row)
          index += 1
          num_lanes = row_index

print "Num lanes = %d" % num_lanes

for i in range(0, num_lanes+1):
  row = []
  for k in range(0, num_lanes+1):
    row.append(2)
  collisions.append(row)

#print collisions

def move_packet():
  global packet_lane
  packet_lane += 1

def move_lanes():
  for i in range(0, num_lanes+1):
    if lanes[i][1] > 0:
      # Update current pos
      lanes[i][2] = lanes[i][2]+lanes[i][3]
      # Update direction
      if lanes[i][2] == lanes[i][1]:
        lanes[i][3] = -1
      if lanes[i][2] == 0:
        lanes[i][3] = 1
        
def check_collision():
  global packet_lane
  global severity
  global packet_time
  list_num = 0-(num_lanes+1)
  for x in results[list_num:]:
    if len(x[1]) <= num_lanes:
      this_packet_time = x[0]
      this_lane = packet_time - this_packet_time
      if lanes[this_lane][2] == 0:
        results[this_packet_time][1] += '1'
      else:
        results[this_packet_time][1] += '0'

def check_made_it():
  total = 0
  index = 0
  list_num = 0-(num_lanes+1)
  for x in results[list_num:]:
    #print "  ",
    #print x
    this_packet_time = x[0]
    if len(x[1]) == num_lanes+1: 
      if '1' not in x[1]:
        print x
        print "MADE IT!"
        exit() 

results = []
packet_time = 0
while True:
    results.append([packet_time,''])
    print packet_time
    check_collision()
    check_made_it()
    move_lanes()
    packet_time += 1
    #if packet_time > 30:
    #  exit()
