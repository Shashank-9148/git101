#using raise (Value Error)
def validate(mob):
    if len(mob) == 10:
        print('valid mobile number')
    else:
        raise ValueError
    
def main():
    mob = input()
    validate(mob)
main()

#Name Error
def menu(item):
    if item == 'Pizza':
        print('Enjoy your pizza')
    elif item == 'idli':
        print('Enjoy your idli')
    elif item == 'burger':
        print('Enjoy your burger')
    else:
        raise NameError
    
def main():
    item = input()
    menu(item)
main()

#using Finally:
def fun():
    print('fun() started execution')
    try:
        num = int(input('Enter the numerator:'))
        den = int(input('Enter the denominator'))
        res = num/den
        print(res)

    except ZeroDivisionError as e:
        print('Exception handled in fun() ')
        raise e
    
    finally:
        print('fun() finished execution normally ')

def main():
    print('main() started execution')
    try:
        fun()
    except:
        print('Exception handled in main()')
    print('main() finished execution normally')

main()