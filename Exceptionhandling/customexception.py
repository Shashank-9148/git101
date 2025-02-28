class InvalidMobileNumberError(Exception):
    pass

def validate(mob):
    if len(mob) == 10:
        print('valid mobile number')
    else:
        raise InvalidMobileNumberError('Enter 10 digit mobile number')
    
def main():
    mob = input()
    validate(mob)
main()


#Example 2
class ItemNotInMenu(Exception):
    pass

def menu(item):
    if item == 'pizza':
        print('enjoy your pizza')
    elif item == 'idly':
        print('enjoy your idly')
    elif item == 'burger':
        print('enjoy your burger')
    elif item == 'rotti':
        print('enjoy your rotti')
    else:
        raise ItemNotInMenu('Item not present in menu')
    
def main():
    item = input()
    try:
        menu(item)
    except ItemNotInMenu as e:
        print(e)
      
main()


#let us take  an example of creating an account an account.when will check if the username is unique and password satisfying the condition
class DuplicateUserError(Exception):
    pass
class WeakPasswordError(Exception):
    pass

class User:
    User_name = set()
    def __init__(self,un,mob,pwd) -> None:
        self.un = un
        self.mob = mob
        self.pwd = pwd

    def add_user(self):
        if self.un in User.User_name:
            raise DuplicateUserError('username already exists')
        else:
            User.User_name.add(self.un)

    def validate(self):
        uc=lc=num=sp=0
        for i in self.pwd:
            if i.isupper():
                uc += 1
            elif i.islower():
                lc += 1
            elif i.isdigit():
                num += 1
            else:
                sp += 1

        if len(self.pwd)<6 or uc==0 or lc==0 or num==0 or sp==0:
            raise WeakPasswordError('password not strong enough')
        
def main():
    un = input('Enter the username')
    mob = int(input('Enter mobile number'))
    pwd = input('Enter password')

    try:
        u1 = User(un,mob,pwd)
        u2 = User(un,mob,pwd)

    except DuplicateUserError as e:
        print(e)
    except WeakPasswordError as e:
        print(e)
    except:
        print('Hey some issue occured')
    else:
        print('Account created successfully')

main()

        