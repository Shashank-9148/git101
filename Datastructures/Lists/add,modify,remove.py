#using extend function to add elements in the end
lst = [10,20,30,40,50]
lst.append(60)
print(lst)
lst = lst + [90,100,40]
print(lst)
lst.extend([120,30,379])
print(lst)

#using insert function to modify
lst = [10,20,30,40]
print(lst)
lst.insert(3,80)
print(lst)

#To replace one single element
lst = [10,20,30,40]
print(lst)
lst[3] = 50
print(lst)

#To replace multiple characters using slicing
lst = [10,20,30,40,50]
print(lst)
lst[1:4] = [70,60,99]
print(lst)

#own method
lst = [10,20,30,40,50,70,90,99,88,78,67,57,45,35,64]
print(lst)
for i in range(0,len(lst)):
      lst[::2] = [98,97,96,95,90,89,78,67]
      print(lst)


#To remove element in list
lst = [1,2,3,4,5]
print(lst)
lst.remove(3)
print(lst)