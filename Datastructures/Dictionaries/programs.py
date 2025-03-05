#program to count the occurance of each character in the given string
s = input("enter a string\n").upper()
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
        print(d)
for i in d:
    if d[i] >= 3:
      print(i)


#program to  count the total number of pairs
lst = map(int,input().split())
d = {}
for i in lst:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

res = 0
for i in d.values():
    res += i//2 
print(res) 

#program to print the mobile number associated with name,if the name is not among the entry display'contact not found'
n = int(input())
d = {}
for i in range(n):
    l = input().split()
    d[l[0]].lower() = l[1]

s = int(input())
for i in range(s):
    name = input().lower()
    if name in d:
        print('mob:',d[name])
    
    else:
        print("contact not found")

#program to print the kth non-repeating character in the given string
lst = input()
k = int(input())
d = {}

for i in lst:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
    count = 0
for i in d:
    if d[i] == 1:
        count += 1
    if k == count :
        print(i)
        break

#program to count the occurance of each word in the given sentence
import re
s = input().upper()
s = re.sub(r'[,.!?]','',s)
lst = s.split()
d = {}
for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in d:
    if d[i] >= 3:
        print(i)

#program to print the highest marks of every persons
lst = input().split(',')
d = {}
for i in lst:
    t = i.split()
    if t[0] not in d:
        d[t[0]] = t[1]
    else:
        if t[1] > d[t[0]]:
            d[t[0]] = t[1]
            print(d)

#program to inverse the dictionary in such a way keys becomes values and values becomes keys
d = {1:'A',2:'B',3:'A',4:'B',5:'B',6:'C'}
res = {}
for i in d:
    if d[i] not in res:
        res[d[i]] = []
        res[d[i]].append(i)
    else:
        res[d[i]].append(i)
    print(res)

#program that splits the sentence and arrange them into descending order based on their length and then on their chronological order
lst = input().lower().split()
d = {}
for i  in lst:
    if len(i) not in d:
        d[len(i)] = []
        d[len(i)].append(i)
    else:
        d[len(i)].append(i)
    
s_d = sorted(d.keys(),reverse = True)
for i in s_d:
    for j in sorted(d[i]):
        print(j)

#program to print key and value 
lst = input().split()
d = {i:len(i) for i in lst}#using comprehension
for i in lst:
    d[i] = len[i]
print(i)

#program to print the key values even as squares and odd values as cubes
lst = [1,2,3,4,5,6,7,8,9]
d = {i:(i**2 if i%2==0 else i**3)for i in lst}
for i in lst:
    if i%2 == 0:
        d[i] = i**2
    else:
        d[i] = i**3
    print(d) 
