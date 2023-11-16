### Dictionary Merging
# Declare a dict
student = {'name': 'John', 'age': 14}
# Get a value 
age = student['age']
print(age) # age is 14


# Update the age Values
student['age'] = 25

print(student['age'])

# # Insert a key-value pair
student['score'] = 'A'


### Merging Dictionaries

# two dicts to start with
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}


d3 = d1.copy()
print("Before update",d3)# d1 keys and values are same
d3.update(d2) # update Values d2
print("After Update",d3)

d2a = {'a': 10, 'c': 3, 'd': 4}

# create a copy of d1, as update() modifies the dict in-place
d3 = d1.copy()
# update the d3 with d2
d3.update(d2)
# d3 now is {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# another way to update
di = {**d1,**d2}
print(di)

# Merging Dictionaries in another way
d = d1 | d2
print(d)
 
