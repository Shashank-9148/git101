lst = [10,12,13,15,17,19,20]

def fun(x):
    if x%2==0:
        return True
    else:
        return False
evn_lst = list(filter(fun,lst))
print(evn_lst)


lst = [10,12,13,15,17,19,20]
def fun(x):
    if x%2==0:
        return False
    else:
        return True
odd_lst = list(filter(fun,lst))
print(odd_lst)

evn_lst = list(filter(lambda x : x%2==0,lst))
print(evn_lst)

odd_lst = list(filter(lambda x : x%2!=0,lst))
print(odd_lst)


lst = [12,13,14,15,16,17]

def even_lst(n):
    if n%2==0:
        return True
    else:
        return False
even_lst = list(filter(lambda n : n%2==0,lst))
print(even_lst)
    

lst = [1,2,3,4,5,6]
def fun(x):
    if x%3==0:
        return True
    else:
        return False
fun = list(filter(fun,lst))
print(fun) 
fun = list(filter(lambda x:x%3==0,lst))
print(fun)




