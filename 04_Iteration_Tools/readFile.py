f = open('script.py')
# print(f.readline()) # read each line at a time
# print(f.readline())
# print(f.readline())
# print(f.readline())

# print(f.__next__())  # Same as readline() but it don't handle exception

# for line in f:
#     print(line, end='')  #loop the file it will read the file at a time

# while True:
#     line = f.readline()
#     if not line: break
#     print(line, end="")

# print(f.read(), end="")  # Also can read file by sung read() method 

#not 
test = True
if not test:
    print('Malik') #print nothing

test = False
if not test:
    print('Malik')    
