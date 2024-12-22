fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print("Fruits list:", fruits)

print("First item:", fruits[0])
print("Last item:", fruits[-1])

fruits.append("fig")
print("After adding 'fig':", fruits)

fruits.remove("banana")
print("After removing 'banana':", fruits)

fruits[1] = "blueberry"
print("After changing second item to 'blueberry':", fruits)

print("Length of the list:", len(fruits))
