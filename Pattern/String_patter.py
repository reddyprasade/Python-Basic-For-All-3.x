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
