#program for  string slicing 3
s = input("enter a string\n")
for i in range (0,len(s)-2):
    print(s[i:i+3])


#program for string to slice first and last character
s = input("enter a string\n")
print(s[1:len(s)-1])

#program for reverse string slicing excluding first and last character
s = input("enter a string\n")
print(s[len(s)-2:0:-1])

#program for a string to check its palindrome or not
s = input("enter a string\n")
if s == s[::-1]:
    print(s,"its a palindrome ")
else:
    print(s,"its not palindrome")

#comparision program
s1 = "python"
s2 = "java"

if id(s1) == id(s2):
    print("the references are equal")
else:
    print("the references are unequal")

#comparision program
s1 = "python"
s2 = "python"

if id(s1) == id(s2):
    print("the references are same")
else:
    print("the references are not same")

#comparision program
s1 = "python"
s2 = "PYTHON"

if id(s1) == id(s2):
    print("string references are same")
else:
    print("string references are not same")


#program to reverse a second half of the string
s = input("enter a string\n")
print(s[:len(s)//2:] + s[len(s)-1:(len(s)//2)-1:-1])

#program to count the number of lower case,uppercase,numbers and special characteristics present in a string
s = input("enter a string\n")
low_count,up_count,sp_count,num_count = 0,0,0,0

for i in s:
    if i.islower():
        low_count += 1
    elif i.isupper():
        up_count += 1
    elif i.isnumeric():
        num_count += 1
    else:
        sp_count += 1

    print("lower case=",low_count)
    print(" upper case=",up_count)
    print(" numeric=",num_count)
    print(" spl=",sp_count)

