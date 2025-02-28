s = "hello" + "world"
print(s)


s1 = "hello"
print(s1)
s2 =s1 + "world"
print(s2)

s1 = "hello"
print(s1)
s1 = s1 + "world"
print(s1)

#program for converting small letters to caps using concatenation

#c = 'a'
#print(ord(c))

#c = 'a'
#print(chr(ord(c)))



s = input("enter a string\n")#type1
s_upper = ""

for i in s:
    if ord(i) >= 97 and ord(i) <= 122:
        s_upper += chr(ord(i)-32)
    else:
        s_upper += i
print(s)
print(s_upper)


s = input("enter a string\n")#type 2
s_upper = s.upper() 
print(s_upper)


s = input("enter a string\n")
s_lower = s.lower()
print(s_lower)


#program to concatinate more strings type1
lst = ['java','python','django','springs']
s =""
for i in lst:
    s += i
print(s)

#type2
lst = ['java','python','django','springs']
s = "".join(lst)
print(s)