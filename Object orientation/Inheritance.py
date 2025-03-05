#single inheritance

class alpha:
    def fun(self):
        print('Alpha class fun()')

class beta(alpha):
    pass

b = beta()
b.fun()


#Multilevel inheritance

class alpha:
    def fun1(self):
        print('Inside alpha fun1()')

class beta(alpha):
    def fun2(self):
        print('Inside beta fun2()')

class gamma(beta):
    pass

b = gamma()
b.fun1()
b.fun2()


#Multiple Inheritance
class alpha:
    def fun1(self):
        print('Alpha class fun1()')

class beta:
    def fun2(self):
        print('Beta class fun2()')

class gamma(alpha,beta):
    pass

c = gamma()
c.fun1()
c.fun2()


#using super() in multilevel inheritance
class a:
    def fun(self):
        print('a')

class b(a):
    def fun(self):
        print('b')

class c(c):
    def fun(self):
        super().fun() #super(c,self).fun() if we want to access 'B' level inheritance in super()
        print(c)

d = c()
d.fun()


#using super() in multiple inheritance
class a:
    def fun(self):
        print('a')

class b:
    def fun(self):
        print('b')

class c:
    def fun(self):
        super().fun()
        print('c')

x = c()
x.fun()

