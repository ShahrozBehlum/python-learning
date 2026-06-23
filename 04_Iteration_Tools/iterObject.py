myList = [1,2,3,4]

# I = iter(myList)
# print(I)
# print(I.__next__())
# print(I.__next__())
# print(I.__next__())
# print(I.__next__())
# print(I.__next__())

#Files have bydefault iter object
f = open('script.py')
print(iter(f) is f)  #True  only for file

#give false for list, range, dict
print(iter(myList) is myList) #False