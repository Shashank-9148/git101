#diff ways of creating a list

lst = [10,[20,30,40],(50,60,70),{9,10,11},{1:'x',2:'y'}]
print(lst)
print(lst[1])
print(lst[2])
print(lst[2][2])
print(lst[4][1])

#accessing the lists using slicing
lst = [10,20,30,40,50,60,70]
print(lst[0])
print(lst[::])
print(lst[1:6:])
print(lst[-1:-4:-1])
print(lst[::-1])

#accessing the list using index order
lst = [10,20,30,40,50,60]
for i in range(0,len(lst)):
    print(lst[i])


