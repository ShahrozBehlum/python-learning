import math
import random

print(1*2+1)

print(math.floor(3.44))
print(math.ceil(3.44))
print(math.trunc(3.44))

myList = [1,2,3,4]

print(random.random())
print(random.randint(1,10))
print(random.choice(myList))
random.shuffle(myList)
print(myList)

print((0.1+0.1+0.1)-0.3) #it give not exactly value
#use this 
from decimal import Decimal  #same for fraction
print((Decimal('0.1') + Decimal('0.1') + Decimal('0.1')) - Decimal('0.3'))
