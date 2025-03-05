#using zip()
lst1 = [2,3,4,5]
lst2 = [6,7,8,9]

print(list(zip(lst1,lst2)))

#to itirate over two zips
lst1 = [2,3,4,5]
lst2 = [6,7,8,9]
for i,j in zip(lst1,lst2):
    print(i,j)


#program to concatenate two lists using zip and join function
lst1 = ['A','app','','da','kee','t','doc','a']
lst2 = ['n','le','a','y','ps','he','tor','way']
res = []
for i,j in zip(lst1,lst2):
   res.append(i+j)
print(' '.join(res))
#using list comprehension
lst1 = ['A','app','','da','kee','t','doc','a']
lst2 = ['n','le','a','y','ps','he','tor','way']
res =  [''.join(i+j) for i,j in zip(lst1,lst2) ]
print(res)


#program to convert lower & upper case which contains more than 5 elements
s = input("Enter a string\n")
lst = s.split()
res = []
for i in range(len(lst)):
    if len(lst[i])>5:
        res.append(lst[i].lower())
    else:
        res.append(lst[i].upper())
print(''.join(res))
#using list comprehension
s = input("Enter a string\n")
lst = s.split()
print(' '.join([lst[i].lower() if len(lst[i])>5 else lst[i].upper() for i in range(len(lst))]))

