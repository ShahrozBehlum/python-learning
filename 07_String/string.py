#Denoted by '', "", """ """
#mostly we use unicode string
# str is immutable it give new object doesn't change original

username = 'Shahroz'
print(username)
print(len(username))

cast = "I am \"Malik\""
print(cast)

firstChar = username[0]
print(firstChar)

lastChar = username[-1]
print(lastChar)

#Slicing(substring) method the last index doesn't include
num_list = '012346789'
print(num_list[:])  #make the copy give all elements
print(num_list[0:1]) #give first element 0
print(num_list[0:3]) #12
print(num_list[0:]) 
print(num_list[:-1])
print(num_list[1:5:2]) # third is difffrence

# num_list[0] = 'a'
# print(num_list)  #give error

#List To String
list_char = ['a', 'b', 'c']
print(list_char)
print(''.join(list_char))
print(', '.join(list_char))


#iterate
for char in list_char:
    print(char)

for char in list_char:
    print(char, end="")

for char in list_char:
    print(char, end=", ")

#repr vs str vs print
print(repr('python'))
print(str('python'))
print('python')