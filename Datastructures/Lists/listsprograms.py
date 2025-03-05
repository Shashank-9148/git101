'''#program to find sum of subsets
lst = input("Enter a list between[]\n")
lst = eval(lst)
start = int(input("Enter the start index"))
stop = int(input("Enter the stop index"))
print("sum=",sum(lst[start:stop+1]))

#program to append lists which is not present in another list
lst1 = [10,20,30,40]
lst2 = [35,20,10,15]
for i in lst2:
   if i not in lst1:
      lst1.append(i)
print(lst1)


#program to insert an element at right position within a sorted list
lst = eval(input("Enter a sorted list between []\n"))
n = int(input("Enter the value to be inserted\n"))
print(lst)

for i in range(len(lst)):
    if n<lst[i]:
        lst.insert(i,n)
        break
    print(lst)


#program to find max and min number in list
lst = [4,2,1,5,3]
print(sum(lst)-max(lst),sum(lst)-min(lst))


#program to find expression contains balanced parantheses
s = input("Enter an expression with brackets\n")
lst = []
for i in s:
    if i == '[' or i == '(' or i == '{':
        lst.append(i)
    elif i == ']' and lst [-1] == '[':
        lst.pop()
    elif i == ')' and lst [-1] == '(':
        lst.pop()
    elif i == '}' and lst [-1] == '{':
        lst.pop()
    else:
        break
    if len(lst) == 0:
        print(s,"Expression is balanced")
    else:
        print(s,"Expression is not balanced")
'''

#comparision of lists ==,<=,>=,>,!=
lst1 = [5,3,6,7]
lst2 = [3,6,7]
print(lst1 == lst2)


#program to convert lower & upper case which contains more than 5 elements
s = input("Enter a string\n")
lst = s.split()
res = []
for i in range(len(lst)):
    if len(lst[i])>5:
        res.append(lst[i]).lower()
    else:
        res.append(lst[i]).upper()
print(''.join(res))

