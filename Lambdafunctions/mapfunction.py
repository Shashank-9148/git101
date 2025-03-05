lst = [1,2,3,4,5]
def fun(x):
    return x**2
sq_lst = list(map(fun,lst))
print(sq_lst)

sq_lst = list(map(lambda x : x**2,lst))
print(sq_lst)