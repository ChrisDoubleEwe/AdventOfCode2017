# 0 - Dest register
# 1 - Operation
# 2 - Op value
# 3 - IF
# 4 - Test register
# 5 - Condition
# 6 - Test value

program = []
registers = {}
max_value = 0

filepath = '08_data.txt'

with open(filepath) as fp:
   row = fp.readline().rstrip()
   while row:
     print row
     program.append(row.split())
     row = fp.readline().rstrip()

# Find largest value in any register
def find_max():
  global max_value 
  global registers
  for i in registers:
    if registers[i] > max_value:
      max_value = registers[i]


# Initialise registers
for r in program:
  registers[r[0]] = 0
  registers[r[4]] = 0

# Run program
for r in program:
  if r[5] == '>':
    if registers[r[4]] > int(r[6]):
      if r[1] == 'inc':
        registers[r[0]] += int(r[2])
      else:
        registers[r[0]] -= int(r[2])
  if r[5] == '<':
    if registers[r[4]] < int(r[6]):
      if r[1] == 'inc':
        registers[r[0]] += int(r[2])
      else:
        registers[r[0]] -= int(r[2])
  if r[5] == '>=':
    if registers[r[4]] >= int(r[6]):
      if r[1] == 'inc':
        registers[r[0]] += int(r[2])
      else:
        registers[r[0]] -= int(r[2])
  if r[5] == '<=':
    if registers[r[4]] <= int(r[6]):
      if r[1] == 'inc':
        registers[r[0]] += int(r[2])
      else:
        registers[r[0]] -= int(r[2])
  if r[5] == '==':
    if registers[r[4]] == int(r[6]):
      if r[1] == 'inc':
        registers[r[0]] += int(r[2])
      else:
        registers[r[0]] -= int(r[2])
  if r[5] == '!=':
    if registers[r[4]] != int(r[6]):
      if r[1] == 'inc':
        registers[r[0]] += int(r[2])
      else:
        registers[r[0]] -= int(r[2])
  find_max()

print max_value

