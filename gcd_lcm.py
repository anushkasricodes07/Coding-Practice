a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
x = a
y = b
while b != 0:
    a, b = b, a % b
    gcd = a
    lcm = (x * y) // gcd
print("GCD is:", gcd)
print("LCM is:", lcm)
