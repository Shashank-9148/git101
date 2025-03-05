d = {1:'c',2:'java',3:'python'}
print(d)
d[4] = 'c++' #adding element to dictionary
print(d)
d.update({5:'c#',6:'visual basics'}) #updating multiple elements
print(d)
d.update(seven='javascript',eight='php') #updating multiple elements in another type
print(d)
d[2] = 'python' #modifying element
print(d)

#To delete items using(pop(),popitem(),del)
d = {1:'p',2:'y',3:'x',4:'u',5:'o',6:'h'}
print(d)
d.pop(3)
print(d)
d.popitem()
print(d)
del d[5]
print(d)
d.clear()
print(d)

#simple program
d = {1:'a',2:[1,2,3]}
print(d[1])
x = d[1]
print(x)
x = 'b'
print(d[1])
print(x)
lst = d[2]
print(lst)
lst.append(4)
print(d[2])
print(lst)
