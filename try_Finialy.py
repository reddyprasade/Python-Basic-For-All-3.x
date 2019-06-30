try:
   f = open("testfile", "w")
   f.write("Test write statement")
finally:
   print ("Always execute finally code blocks")
