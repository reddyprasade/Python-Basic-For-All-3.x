try:
    f = open('testfile','r')
    f.write('Test write this')
except IOError:
    # This will only check for an IOError exception and then execute this print statement
   print ("Error: Could not find file or read data")
else:
   print ("Content written successfully")
   f.close()
