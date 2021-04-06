import re 
'''
## Small Alp pattern matching
pattern = "[a-z]"
baya_name= 'liam','olivia','noah','emma'

for string in baya_name:
    result = re.match(pattern,string)
    if result:
        print("Sucessfull",result)
    else:
        print("Not matching")
'''
'''
## Cap Alp pattern matching
pattern = "[A-Z]"
baya_name= 'Liam','Olivia','Noah','Emma'
for string in baya_name:
    result = re.match(pattern,string)
    if result:
        print("Sucessfull",result)
    else:
        print("Not matching")


'''

### Both Cap and Small alp

pattern = "[a-z&A-Z]"
baya_name= 'Liam','Olivia','Noah','emma'

copy_result = []
for string in baya_name:
    result = re.match(pattern,string)
    copy_result.append(result)
    if result:
        print("Sucessfull",result)
    else:
        print("Not matching")
print(copy_result)




pattern = "[0-9]"
