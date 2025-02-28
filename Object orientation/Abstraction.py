from abc import ABC,abstractmethod
class VoiceAssistant(ABC):
    @abstractmethod
    def activate_assistant(self):
        pass
    @abstractmethod
    def perform_task(self):
        pass
    @abstractmethod
    def use_builtin_apps(self):
        pass

class Siri(VoiceAssistant):
    def activate_assistant(self):
        print('Hey siri,activate siri')

    def perform_task(self):
        print('Siri is performing task using apple server')

    def use_builtin_apps(self):
        print('Siri uses the built in apps of ios ')

class Alexa(VoiceAssistant):
    def activate_assistant(self):
        print('Alexa, activates Alexa')

    def perform_task(self):
        print('Alexa is performing task using amazon services')

    def use_builtin_apps(self):
        print('Alexa uses the built in apps of Fire-os')

class GoogleAssistant(VoiceAssistant):
    def activate_assistant(self):
        print('Ok google,activates GA')

    def perform_task(self):
        print('GA is performing task using google services')

    def use_builtin_apps(self):
        print('Google uses the builtin apps of android-Os')

def use_assistant(ref):
    ref.activate_assistant()
    ref.perform_task()
    ref.use_builtin_apps()

def main():
    s = Siri()
    a = Alexa()
    ga = GoogleAssistant()
    
    use_assistant(s)
    use_assistant(a)
    use_assistant(ga)

main()


#program for finding area of circle,triangle and rectangle
from math import pi
class Circle:
    def __init__(self) -> None:
        self.r = 0
        self.area = 0

    def take_input(self):
        self.r = int(input('Enter the radius: \n'))

    def find_area(self):
        self.area = pi*self.r**2

    def disp_area(self):
        print(f'circle area = {self.area}')

class Rectangle:
    def __init__(self) -> None:
        self.h = 0
        self.b = 0
        self.area = 0

    def take_input(self):
        self.h = int(input('Enter the length:\n'))
        self.b = int(input('Enter the breadth:\n'))

    def find_area(self):
        self.area = self.h*self.b

    def disp_area(self):
        print(f'Rectangle area = {self.area}')

class Triangle:
    def __init__(self) -> None:
        self.h = 0
        self.b = 0
        self.area = 0

    def take_input(Self):
        Self.h = int(input('Enter the height:\n'))
        Self.b = int(input('Enter the base:\n'))

    def find_area(self):
        self.area = (self.h*self.b)/2

    def disp_area(self):
        print(f'Triangle area = {self.area}')

def main():
    c = Circle()
    r = Rectangle()
    t = Triangle()

    c.take_input()
    c.find_area()
    c.disp_area()

    r.take_input()
    r.find_area()
    r.disp_area()

    t.take_input()
    t.find_area()
    t.disp_area()

main()

#same program using abstraction,inheritance and polymorphism
from math import pi
from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self) -> None:
        self.area = 0
    
    @abstractmethod
    def take_input(self):
        pass

    @abstractmethod
    def find_area(self):
        pass

    @abstractmethod
    def disp_area(self):
        pass

class Circle(Shape):
    def __init__(self) -> None:
        self.r = 0

    def take_input(self):
        self.r = int(input('Enter the radius: \n'))

    def find_area(self):
        self.area = pi*self.r**2

    def disp_area(self):
        print(f'circle area = {self.area}')

class Rectangle(Shape):
    def __init__(self) -> None:
        self.h = 0
        self.b = 0
        super().__init__()

    def take_input(self):
        self.h = int(input('Enter the length:\n'))
        self.b = int(input('Enter the breadth:\n'))

    def find_area(self):
        self.area = self.h*self.b

    def disp_area(self):
        print(f'Rectangle area = {self.area}')

class Triangle(Shape):
    def __init__(self) -> None:
        self.h = 0
        self.b = 0
        super().__init__()

    def take_input(Self):
        Self.h = int(input('Enter the height:\n'))
        Self.b = int(input('Enter the base:\n'))

    def find_area(self):
        self.area = (self.h*self.b)/2

    def disp_area(self):
        print(f'Triangle area = {self.area}')

def geometric_shapes(ref):
    ref.take_input()
    ref.find_area()
    ref.disp_area()

def main():
    c = Circle()
    r = Rectangle()
    t = Triangle()

    geometric_shapes(c)
    geometric_shapes(r)
    geometric_shapes(t)

main()



#another program on abstraction
from abc import ABC,abstractmethod
class FundTransfer(ABC):
    def __init__(self,account_number,balance) -> None:
        self.__account_number = account_number
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number
    
    @account_number.setter
    def account_number(self,account_number):
        if len(str(account_number)) == 10:
            self.__account_number = account_number

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,balance):
        if balance > 0:
            self.__balance = balance

    def validate(self,amount):
        return len(str(self.account_number)) == 10 and amount < self.__balance and amount > 0
    
    @abstractmethod
    def transfer(self,amount):
        pass

class NEFTTransfer(FundTransfer):
    def __init__(self, account_number, balance) -> None:
        super().__init__(account_number, balance)

    def transfer(self,amount):
        sc = amount * 0.05
        if (amount + sc) < self.balance:
            self.balance = self.balance - (amount + sc)
            return True
        return False
    
class IMPSTransfer(FundTransfer):
    def __init__(self, account_number, balance) -> None:
        super().__init__(account_number, balance)

    def transfer(self,amount):
        sc = amount * 0.02
        if (amount + sc) < self.balance:
            self.balance = self.balance - (amount + sc)
            return True
        return False
    
class RTGSTransfer(FundTransfer):
    def __init__(self, account_number, balance) -> None:
        super().__init__(account_number, balance)

    def transfer(self,amount):
        if amount < self.balance and amount >= 10000:
            self.balance = self.balance - amount
            return True
        return False
    
def main():
    an = int(input('Enter your account number:\n'))
    bal = int(input('Enter your account balance:\n'))

    print('Enter your choice')
    print('1:NEFT\n 2:IMPS\n 3:RTGS\n')
    choice = int(input())
        

    if choice == 1:
        ref = NEFTTransfer(an,bal)

    elif choice == 2:
        ref = IMPSTransfer(an,bal)

    elif choice == 3:
        ref = RTGSTransfer(an,bal)

    else:
        print('INVALID CHOICE')

    amt = int(input("Enter the amount to be transferred:"))

    if ref.validate(amt):
        if ref.transfer(amt):
            print('Transfer occured successfully')
            print(f'Remaining balance is {ref.balance}')

        else:
            print('Transfer could not be made')

    else:
        print('Account number or transfer amount seems to be wrong')

if __name__ == '__main__':
    main()

             