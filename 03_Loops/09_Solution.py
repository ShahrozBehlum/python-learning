<<<<<<< HEAD
items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ", item)
        break
=======
items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ", item)
        break
>>>>>>> 8e7f2e321fefce9d5ac2b428313771f58418cce2
    unique_item.add(item)