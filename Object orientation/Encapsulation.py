class AccountHolder:
    def __init__(self) -> None:
        self.bal = 10000

ah = AccountHolder()
print(ah.bal)
ah.bal = 20000
print(ah.bal)

#giving negative number and see what happens
class AccountHolder:
    def __init__(self) -> None:
        self.bal = 10000

ah = AccountHolder()
print(ah.bal)
ah.bal = -200000
print(ah.bal)


#giving the getter and setter not to access the code easily
class AccountHolder:
    def __init__(self) -> None:
        self.bal = 10000

    def get_bal(self):
        return self.bal
    
    def set_bal(self,amt):
        if amt > 0:
            self.bal = amt
        else:
            print('its invalid')

ah = AccountHolder()
print(ah.get_bal())
ah.set_bal(-20000)
print(ah.get_bal())
 

#this code is protected by the (_bal) means not to access directly
class AccountHolder():
    def __init__(self) -> None:
        self._bal = 10000

    def get_bal(self):
        self._bal

    def set_bal(self,amt):
        if amt>0:
            self._bal = amt
        else:
            print('Its invalid')

ah = AccountHolder()
print(ah.get_bal())
ah.set_bal(-20000)
print(ah.get_bal())
print(ah.__dict__) #checks if bal is stored in dictionary  


#By adding 2 underscore in front of the variable made the difference,python internally changed the__bal to _AccountHolder__bal 
# using a concept called as "Data mangling" syntax[_classname__variable] which is declared within the class


class AccountHolder:
    def __init__(self) -> None:
        self.__bal = 10000

    def get_bal(self):
        return self.__bal
    
    def set_bal(self,amt):
        if amt>0:
            self.__bal = amt
        else:
            print('its invalid')

ah = AccountHolder()
print(ah.get_bal())
ah.set_bal(29000)
print(ah.get_bal())
print(ah.__dict__)
print(ah._AccountHolder__bal) #accessing by calling _classname__variable


#Using property method
class AccountHolder:
    def __init__(self) -> None:
        self.__bal = 10000

    def get_bal(self):
        print('get_bal is called')
        return self.__bal
    
    def set_bal(self,amt):
        print('set_bal is called')
        if amt>0:
            self.__bal = amt
        else:
            print('its invalid')

    bal = property(get_bal,set_bal)

ah = AccountHolder()
print(ah.bal) #not to call __bal becausse of using property method
ah.bal = 20000
print(ah.bal)
print(ah.get_bal()) #we can call in this type also



#another way of doing this
class AccountHolder:
    def __init__(self) -> None:
        self.__bal = 10000

    @property
    def bal(self):
        print('get_bal is called')
        return self.__bal
    
    @bal.setter
    def bal(self,amt):
        print('set_bal is called')
        if amt>0:
            self.__bal = amt
        else:
            print('its invalid')


ah = AccountHolder()
print(ah.bal) #not to call __bal because of using property method
ah.bal = 20000
print(ah.bal)
