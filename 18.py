prog = []
reg = dict()
pc = 0

with open ("18a_data.txt", "r") as myfile:
    for line in myfile:
        prog.append(line.split())

print prog 
print reg
last_sound = 0

def get(b):
  try:
    z = int(b)
  except ValueError:
    if b in reg:
      z = reg[b]
    else:
      reg[b] = 0
      z = 0
  return z
    
def set(a, b):
  print "SET %s, %s" % (a, b)
  print b
  reg[a] = get(b)

def snd(a):
  global last_sound
  print "SND %s" % a
  last_sound = get(a)

def add(a, b):
  print "ADD %s, %s" % (a, b)
  val = get(a)
  val = val + get(b)
  reg[a] = val

def mul(a, b):
  print "MUL %s, %s" % (a, b)
  val = get(a)
  val = val * get(b)
  reg[a] = val

def mod(a, b):
  print "MOD %s, %s" % (a, b)
  val = get(a)
  val = val % get(b)
  reg[a] = val

def rcv(a):
  global last_sound
  print "RCV %s" % (a)
  if get(a) != 0:
    print "    LAST SOUND = %d" % last_sound
    exit()

def jgz(a, b):
  global pc
  print "JGZ %s, %s" % (a, b)
  if (get(a) != 0):
    pc += get(b)


while pc < len(prog):
  i = prog[pc]
  print pc,
  print ": ",
  start_pc = pc
  if i[0] == 'set':
    set(i[1], i[2])
  if i[0] == 'snd':
    snd(i[1])
  if i[0] == 'add':
    add(i[1], i[2])
  if i[0] == 'mul':
    mul(i[1], i[2])
  if i[0] == 'mod':
    mod(i[1], i[2])
  if i[0] == 'rcv':
    rcv(i[1])
  if i[0] == 'jgz':
    jgz(i[1], i[2])
  if pc == start_pc:
    pc = pc + 1
  print reg

