'''n = int(input("enter a number"))
if n%2==0:
    print("its even")
else:
    print("its odd")'''


'''a = int(input("enter 1 value"))
b = int(input("enter 2nd value"))
c = int(input("enter 3rd value"))

if a>b and a>c:
    print("a is greatest")
elif b>c:
    print("c is greatest")
else:
    print("c is greatest")'''


'''a = 25
if a%2==0 or a%5==0:
    print("a i divisible by either 2 or 5")
else:
    print("a is not divisible by  neither 2 nor 5")'''


'''n = int(input("enter a variable"))
if not n%2==0:
    print("its odd")
else:
    print("its even")'''


'''exp = input("enter expression")
res = eval(exp)
print(res)'''


'''
even_sum,odd_sum = 0,0
n = int(input("enter the variable"))
for i in range(1,n+1):
    if n%i==0:
        even_sum += i
        continue
    odd_sum += i
print("sum of all even numbers:",even_sum)
print("sum of all odd numbers:",odd_sum)'''



'''balance = 15000
min_balance = 2000

print("balance before transaction:",balance)
for i in range(5):
    
    balance = balance-1000
else:
    print("balance after transaction:",balance)'''



'''lst = input("Enter a list between[]\n")
lst = eval(lst)
start = int(input("Enter the start index"))
stop = int(input("Enter the stop index"))
print("sum=",sum(lst[start:stop+1]))



matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Original Matrix")
print(matrix)

# new nested list to store mirrormatrix
mirror_matrix = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]

# nested for loop to iterate through lists
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        mirror_matrix[j][i] = matrix[i][j]

print("Mirror Matrix")
print(mirror_matlrix)
'''
'''lst = []
res = ''.join(map(str,lst))
for i in range(21):
   for j in range(i):
    lst.append(i)
print(lst)'''


'''def fibonacci(n):
    list = []
    a, b = 0, 1  
    for i in range(n):
        list.append(a)  
        a, b = b, a + b  
    return list 
list = fibonacci(20)
print(list)'''

import logging
logging.basicConfig(filename='log.txt',level=logging.ERROR,filemode='w',format='%(levelname)s:%(name)s:%(asctime)s:%(filename)s:%(msg)s:')
def fun():
    lst = [0,20,30,40,50]
    d = {1:'c',2:'java',3:'python',4:'c++'}
    try:
        r = int(input('enter the rank of the language'))
        print(d[r])
        num = int(input('enter the index of the numerator'))
        den = int(input('enter the index of the denominator'))
        print(lst[num]/lst[den])
    except KeyError:
        print('key does not exist')
    except IndexError:
        print('index outof bounds')
    except ZeroDivisionError:
        print('division by zero')
    except:
        print('hey,some issue occured')
        logging.error('exception occured',exc_info=True)
def main():
    fun()
main()