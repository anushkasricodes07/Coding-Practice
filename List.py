n = [10,20,30,5,80,25]
largest = n[0]
smallest = n[0]
for num in n:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Largest number is:", largest)
print("Smallest number is:", smallest)
