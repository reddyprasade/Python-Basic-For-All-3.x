import pickle

# we open the file for reading
fileObject = open('testfile.csv','rb')  

# load the object from the file into var b
b = pickle.load(fileObject)  
print(b)
