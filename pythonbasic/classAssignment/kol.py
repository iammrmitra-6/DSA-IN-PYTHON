# program to find largest and smallest in a list (without min() / max())

nums = [12, 5, 7, 25, -3, 18]

# assume first element is both smallest and largest
smallest = nums[0]
largest = nums[0]

for n in nums[1:]:
    if n < smallest:
        smallest = n
    if n > largest:
        largest = n

print("List:", nums)
print("Smallest element:", smallest)
print("Largest element:", largest)
