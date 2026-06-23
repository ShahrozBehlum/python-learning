# 1️⃣ count() — Infinite counter
from itertools import count

for i in count(1):
    if i == 5:
        break
    print(i)

# 2️⃣ cycle() — Repeat elements forever
from itertools import cycle

colors = ["red", "green", "blue"]

for c in cycle(colors):
    print(c)
    break

# 3️⃣ repeat() — Repeat a value
from itertools import repeat

for x in repeat("Hi", 3):
    print(x)

# 4️⃣ chain() — Combine iterables
from itertools import chain

a = [1, 2]
b = [3, 4]

print(list(chain(a, b)))

# 5️⃣ zip_longest() — Zip uneven iterables
from itertools import zip_longest

a = [1, 2]
b = [3, 4, 5]

print(list(zip_longest(a, b, fillvalue=0)))

# 6️⃣ enumerate() — Index + value (very common)
names = ["Ali", "Ahmed", "Sara"]

for index, name in enumerate(names):
    print(index, name)

# 7️⃣ map() — Apply function to each item
nums = [1, 2, 3]

squares = map(lambda x: x*x, nums)
print(list(squares))

# 8️⃣ filter() — Filter values
nums = [1, 2, 3, 4]

even = filter(lambda x: x % 2 == 0, nums)
print(list(even))