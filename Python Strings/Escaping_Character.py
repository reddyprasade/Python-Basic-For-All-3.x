# Escape Characters in Python


# Single quote escape character
print('This is Michael\'s house')

# Double quote escape character
print("He told me, \"Go home\", which I did")


# Tab escape character
print('\tThis is good')

# Carriage Return
txt = "Hello\rWorld!"
print(txt) 

#  A backslash followed by three integers will result in a octal value:

txt = "\110\145\154\154\157"
print(txt) 


# A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

# 
print('\x0c',end='')

print('\f',end='')