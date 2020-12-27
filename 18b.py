prog0 = []
prog1 = []
reg0 = dict()
reg1 = dict()
q0 = []
q1 = []
stall0 = 0
stall1 = 0
send_count = 0

pc0 = 0
pc1 = 0

with open ("18a_data.txt", "r") as myfile:
    for line in myfile:
        prog0.append(line.split())
        prog1.append(line.split())


last_sound0 = 0
last_sound1 = 0


def get(prog, b):
  try:
    z = int(b)
  except ValueError:
    if prog == 0:
      if b in reg0:
        z = reg0[b]
      else:
        reg0[b] = 0
        z = 0
    else:
      if b in reg1:
        z = reg1[b]
      else:
        reg1[b] = 0
        z = 0
  return z
    
def set(prog, a, b):
  print "SET %s, %s" % (a, b)
  if prog == 0:
    reg0[a] = get(0, b)
  else:
    reg1[a] = get(1, b)


def snd(prog, a):
  global last_sound0
  global last_sound1
  global q0
  global q1
  global send_count

  print "SND %s" % a
  if prog == 0:
    q0.append(get(0, a))
    print "q0 = ",
    print q0
  else:
    q1.append(get(1, a))
    print "q1 = ",
    print q1
    send_count += 1

def add(prog, a, b):
  print "ADD %s, %s" % (a, b)
  val = get(prog, a)
  val = val + get(prog, b)
  if prog == 0:
    reg0[a] = val
  else:
    reg1[a] = val


def mul(prog, a, b):
  print "MUL %s, %s" % (a, b)
  val = get(prog, a)
  val = val * get(prog, b)
  if prog == 0:
    reg0[a] = val
  else:
    reg1[a] = val

def mod(prog, a, b):
  print "MOD %s, %s" % (a, b)
  val = get(prog, a)
  val = val % get(prog, b)
  if prog == 0:
    reg0[a] = val
  else:
    reg1[a] = val

def rcv(prog, a):
  global pc0
  global pc1
  global q1
  global q0
  global stall0
  global stall1

  print "RCV %s" % (a)
  if prog == 0:
    if len(q1) == 0:
      stall0 = 1
    else:
      v = q1[0]
      del q1[0]
      set(prog, a, v)
      print "q1 = ",
      print q1
      stall0 = 0

  else:
    if len(q0) == 0:
      stall1 = 1
    else:
      v = q0[0]
      del q0[0]
      set(prog, a, v)
      print "q0 = ",
      print q0
      stall1 = 0


def jgz(prog, a, b):
  global pc0
  global pc1
  print "JGZ %s, %s" % (a, b)
  if (get(prog, a) > 0):
    if prog == 0:
      pc0 += get(prog, b)
    else:
      pc1 += get(prog, b)


def run(prog):
  global pc0
  global pc1

  start_pc = 0
  if prog == 0:
    start_pc = pc0
    print "[proc0]",
    print pc0,
    print ": ",
    i = prog0[pc0]
  else:
    start_pc = pc1
    print "[proc1]",
    print pc1,
    print ": ",
    i = prog1[pc1]

  if i[0] == 'set':
    set(prog, i[1], i[2])
  if i[0] == 'snd':
    snd(prog, i[1])
  if i[0] == 'add':
    add(prog, i[1], i[2])
  if i[0] == 'mul':
    mul(prog, i[1], i[2])
  if i[0] == 'mod':
    mod(prog, i[1], i[2])
  if i[0] == 'rcv':
    rcv(prog, i[1])
  if i[0] == 'jgz':
    jgz(prog, i[1], i[2])
  if prog == 0:
    print "  reg0: ",
    print reg0
    if (pc0 == start_pc) and stall0 == 0:
      pc0 = pc0 + 1
    if pc0 > len(prog0)-1:
      pc0 = -1
      print "Prog0 RAN TO COMPLETION"
    if stall0 == 1:
      print "Prog0 STALLING..."
  else:
    print "  reg1: ",
    print reg1
    if (pc1 == start_pc) and stall1 == 0:
      pc1 = pc1 + 1
    if pc1 > len(prog1)-1:
      pc1 = -1
      print "Prog1 RAN TO COMPLETION"
    if stall1 == 1:
      print "Prog1 STALLING..."


set(0, 'p', '0')
set(1, 'p', '1')

while True:
  print '---------------------------------------------'
  # Run prog0
  if pc0 > -1:
    run(0)
  # Run prog1
  if pc1 > -1:
    run(1)
  print "SEND COUNT = %d" % send_count
  if pc1 == -1 and pc0 == -1:
    print "Both programs finished"
    exit()
  if stall0 == 1 and stall1 == 1:
    print "DEADLOCK. Finishing."
    exit()
