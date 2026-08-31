# Creating an array (list)
arr = [10, 20, 30, 40]

print("Original Array:", arr)

# i. insert() -> Insert element at specific position
arr.insert(2, 25)   # Insert 25 at index 2
print("After insert(2, 25):", arr)

# ii. remove() -> Remove specific element
arr.remove(20)      # Remove element 20
print("After remove(20):", arr)

# iii. append() -> Add element at the end
arr.append(50)      # Add 50 at end
print("After append(50):", arr)

# iv. extend() -> Add multiple elements
arr.extend([60, 70, 80])   # Add multiple elements
print("After extend([60, 70, 80]):", arr) 