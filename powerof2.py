def check(n):
   if (n == 0):
      return False
   while (n != 1):
      if (n % 2 != 0):
         return False
      n = n / 2
   return True
if(check(int(input("Enter number:")))):
   print('Yes,power of two')
else:
   print('No,not power of two')