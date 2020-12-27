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

     for numa in nums:
       for numb in nums:
         inuma = int(numa)
         inumb = int(numb)
         if inuma != inumb:
           if inuma % inumb == 0:
             print "%d divides evenly by %d" % (inuma, inumb)
             checksum = checksum + (inuma / inumb)
     row = fp.readline()


print " Checksum = %d" % checksum

