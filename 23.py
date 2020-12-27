prog = []
reg = dict()
pc = 0
mul_count = 0

with open ("23_data.txt", "r") as myfile:
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

def sub(a, b):
  print "ADD %s, %s" % (a, b)
  val = get(a)
  val = val - get(b)
  reg[a] = val

def mul(a, b):
  global mul_count
  mul_count += 1
  print "MUL %s, %s" % (a, b)
  val = get(a)
  val = val * get(b)
  reg[a] = val

def jnz(a, b):
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
  if i[0] == 'sub':
    sub(i[1], i[2])
  if i[0] == 'mul':
    mul(i[1], i[2])
  if i[0] == 'jnz':
    jnz(i[1], i[2])
  if pc == start_pc:
    pc = pc + 1
  print reg

print "MUL count = %d" % mul_count
