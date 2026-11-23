numbers = [10,20,30,55,40,60]
target = int(input("Enter the element to search: "))
for i in range(len(numbers)):
    if numbers[i] == target:
        print("Element found at index:", i)
        found = True
if not found:
    print("Element not found")