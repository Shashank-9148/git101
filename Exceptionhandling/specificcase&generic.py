print('Execution started normally')
lst = [10,20,0,40,50]
d = {1:'c',2:'Java',3:'Python',4:'C++'}

try:
    r = int(input('Enter the rank of the language: \n'))
    print(d[r])
    num = int(input('Enter the index numerator: \n'))
    den = int(input('Enter the index denominator: \n'))
    print(lst[num]/lst[den])

except KeyError: #we can use it as except keyerror as e
    print('Key does not exist')

except IndexError :#we can use it as except Indexerror as e
    print('Index out of range')

except ZeroDivisionError:#we can use it as except zerodivisionerror as e
    print('Division by zero')

except:#we can use it as exception as e
    print('Hey some issue occured')

    print('Execution terminated normally')



#Exception handling mechanism when multiple methods calls are involved
def fun2():
    print('fun2() started execution')
    num = int(input('Enter the numerator'))
    den = int(input('Enter the denominator'))
    res = num/den
    print(res)
    print('fun2() finished execution normally')

def fun1():
    print('fun1() started execution')
    fun2()
    print('fun1() finished execution')

def main():
    print('main()started execution')
    fun1()
    print('main()finished execution')

main()

#example
def fun2():
    print('fun2() started execution')
    try:
       num = int(input('Enter the numerator'))
       den = int(input('Enter the denominator'))
       res = num/den
       print(res)
    except ZeroDivisionError:
        print('Exception handled in fun2')
        
    print('fun2() finished execution normally')

def fun1():
    print('fun1() started execution')
    fun2()
    print('fun1() finished execution')

def main():
    print('main()started execution')
    fun1()
    print('main()finished execution')

main()


#example
print('Execution started normally')
lst = [10,20,0,40,50]
d = {1:'c',2:'Java',3:'Python',4:'C++'}

try:
    r = int(input('Enter the rank of the language: \n'))
    print(d[r])
    num = int(input('Enter the index numerator: \n'))
    den = int(input('Enter the index denominator: \n'))
    print(lst[num]/lst[den])

except KeyError as e: #we can use it as except keyerror as e
    print(e)

except IndexError as e :#we can use it as except Indexerror as e
    print(e)

except ZeroDivisionError as e:#we can use it as except zerodivisionerror as e
    print(e)

except Exception as e:#we can use it as exception as e
    print(e)

    print('Execution terminated normally')

