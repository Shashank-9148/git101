#Chain map: ** is used to merge dictionaries
#program is based on without using chain map

clothes = {'shirts':100,'pants':29,'blazers':89}
ele = {'mobiles':150,'computers':90,'ac':78}
food = {'milk':200,'chips':180,'biscuit':290}

inv = {**clothes,**ele,**food}
print(inv)
inv["shirts"] = 95
print(inv)
print(clothes)

#program using chain map
from collections import ChainMap
clothes = {'shirts':100,'pants':49,'blazers':89}
ele = {'mobiles':67,'computers':80,'ac':65}
food = {'milk':39,'chips':76,'biscuit':67}

inv = ChainMap(clothes,ele,food)
print(inv)
inv['shirts']=999
print(inv)
print(clothes)


#counter class
#program to print no of occurances 

from collections import Counter
s = 'mississippi'
c = Counter(s)
print(c)


#program to print most number of occurances and most common

from collections import Counter
c = Counter(['a','a','b','c','b','c','b','b','a'])
print(c.most_common())

#program to print all elements
from collections import Counter
c = Counter(['a','b','b','c','b','a','b','a','c'])
print(list((c.elements())))

#program to add,sub,union,intersection elements (we can operate sub,union,intersection)
from collections import Counter
c1 = Counter(a=2,b=4,c=6)
c2 = Counter(a=3,b=5,c=8)
c3 = c1+c2
print(c3)


#Named tuple class
#program to print student names and values
from collections import namedtuple
S = namedtuple('student',('name','age','stream','avg'))
S1 = S('alex',22,'cs',78)
print(S1)

#Deque class
from collections import deque
dq = deque([10,20,30,40])
dq.append(50)
dq.appendleft(99)
print(dq)