#using pop 
lst = [10,20,30,40,50]
print(lst)
lst.pop()
print(lst)

lst = [10,20,30,40,50]
print(lst)
lst.pop(2)
print(lst)

#using del
lst = [1,3,4,5,6,7]
print(lst)
del lst[3]
print(lst)

#using slice
lst = [1,2,3,4,5,6,7,8,9]
print(lst)
del lst[2:6:]
print(lst)

#using slice reverse
lst = [1,2,3,4,5,6,7,8,9]
print(lst)
del lst[-2:-8:-1]
print(lst)

#using slice reverse step 2
lst = [1,2,3,4,5,6,7,8,9]
print(lst)
del lst[-1::-2]
print(lst)



