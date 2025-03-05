import Modules.mymodule as mymodule
mymodule.add()
mymodule.sub()
mymodule.mul()

import Modules.mymodule as mm
mm.add()
mm.sub()
mm.mul()

from Modules.mymodule import*
add()
sub()
mul()

from Modules.mymodule import add,sub
add()
sub()


import Modules.mymodule as mymodule
#help(mymodule)
#help(mymodule.power_of)
help(mymodule.get_quotient)

#print(mymodule.power_of.__doc__)
print(mymodule.get_quotient.__doc__)





import Modules.mymodule as mymodule 
def get_remainder(num,den):
    '''This function calculates the remainder of num/den'''

    rem = num%den
    print(rem)

get_remainder(100,6)
mymodule.power_of(2,5)
mymodule.get_quotient(100,2)
