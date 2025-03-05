a = 10

if a%3==0 or a%5==0:
    print(a,"is divisible by either 3 or 5")
else:
    print(a,"is not divisible by neither 3 or 5")

a = 14
if a%3==0 or a%5==0:
    print(a,"is divisible by either 3 or 5")
else:
    print(a,"is not divisible by neither 3 or 5") 


a =14
if a%5==0 or a%7==0:
    print(a,"the number is divisible by either 7 or 5") 
else:
    print(a,"the number is not  divisible by neither 7 or 5")


a = 15
if a%2==0 or a%3==0:
    print("is divisible by either 2 or 3")
else:
    print("is not divisible by neither 2 nor 3 ")



n = int(input("enter a number\n"))
if n%2==0:
    print(n,'is even')
else:
    print(n,'is odd')