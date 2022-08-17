def primeFactors(num):
    c = 2
    while(num > 1):
     if(num % c == 0):
            print(c, end=" ") 
            num = num / c
    else:
            c = c + 1
num = int(input("Enter number:"))
print("Factors are:")
primeFactors(num)

 