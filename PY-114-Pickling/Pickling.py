import pickle

a = ['test value','test value 2','test value 3']



# open the file for writing
fileObject = open('testfile.txt','wb') 

# this writes the object a to the
# file named 'testfile'
pickle.dump(a,fileObject)   

# here we close the fileObject
fileObject.close()
