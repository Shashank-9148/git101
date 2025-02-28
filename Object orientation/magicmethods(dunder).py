#important dunder methods
# __init__
#__new__
#__repr__
#__add__
#__sub__
#__mul__
#__div__
#__pow__
#__eq__
#__ne__
#__it__
#__gt__
#__le__
#__ge__

def main():
    a = 5
    print(a)
    a = a+5 #a.__add__(5)  executes in the following manner __add__(self,other)
    print(a)

if __name__ == '__main__':
    main()

#using magic method
def main():
    a = 5
    print(a)
    a = a.__add__(6)
    print(a)

if __name__ == '__main__':
    main()


#example of concatenation
def main():
    s = 'pyt'
    print(s)
    s = s + 'hon'     #s = s.__add__('hon') we can execute in this type also 
    print(s)

if __name__ == '__main__':
    main()




#concept operator overloading
class point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def display(self):
        print(self.__dict__)

def main():
    p1 = point(2,3)
    p2 = point(1,1)
    p1.display()
    p2.display()

if __name__ == '__main__':
    main()
        

#now we can get the third point which will be the added result of two points
class point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def __add__(self,other): #this is the user defined method
        return point(self.x + other.x,self.y + other.y)
    
    def display(self):
        print(self.__dict__)

def main():
    p1 = point(2,3)
    p2 = point(1,1)
    p3 = p1 + p2  #we can access this only by creating user defined method that is (p1.__add__(p2))
    p3.display()

if __name__ == '__main__':
    main()       
