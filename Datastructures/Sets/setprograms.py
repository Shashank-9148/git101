#program to take names and remove all duplicates
'''lst = input().split()
print(lst)
print(set(lst))'''

#program to print the number of duplicates in the list
lst = list(map(int,input().split()))
s = set(lst)
print(len(lst) - len(s))

#given set of roll numbers of students who play hockey,football,cricket
# 1.who play anygame
# 2.who play all games
# 3.who play only hockey
# 4.who play either football or cricket but not both

h = {1,9,12,7,14}
f = {6,9,8,10,5,11,12,13,15}
c = {2,4,9,3,5,13}
print(h|f|c) #play any game
print(h&f&c) #play all 3 game
print(h-(f|c)) #plays only hockey
print(f^c) #either football or cricket but not both


#program to print square number in set
s = {5,4,9,8,7,3}
res = set()
for i in s:
    if i%2==0:
     res.add(i**2)
    else:
       res.add(i+i)
print(res)
#using listcomprehension
s = {5,4,9,8,7,3}
res = {i**2 if i%2==0 else i+i for i in s}
print(res)


#program to print it is pangram or not
s = "The quick brown fox jumps over a lazy dog"
s = s.upper()
c = set()
for i in s:
   if ord(i) >= 65 and ord(i) <= 90:
      c.add(i)
   if len(c) == 26:
      print(s,"its pangram")
   else:
      print(s,"its not pangram")
#using listcomprehension
s = "The quick brown fox jumps over a lazy dog !"
s = s.upper()
c = {i  for i in s if ord(i)>= 65 and ord(i)<= 90 }

if len(c) == 26:
      print(s,"its pangram")
      
else:
      print(s,"its not pangram")



#program to print its a heterogram
s = "The big dwarf only jumps!".upper()
l = []

for i in s:
    if ord(i) >= 65 and ord(i) <= 90:
        l.add(i)
    c = set(l)
    if len(l) == len(c):
        print(s,"its a heterogram")
    else:
        print(s,"its not a heterogram")
#using set comprehension
s = "The big dwarf only jumps!".upper()
l = [i for i in s if ord(i) >= 65 and ord(i) <= 9 ]
c = set(l)
if len(l) == len(c):
        print(s,"its a heterogram")
else:
        print(s,"its not a heterogram")


#using frozen set
s = frozenset({2,3,1,4,5})
s1 = {5,3,6,8,9}
print(s|s1)

