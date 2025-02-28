x = 99
def fun():
    y = 999
    print(y)
fun()
print(x)


x = 99
def fun():
    y = 999
    print(y)
print(globals)
print(locals)
fun()



x = 99
def fun():
    global x
    x = 999
    print(x)
fun()
print(x)


import re
user_data = '''bill@outlook.com 1975-11-20 MALE
elon@gmail.com 1978-05-15 MALE
messi@yahoo.com 1987/06/28 MALE'''

regex = r"(\w+)@\w{3,}.\w{2,}(\d{4}[-:/]\d{2}[-:/]\d{2})"
itr = re.finditer(regex,user_data)
for m in itr:
    name = m.group(1)
    dob = m.group(2)
    l = re.split(r"[:/-]",dob)
    print(name,"age=",2020-int(l[0]))

    