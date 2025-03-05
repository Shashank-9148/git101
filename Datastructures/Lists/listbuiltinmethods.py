#using built in methods
#using count,index method

lst = [10,20,30,40,50,20]
print(lst.count(20))
print(lst.index(30))
print(lst.index(50,2,6))

#using clear method
lst = [10,20,30,40]
print(lst)
lst.clear()
print(lst)


#using sorted or sort method
lst = [7,15,13,24,21,25,30]
print(lst)
lst = sorted(lst)
print(lst)
lst = sorted(lst,reverse = True)
print(lst)


lst = [7,15,13,24,21,25,30]
print(lst)
lst.sort()
print(lst)
lst.sort(reverse = True)
print(lst)


#using reverse method
lst = [10,20,30,40,50]
print(lst)
lst = list(reversed(lst))
print(lst)

lst = [10,20,30,40,50]
lst.reverse()
print(lst)
