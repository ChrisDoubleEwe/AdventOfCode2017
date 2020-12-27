filepath = '02_data.txt'  
checksum = 0

with open(filepath) as fp:  
   row = fp.readline()
   cnt = 1
   while row:
     print row
     nums = row.split()
     low = 9999999999
     high = 0
     for num in nums:
       print num
       i_num = int(num)
       if i_num < low:
         low = i_num
       if i_num > high:
         high = i_num
     diff = high - low
     checksum = checksum+diff
     print "    %d" % diff

     print "----"
     row = fp.readline()


print " Checksum = %d" % checksum

