"""
Given an integer, n , print the following values for each integer i from 1 to n :

* Decimal
* Octal
* Hexadecimal (capitalized)
* Binary

Function Description:
    Complete the print_formatted function in the editor below.
    print_formatted has the following parameters:
    int number: the maximum value to print
"""
def print_formatted(number):
    # your code goes here
    width = len("{0:b}".format(number))
    for i in range(1,n+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))
n = int(input())
print_formatted(n)



# Method -2 
from future import print_function
st=int(raw_input())
w=len(bin(st)[2:])
for i in range(1,st+1):
    print((str(i).rjust(w,' '),str(oct(i)[1:]).rjust(w,' '),str(hex(i)[2:].upper()).rjust(w,' '),str(bin(i)[2:]).rjust(w,' '),sep=' '))
    
    
    
# Method-3 
STDIN = int(raw_input())
w = len(str(bin(STDIN)).replace('0b',''))

for i in xrange(1, STDIN+1):
    b = bin(int(i)).replace('0b','').rjust(w, ' ')
    o = oct(int(i)).replace('0','', 1).rjust(w, ' ')
    h = hex(int(i)).replace('0x','').upper().rjust(w, ' ')
    j = str(i).rjust(w, ' ')
    print(j, o, h, b)

 # Method-4
n = int(input())

results = []

for i in range(1, n+1):
    decimal = str(i)
    octal = str(oct(i)[2:])
    hex_ = str(hex(i)[2:]).upper()
    binary = str(bin(i)[2:])

    results.append([decimal, octal, hex_, binary])

width = len(results[-1][3])  # largest binary number

for i in results:
    print(*(rep.rjust(width) for rep in i))
