filepath = '09_data.txt'

data = ''

with open(filepath) as fp:
   row = fp.readline().rstrip()
   while row:
     data += row
     row = fp.readline().rstrip()

#data = '{}'                             # 1
#data = '{{{}}},'                        # score of 1 + 2 + 3 = 6.
#data = '{{},{}},'                       # score of 1 + 2 + 2 = 5.
#data = '{{{},{},{{}}}},'                # score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
#data = '{<a>,<a>,<a>,<a>},'             # score of 1.
#data = '{{<ab>},{<ab>},{<ab>},{<ab>}},' # score of 1 + 2 + 2 + 2 + 2 = 9.
#data = '{{<!!>},{<!!>},{<!!>},{<!!>}},' # score of 1 + 2 + 2 + 2 + 2 = 9.
#data = '{{<a!>},{<a!>},{<a!>},{<ab>}},' # score of 1 + 2 = 3.

#data = '{<>,}'                           # 0 characters.
#data = '{<random characters>,'           # 17 characters.
#data = '{<<<<>,'                         # 3 characters.
#data = '{<{!>}>,'                        # 2 characters.
#data = '{<!!>,'                          # 0 characters.
#data = '{<!!!>>,'                        # 0 characters.
#data = '{<{o"i!a,<{i<a>,'                # 10 characters.

#iterate over data and remove cancelled characters
skip = 0
clean_data = ''

for d in data:
  if skip == 1:
    skip = 0
  else:
    if d == '!':
      skip = 1
      continue
    else:
      clean_data += d
 
print clean_data

#iterate over data and collapse garbage
garbage_count = 0
skip = 0
data = clean_data
clean_data = ''

for d in data:
  if ((skip == 1) and (d == '>')):
    skip = 0
    clean_data += '<>'
    continue
  if skip == 0:
    if d == '<':
      skip = 1
      continue
    clean_data += d
  else:
    garbage_count += 1

print clean_data

# Score group
total = 0
level = 1
for d in clean_data:
  if d == '{':
    total = total + level
    level = level + 1
  if d == '}':
    level = level - 1 

print total
print garbage_count
