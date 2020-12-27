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
  if packet_lane >= 0:
    if lanes[packet_lane][2] == 0:
      print "    COLLISION IN LANE %d" % packet_lane
      severity += (packet_lane * (lanes[packet_lane][1]+1))

def initialize_lanes():
  for i in range(0, num_lanes+1):
    if lanes[i][1] > 0:
      # Update current pos
      lanes[i][2] = 0
      # Update direction
      lanes[i][3] = 1

  


severity = 1
start_packet_lane = -1

packet_lane = start_packet_lane
print "  trying offset %d" % abs(start_packet_lane)
severity = 0
initialize_lanes()
while packet_lane < num_lanes:
  #print "  packet lane = %d" % packet_lane
  move_packet()
  check_collision()
  move_lanes()
print "START = %d ; SEVERITY = %d" % (start_packet_lane, severity)
start_packet_lane -= 1

