import math
inputRadius = int(input('Enter the radius: '))

def radius_circum(num):
    radius = round(math.pi * (num**2), 2)
    circumference = round(2 * (math.pi) * num, 2) 
    return radius, circumference

r,c = radius_circum(inputRadius)
print('The radius of circle is: ',r)
print('The circumference of circle is: ',c)
