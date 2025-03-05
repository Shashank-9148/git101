#Dictionary built in methods
#.keys()=access only keys
#.values()=access only values
#.items()=access keys and values

d = {1:'c',2:'java',3:'python'} #using keys
print(list(d.keys()))
for i in d.keys():
    print(i,d[i])

d = {1:'c',2:'java',3:'python'} #using values
print(list(d.values()))
for i in d.values():
    print(i)


d = {1:'c',2:'java',3:'python'} #using items
print(tuple(d.items()))
for i in d.items():
    print(i)

