'''def pizza_toppings(toppings):
    print(toppings)

pizza_toppings("cheese")


def pizza_toppings(*toppings):
    print(toppings)

pizza_toppings("cheese")
pizza_toppings("cheese","onions","olives","corns")

def pizza_toppings(name,*toppings,crust):
    print(name)
    print(toppings)
    print(crust)
    print(type(toppings))

pizza_toppings("shashank","cheese","olive","deer","tiger",crust="fan")


def pizza_toppings(*toppings):
    print(toppings)
    pizza_toppings("cheese","pizza","toppings","olives")'''


'''def pizza_toppings(name,*toppings,crust):
    print(name)
    print(toppings)
    print(crust)
pizza_toppings("Rohit","cheese","corn","olives",crust="thin")'''



def collect_student_data(*data,crust):
    
    print(data)
    print(crust)
collect_student_data("rohith",35,89,"m",crust="male")


