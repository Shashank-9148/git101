#program for printing a zero element and a non zero element without using decorator
def outer(ref):
    def wrapper(lst):
        if 0 in lst:
            print('0 is present')
        else:
            ref(lst)
    return wrapper

def get_product(lst):
    p = 1
    for i in lst:
        p *= i
        print(p)

mod_get_product = outer(get_product)
mod_get_product([10,20,30])
mod_get_product([10,0,30])


#program using decorator
def outer(ref):
    def wrapper(lst):
        if 0 in lst:
            print('0 is present')
        else:
            ref(lst)
    return wrapper

@outer   #decorator
def get_product(lst):
    p = 1
    for i in lst:
        p *= i
        print(p)

get_product([10,20,30])
get_product([10,0,30])


#using decorator division program
def outer(ref):
    def wrapper(a,b):
        if b == 0 :
            print("please provide a non zero element")
        else:
            ref(a,b)
    return wrapper

@outer   #decorator
def div(a,b):
    print(a/b)
div(10,2)
div(10,0)

#program to print the square of a numbers and its product
def decorator(num):

    def power_of(ref):
        
        def wrapper(lst):
            lst = list(map(lambda x:x**num ,lst))
            ref(lst)
        return wrapper
    return power_of

@decorator(198)
def get_product(lst):
    p = 1
    for i in lst:
        p *= i
        print(p)

#fun1 = decorator(2)
#mod_get_product = fun1(get_product)
#mod_get_product([1,2,3,4,5])
get_product([1,2,3,4,5])



#Closures
def outer():
    z = 99

    def inner():
        print(z)
    return inner

fun = outer()
fun()
del outer
outer()

#closure
def outer():
    x = 99

    def inner1():
     y= 98

     def inner2():
      print(x)
      print(y)
     return inner2
    return inner1
    
fun1 = outer()
fun2 = fun1()
fun2()
del outer
del fun1 
fun2()