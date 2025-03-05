from functools import reduce
lst = [1,2,3,4,5]
def fun(x,y):
    return x+y
res = reduce(fun,lst)
print(res)

res = reduce(lambda x,y : x+y,lst)
print(res)


res = reduce(lambda x,y : x*y,lst)
print(res)


from functools import reduce
lst = [20,30,40,50,60]
def fun(x,y):
    return x+y
res = reduce(lambda x,y : x+y,lst)
print(res)
    

from functools import reduce
lst = [2,3,5,7,9,4]
def fun(x,y):
    return x+y
fun = reduce(fun,lst)
print(fun)

fun = reduce(lambda x,y : x+y,lst)
print(fun)


    