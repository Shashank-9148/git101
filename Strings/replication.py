s = "PYTHON"
s_rep = s*4
print(s)
print(s_rep) 

#program to find binary,octal,hexadecimal number
s = int(input("enter the number\n"))
print(s)
print("{0:b}".format(s))
print("{0:o}".format(s))
print("{0:x}".format(s))


#format specifier
import math
name = "rohit"
place = "bengaluru"
print("{} {}".format(name,place))
print("{0:.3f}".format(math.pi))

# using F string instead of format
import math
name = "rohit"
place = "bengaluru"
print(f"{name} {place}")
print(f"{math.pi:.4f}")

#using raw form
name = "roh\nhit"
print(name)