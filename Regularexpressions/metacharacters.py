#program to find each every character(.)
import re
text = 'bengaluru is cool.'
regex = r'.'
match = re.findall(regex,text)
print(match)



#program to find only character(\)
import re
text = 'bengaluru is cool\.'
regex = r'\.'
match = re.findall(regex,text)
print(match)



#program using (|) character
import re 
text = "bengaluru is cool."
regex = r"bengaluru|cool"
l = re.findall(regex,text)
print(l)


#program using (*) character
import re
text = "whole world is hole wwwhole"
regex = r"w*hole"
l = re.findall(regex,text)
print(l)


#program using (?) character
import re
text = "whole world is hole wwwhole"
regex = r"w?hole"
l = re.findall(regex,text)
print(l)


#program using (+) character
import re
text = "whole world is hole wwwhole"
regex = r"w+hole"
l = re.findall(regex,text)
print(l)

#simpleprogram
import re
text = "I know that no one is there in the school now"
regex = r"k?now?"
l = re.findall(regex,text)
print(l)
print("number of occurances =",len(l))


#program using {} character
import re
text = "gogle google gooogle goooogle gooooogle gooooooogle"
regex = r"go{1,5}gle"
l = re.findall(regex,text)
print(l)
print("number of occurances=",len(l))


#program using (^) character
import re
text = "python has nothing to do with snake python"
regex = r"^python"
l = re.findall(regex,text)
print(l)



#program using ($) character

import re
text = "python has nothing to do with snake"
regex = r"snake$"
l = re.findall(regex,text)
print(l)



#program using [] character class meta character
import re
text = "python java ai data science"
regex = r"[aeiou]"
l = re.findall(regex,text)
print(l)
print("number of occurances =",len(l))

#type2
import re
text = "python java ai data science"
regex = r"[^aeiou]"
l = re.findall(regex,text)
print(l)
print("number of occurances =",len(l))


#program using (\w) character
import re
text = "My name is ROHIT and this is my number:9353667799"
regex = "\w"
l = re.findall(regex,text)
print(l)
print("number of occurances =",len(l))



#program using (\W) character
import re
text = "My name is ROHIT and this is my number:9353667799"
regex = "\W"
l = re.findall(regex,text)
print(l)
print("number of occurances =",len(l))



#program using (\b) character
import re
text = "abcpqrxyz,pqrxyzabc,pqrabcxyz,abc"
regex = r"\babc\b"
l = re.findall(regex,text)
print(l)



#program using (\B) character
import re
text = "abcpqrxyz,pqrxyzabc,pqrabcxyz,abc"
regex = r"\Babc"
match = re.search(regex,text)
print(match)


#program using (+) character
import re
text = "python is the best language"
regex = r"[a-zA-z]+"
match = re.search(regex,text)
print(match)
print(match.group())


#program using ($) character
import re
text = "python is the best language"
regex = r"[a-zA-z]+$"
match = re.search(regex,text)
print(match)
print(match.group())


#program for finding exactly 4 characters \b[a-zA-Z]{4}\b
import re
text = " bengaluru is cool and warm"
regex = r"\b[a-zA-Z]{4}\b"
l = re.findall(regex,text)
print(l)


#program to find gmail address
import re
text = "rohit@gmail.com,rohit_@gmail.com,rohit123$_@gmail.com,rohit@yahoo.com"
regex = r"[a-zA-Z0-9$_]+@[a-zA-Z]+.com"
l = re.findall(regex,text)
print(l)


#program to find the grouping in regular expression

import re
text = "rohit@gmail.com,rohit@@gmail.com,rohit_xyz@gmail.com,roh?>gmail.com,rohit-123@gmail.com,rohit@yahoo.com,rohit@outlook.com,rohit@hotmail.com"
regex = r"([a-zA-Z0-9_$>@?\-]+)@([a-zA-Z]+.com)"
itr = re.finditer(regex,text)
for i in itr:
    print(i.group(0))
    print(i.group(1))
    print(i.group(2))


#program to substitue a regular expression
import re
text = "rohit@gmail.com,rohit@@gmail.com,rohitxyz@gmail.com,rohit@yahoo.com,rohit@outlook.com"
regex = r"@[a-zA-Z]+.com"
s = re.subn(regex,"@rooman.com",text)
print(s)


#program to print the name and age
import re
user_data = "bill@outlook.com 1975-11-20 MALEelon@gmail.com 1978-05-15 MALEmessi@yahoo.com 1987/06/28 MALE"

regex = r"(\w+)@\w{3,}.\w{2,}(\d{4}[-:/]\d{2}[-:/]\d{2})"
itr = re.finditer(regex,user_data)
for m in itr:
    name = m.group(1)
    dob = m.group(2)
    l = re.split(r"[:/-]",dob)
    print(name,"age=",2020-int(l[0]))

