#collection of key value-pair
#order doesn't matter

dict1 = {'1':'m', '2':'b', '3':'c', '4':'d'}
print(dict1)

print(dict1['1'])  #pass key for access value

# dict is mutable
dict1['4'] = 'z'
print(dict1)

#methods get(), len(), pop(), clear()

#Iteration
for item in dict1:
    print(item)  #it print only keys
for item in dict1:
    print(item, dict1[item])  #it print both
#OR
for key,value in dict1.items():
    print(key, value) 

if 'm' in dict1:
    print('ture')         
else:
    print('false')    