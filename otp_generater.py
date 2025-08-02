import random

def otp_generator():
   n = int(input("Enter digit of otp :  "))
   lower = 10**(n-1)
   greater = (10**n )- 1
   otp = random.randint(lower,greater)
   print(otp)




otp_generator()
   
