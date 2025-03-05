#To define a car class and its instance variable and instance methods

class car:   #creating class
    def __init__(self):  
        self.brand = 'BMW'  #creating instance variables
        self.cc = '2100'    #creating instance variables
        self.color = 'Blue' #creating instance variables

    def start_engine(self):
         print(self.brand,'engine is starting')   #creating instance methods
    
    def shift_gear(self):
         print(self.brand,'gear is shifting')     #creating instance variables

    def accelerate(self):
         print(self.brand,'car is accelerating')  #creating instance variables

def main():
    c1 = car()
    print(c1.brand)
    print(c1.cc)
    print(c1.color)
    c1.start_engine()
    c1.shift_gear()
    c1.accelerate()

if __name__ == '__main__':
        main()
    

#To create aeroplane class
class aeroplane:

    def __init__(self):
        self.company = 'Boeing 777'
        self.capacity = 500
        self.destination = 'New York'
    
    def aeroplane_engine(self):
        print(self.company,'Its a powerful engine')

    def aeroplane_pilots(self):
        print(self.company,'Pilots are 4 in numbers')

    def aeroplane_business_class(self):
        print(self.company,'Its having Premium economy and Business Class Suite')

def main():
    a1 = aeroplane()
    print(a1.company)
    print(a1.capacity)
    print(a1.destination)
    a1.aeroplane_engine()
    a1.aeroplane_pilots()
    a1.aeroplane_business_class()

if __name__ == '__main__':
    main()


# Define a class called Car
class Car:
    # Constructor (__init__) to initialize the object
    def __init__(self, make, model, color):
        self.make = make        # Attribute to store the make of the car
        self.model = model      # Attribute to store the model of the car
        self.color = color      # Attribute to store the color of the car
        self.speed = 0          # Default speed is 0

    # Method to start the car
    def start(self):
        print(f"The {self.color} {self.make} {self.model} is now started.")

    # Method to accelerate the car
    def accelerate(self, increment):
        self.speed += increment
        print(f"The car is now going {self.speed} km/h.")

    # Method to stop the car
    def stop(self):
        self.speed = 0
        print(f"The {self.color} {self.make} {self.model} has stopped.")

    # Method to display car details
    def display_info(self):
        print(f"{self.make} {self.model} ({self.color}), Speed: {self.speed} km/h")

# Create an object (instance) of the Car class
my_car = Car("Tesla", "Model S", "Red")

# Accessing methods and attributes of the object
my_car.start()               # Output: The Red Tesla Model S is now started.
my_car.accelerate(5)        # Output: The car is now going 50 km/h.
my_car.display_info()        # Output: Tesla Model S (Red), Speed: 50 km/h
my_car.stop()                # Output: The Red Tesla Model S has stopped.'''


#creating class dominos pizza
class dominos:
    def __init__(self) :
        self.pizza1 = 'Cheese and capsicum'
        self.pizza2 = 'Corn Pizza'
        self.pizza3 = 'Butter and veggies'

    def pizza_amount1(self):
        print(self.pizza1 ,'= $199')

    def pizza_amount2(self):
        print(self.pizza2 ,'= $99 ')

    def pizza_amount3(self):
        print(self.pizza3,'= $399')


def main():
     d1 = dominos()
     print(d1.pizza1)
     print(d1.pizza2)
     print(d1.pizza3)
     d1.pizza_amount1()
     d1.pizza_amount2()
     d1.pizza_amount3()

if __name__ == '__main__':
    main()



#creating class company
class company():
    def __init__(self):
        self.companyname = 'Harman'
        self.Noofemployees = '1K'
        self.cafeteria = 'Nescafe'

    def company_location(self):
        print(self.companyname,'is in whitefield')

    def company_salary(self):
        print(self.companyname,'giving $30000 per annum')

    def company_cafeteria(self):
        print(self.cafeteria,'coffee is available from 9am to 9pm')

    def company_opening(self):
        print(self.companyname,'opens Monday-9am till Friday-9pm')

def main():
    c1 = company()
    print(c1.companyname)
    print(c1.Noofemployees)
    print(c1.cafeteria)
    c1.company_location()
    c1.company_salary()
    c1.company_cafeteria()
    c1.company_opening()

if __name__ == '__main__':
    main()


class FootBaller:
    def __init__(self,name,team,goals) -> None:
        self.name = name
        self.team = team
        self.goals = goals
    
    def shooting(self):
        print(self.name,'is shooting')

    def passing(self):
        print(self.name,'is passing')

    def runnning(self):
        print(self.name,'is running')

    def display(self):
        print(self.name)
        print(self.goals)
        print(self.team)
        print(self.age)
        print(self.jersey_no)
def main():
    cr = FootBaller('Christiano','Juventis',780)
    #cr.shooting()
    #cr.runnning()
    #cr.passing()
    setattr(cr,'age',35) #creating instance variables after creating object
    setattr(cr,'jersey_no',7) #creating instance variables after creating object
    print(getattr(cr,'name')) #To get names or anything
    cr.display() #calling instance method using display() function
    cr.passing()
    cr.runnning()
    cr.shooting()
 

    messi = FootBaller("Leonl Messi","Barcelona",999)
    #print(messi.name)
    #print(messi.goals)
    #print(messi.team)
    messi.display()     #calling instance method using display() function
    messi.passing()
    messi.runnning()
    messi.shooting()
    setattr(messi,'age',37)     #creating instance variables after creating object
    setattr(messi,'jersey_no',9)  #creating instance variables after creating object

if __name__ == '__main__':
    main()
        

    
        
