result_list = []
#list = [0, 2, 7, 0]
list = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]
count = 0

list_str = str(list)
result_list.append(list_str)

while True:
  count = count + 1
  max_num = -1
  max_i = -1
  for i in range(0, len(list)):
    if list[i] > max_num:
      max_num = list[i]
      max_i = i

  index = max_i
  list[index] = 0
  while max_num > 0:
    index = index + 1
    if index >= len(list):
      index = 0
    list[index] = list[index] + 1
    max_num = max_num -1


  list_str = str(list)
  for r_str in result_list:
    if r_str == list_str:
      print "PART ONE: Steps = %d" % count
      count = 0
      for r_str in result_list:
        count = count + 1
        if r_str == list_str:
          #print len(result_list)
          #print count
          print "PART TWO: Cycles = %d" % (len(result_list) - count + 1)

      
      exit()
  result_list.append(list_str)


