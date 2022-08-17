n = int(input("Enter the value of n: "))
a = int(input("Enter the value of a: "))
d = int(input("Enter the value of d: "))

for i in range(1, n+1):
    value = 1/(a + (i - 1) * d)
    print(value, end=" ")