import logging
def sum_even(lst):
    logging.info('sum_even() started execution')
    sum = 0
    for i in lst:
        if i%2 == 0:
            sum += i
    logging.info('sum_even() finished execution')
    return sum

def main():
    logging.basicConfig(filename='Log.txt',level=logging.INFO)
    logging.info('main()started execution')
    lst = list(map(int,input().split()))
    logging.info('input taken from user')
    logging.info('calling sum_even()')
    res = sum_even(lst)
    logging.info('result of sum_even() collected')
    print(res)
    logging.info('main() finished execution')   
main()

#level debugging
import logging
def add(x,y):
    return x+y
def mul(x,y):
    return x*y
def sub(x,y):
    return x-y
def div(x,y):
    return x/y

def main():
    logging.basicConfig(filename='log.txt',level=logging.DEBUG)
    a = int(input())
    b = int(input())
    res1 = add(a,b)
    logging.debug(f'res1={res1}')
    res2 = mul(a,b)
    logging.debug(f'res2={res2}')
    res3 = sub(a,b)
    logging.debug(f'res3={res3}')
    res4 = div(a,b)
    logging.debug(f'res4={res4}')
main()


#level warning
import logging
logging.basicConfig(filename='log.txt',level=logging.WARNING)
def validate(mob):
    if len(mob) == 10:
        print('mobile number is validated')
    else:
        print('invalid mobile number')
        logging.warning('invalid mobile number')
def main():
    num = input('enter mobile number :')
    validate(num)
main()



#level warning
import logging
logging.basicConfig(filename='log.txt',level=logging.ERROR,filemode='w')
def div():
    try:
     num = int(input())
     den = int(input())
     q = num/den
     print(q)
    except:
       logging.error('exception occured',exc_info= True)
def main():
    div()
main()


#code for implementing time,file,message in logger file 
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