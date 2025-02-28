#remove,add,discaed operations
s = {1,2,3,4,5}
print(s)
s.add(9)
print(s)
s.remove(2)
print(s)
s.update({0,10,18})
print(s)
s.discard(18)
print(s)

#set operation using union (s1.union(s2) or s1|s2)
s1 = {1,2,3,4,5,6,7,8}
s2 = {5,6,7,8,12,13,14,15}
s3 = s1|s2
print(s1)
print(s2)
print(s3)


#set operation using intersection s1&s2
s1 = {1,2,3,4,5,9,0}
s2 = {1,2,3,5,10,13,15}
s3 = s1&s2
print(s1)
print(s2)
print(s3)


#set operation using difference(s1 - s2)
s1 = {1,2,3,5,7,9,11,13}
s2 = {5,7,9,90,57,38}
s3 = s1-s2
print(s3)

#set operation using symmetric difference(s1^s2 or s1.symmetric(s2))
s1 = {1,2,3,4,5,6,7}
s2 = {1,2,3,4,9,99,78}
s3 = s1^s2
print(s3)

#To update sets present in s2
s1 = {1,2,3,4,5,6}
s2 = {1,2,3,9,10,11}
print(s1)
print(s1.intersection_update(s2))
print(s1)

s1 = {1,2,3,4,5,6}
s2 = {1,2,3,9,10,11}
print(s1)
print(s1.difference_update(s2))
print(s1)

s1 = {1,2,3,4,5,6}
s2 = {1,2,3,9,10,11}
print(s1)
print(s1.symmetric_difference_update(s2))
print(s1)

#To check subsets
#s2 is a subset of s1
s1 = {1,2,3,4,6,9,11}
s2 = {11,9,6,1}
print(s2<=s1)
print(s2.issubset(s1))

#To check superset
s1 = {1,2,3,4,6,9,11}
s2 = {11,9,6,1}
print(s1>=s2)
print(s1.issuperset(s2))

#To check disjoint
s1 = {13,15,78,98,20}
s2 = {45,62,64,90,99}
print(s1.isdisjoint(s2))
