# Collection of different datatypes values
#order matter


list1 = ['a', 'b', 'c', 'd']
print(list1)

print(list1[1])
print(list1[-1])
copy = list1[:]
print(copy)
list1[0:2] = 'A'
print(list1)

#mutable modify original array
list1[0] = 's'
print(list1)

#Iteration
for item in list1:
    print(item)

if 'A' in list1:
    print('true')

list_copy = list1.copy()
print(list_copy)

#range()
squared_num = [x**2 for x in range(10)]
print(squared_num)

#also use these bult in method append(), pop(), remove(), insert()