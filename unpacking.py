letters = ["a", "b", "c"]
print(letters)
letters.append("e")
print(letters)
letters.insert(0, "-")
print(letters)
#first, second, third,*other = letters
#print(first)
#print(second)
#print(other)
#print(third)
#for l in letters:
#    print(l)
for index, letter in enumerate(letters):
    print(index)
    print(letter)
