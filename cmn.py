l1 = [10,20,30,40,50]
l2 = [10,20,50,70,90]
common = []
for num in l1:
    if num in l2:
        common.append(num)
print("Common element are:", common)
