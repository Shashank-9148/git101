


'''def collect_student_data(Name,**data):
    print(Name)
    print(data)
    collect_student_data(Name ="vedamurthy",Age=56,Work = "Retaired lecturer",Place="Tiptur" )'''


def add(a,b):
    c = a+b
    return c
res = add(2,3)
print(res)



def power_of(a,b):
    c = a**b
    return c
res = power_of(2,3)
print(res)


def power_of(a,b=8):
    c = a**b
    return c
res = power_of(a = 7)
print(res)
    

def power_of(a,b):
    c = a**b
    return c
res = power_of(a = 3,b=4)
print(res)


def get_student_data(Name,crust,**data):
    print(Name)
    print(data)
    print(crust)
    print(type(data))
get_student_data(Name="Vedamurthy",Age=57,Proffession="Retaired",Place="Tiptur",crust="Sonsurya")