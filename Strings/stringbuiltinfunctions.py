#program for strings of same letters starts with https
url = ["https://www.google.com/","https://www.youtube.com/","http://www.xyz.com","http://www.abc.org"]
for i in url:
    if i[0:5:] == 'https':
        print(i)


#using built in function
url = ["https://www.google.com/","https://www.youtube.com/","http://www.xyz.com","http://www.abc.org"]
for i in url:
    if i.startswith("https"):
        print(i)


#program to concatinate different strings
lst = ["java","python","django","springs"]
s = ""
for i in lst:
    s += i
print(s)


#using built in function
lst = ["java","python","django","springs"]
s = "".join(lst)
print(s)


#program for strings end with com
url = ["https://www.google.com/","https://www.youtube.com/","http://www.xyz.com","http://www.abc.org"]
for i in url:
    if i[len(i)-3::] == "com" or i[len(i)-4::] == "com/":
        print(i)


#using built in function
url = ["https://www.google.com/","https://www.youtube.com/","http://www.xyz.com","http://www.abc.org"]
for i in url:
    if i.endswith(("com","com/")):
        print(i)