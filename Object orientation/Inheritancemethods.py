#Different methods in inheritance
#Inherited method - code reusability
#overridden method - method customization
#specialized method - adds new features

class Messenger:
    def send_message(self):
        print('Text message is sent')

    def receive_message(self):
        print('Text message is received')

class InternalMesssenger(Messenger):
    pass

class WhatsappMessenger(InternalMesssenger):
    def send_message(self):
        print('Text,photos,videos and files is sent')

    def receive_message(self):
        print('Text,photos,videos and files is received')

    def set_dp(self):
        print('Dp is set')

    def set_status(self):
        print('Status is set')

im = InternalMesssenger()
im.send_message()
im.receive_message()

wm = WhatsappMessenger()
wm.send_message()
wm.receive_message()
wm.set_dp()
wm.set_status()    


#using Super()
class customer:
    def __init__(self,name,ph,email) -> None:
        self.name = name
        self.ph = ph
        self.email = email

class platinumCustomer(customer):
    def __init__(self, name, ph, email,plat_id) -> None:
        super().__init__(name, ph, email)
        self.plat_id = plat_id
        
    def display(self):
        print(self.__dict__)

def main():
    p = platinumCustomer('Shashank',987655434,'shashanklokesh2001@gmail.com',10)
    p.display()

if __name__ == '__main__':
  main()


#we can also call any other method of parent class using super()
class customer:
    def __init__(self,name,addr,ph) -> None:
        self.name = name
        self.addr = addr
        self.ph = ph

    def place_order(self,dish):
        cost = 0
        del_charges = 50
        if dish == 'pizza':
            cost = 500 + del_charges
        else:
            cost = 250 + del_charges
        return cost
        
class platinumcustomer(customer):
    def __init__(self, name, addr, ph,plat_id) -> None:
        super().__init__(name, addr, ph)
        self.plat_id = plat_id

    def place_order(self, dish):
        del_charge = 50
        return (super().place_order(dish) - del_charge) * 0.95 
    
def main():
 p = platinumcustomer('Shashank','Tiptur',9148343924,989)
 print(p.place_order('pizza'))
if __name__ == '__main__':
    main()
        

#Extending built in classes
class ContactList(list):
    def display_all_contacts(self):
        for i in self:
            i.display()

    def search_contact(self,name):
        for i in self:
            if i.name == name:
                return 'contact found'
        return 'contact not found'
        
class contact:
    all_contacts = ContactList()
    def __init__(self,name,email) -> None:
        self.name = name
        self.email = email
        contact.all_contacts.append(self)

    def display(self):
        print(self.__dict__)

def main():
    c1 = contact('Rohit','rohit@gmail.com')
    c2 = contact('manish','manish@gmail.com')

    contact.all_contacts.display_all_contacts()
    print(contact.all_contacts.search_contact())

if __name__ == '__main__':
    main()        