name = input("enter the string\n")
place = input("enter the string\n")

s = "Hello{},How's the weather in{}?".format(name,place)
print(s)


s = "{} {} {}".format(20,3,5)
print(s)

s = "{2} {0} {1}".format(25,40,55)
print(s)
 
#left aligning
s = "{0:*<10}".format(20)
print(s)

#right aligning
s = "{0:*>10}".format(30)
print(s)

#centre aligning
s = "{0:*^10}".format(40)
print(s)


s = "{0:*<5}".format(20,30)
print(s)


