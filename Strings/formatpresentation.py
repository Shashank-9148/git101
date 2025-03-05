import math
s = "{}".format(math.pi)
print(s)

import math
s = "{0:.4f}".format(math.pi)
print(s)

import math
s = "{0:10.4f}".format(math.pi)
print(s)

import math
s = "{0:010.5f}".format(math.pi)
print(s)


#exponent presentation
ew = 597600000000000000000000
s = "{0:e}".format(ew)
print(s)


ew = 12345600000
s = "{0:.2e}".format(ew)
print(s)


#accessing lists in tuples
s = "{}".format([10,20,30])
print(s)


s = "{0},{1},{2}".format(*[10,20,30])
print(s)

#program to find the average of given number
from functools import reduce
nums = input("enter the number\n").split()
l = list(map(int,nums))
res = reduce(lambda x,y:x+y,l)
avg = res/len(l)
print("{0:^14.4f}".format(avg))

