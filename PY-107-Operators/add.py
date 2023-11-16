"""# Get the input for the two variables
num1, num2 = map(int, input().split())

sum_integer =0

# Write the logic to add these numbers here:

sum_integer= num1+num2


# Print the sum 
print(sum_integer)
"""

numArray = map(int, input().split()) # Get the input


sum_integer = 0
# write your logic to add these 4 numbers here
# numArray=[1,2,3,4]
sum_integer= sum(numArray,sum_integer)


print(sum_integer)
