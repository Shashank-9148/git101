#copying type 1
lst = [1,2,3,4,5]
lst1 = lst[:]
print(lst)
print(lst1)
print(lst is lst1)

#copying type 2
lst = [1,2,3,4,5,6]
lst1 = list(lst)
print(lst)
print(lst1)
print (lst is lst1)

#nested copy,shallow copy
lst = [[1,2],[3,4]]
lst1 = list(lst)
print(lst)
print(lst1)
lst.append([5,7])
print(lst)
print(lst1)
lst[1][0] = 30
print(lst)
print(lst1)
print(id(lst))
print(id(lst1))
print(lst is lst1)

#Deep copy
import copy
lst = [[1,2],[3,4]]
lst1 = copy.deepcopy(lst)
print(lst)
print(lst1)
lst.append([5,6])
print(lst)
print(lst1)
lst[1][0] = 30
print(lst)
print(lst1)

