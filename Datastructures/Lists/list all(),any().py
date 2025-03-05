'''#using all() & any() function:
lst = [10,20,30,40,50]
print(all(i>0 for i in lst))
print(any(i>0 for i in lst))

lst = [10,20,-30,40,50]
print(all(i>0 for i in lst))
print(any(i>0 for i in lst))


lst = [-10,20,-30,-40,-50]
print(all(i>0 for i in lst))
print(any(i>0 for i in lst))'''


#program to find all() function is true or false in the list:
lst = [30,45,95,85,80]
print(all([i>35 for i in lst]))


#program to find any() function is true or false in the list:
lst = [30,45,95,85,80]
print(any([i>75 for i in lst]))

