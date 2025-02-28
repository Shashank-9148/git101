def power_of(num,p):
    return num**p
res = power_of(3,4)
print(res)


def power_of(num,p):
    return num**p
res = (lambda num,p : num**p) (3,2)
print(res)

def get_quotient(num,den):
    return num/den
res = get_quotient(200,20)
print(res)


def get_quotient(num,den):
    return num/den
res =(lambda num,den : num/den) (10,2)
print(res)


def power_of(num,p):
    return num**p
fun = lambda num,p : num**p
res = fun(10,2)
print(res)
 
res1 = fun(100,1)
print(res1)



def get_quotient(num,den):
    return num/den
fun = lambda num,den : num/den
res = fun (200,5)
print(res)

res1 = fun(300,5)
print(res1)



def mul(x,y):
   c = x*y
   return c
res = (lambda x,y:x*y)(2,3)
print(res) 




#program using lambda function
def fun1(num):
    return lambda  x : x*num
res = fun1(3)(2)
print(res)

fun2 = fun1(3)
print(fun2(4))

#2
def fun1(num):
    return lambda x : num+x
res = fun1(3)(5)
print(res)

fun2 = fun1(3)
print(fun2(4))


#3
def fun1(num):
    return lambda x : num*x
res = fun1(20)(2)
print(res)
fun2 = fun1(20)
print(fun2(4))

#3
def fun1(num):
    return lambda x : num*x
num = int(input("Enter a number\n"))

math_table = fun1(num)
for i in range(1,11):
    print(num,"X",i,"=",math_table(i))