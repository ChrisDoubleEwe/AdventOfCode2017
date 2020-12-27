tape = [0]

states = dict()


states['A'] = [[0, 1, 'R', 'B'], [1, 0, 'L', 'C']]
states['B'] = [[0, 1, 'L', 'A'], [1, 1, 'R', 'D']]
states['C'] = [[0, 0, 'L', 'B'], [1, 0, 'L', 'E']]
states['D'] = [[0, 1, 'R', 'A'], [1, 0, 'R', 'B']]
states['E'] = [[0, 1, 'L', 'F'], [1, 1, 'L', 'C']]
states['F'] = [[0, 1, 'R', 'D'], [1, 1, 'R', 'A']]


current_state = 'A'

def left():
  global cursor
  if cursor == 0:
    tape.insert(0, 0)
  else:
    cursor -=1

def right():
  global cursor
  if cursor == len(tape)-1:
    tape.append(0)
  cursor+=1
 
def action():
  global current_state
  global tape
  a = states[current_state]
  for i in a:
    if i[0] == tape[cursor]:
      r = i

  tape[cursor] = r[1]
  current_state = r[3]
  if r[2] == 'R':
    right()
  else:
    left() 


target = 12667664
steps = 0
cursor = 0

while steps < target:
  if steps % 100000 == 0:
    print steps
  action()
  steps += 1

print tape

print "Checksum =",
print tape.count(1)
