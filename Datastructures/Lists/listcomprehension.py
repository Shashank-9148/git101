'''#program to find square number in lst
lst = [2,3,5,7,8,10,12]
sq_lst = []
for i in lst:
    sq_lst.append(i**2)
    if i%2==0:
print(lst)
print(sq_lst)'''

#using lists comprehension  syntax[expression , for item in list ,if condition]
                                  #[what I want, from which loop , on what condition]
lst = [2,3,4,5,10,11]
sq_lst = [i**2 for i in lst]
print(sq_lst)

#using condition
lst = [2,3,4,6,8,10,12]
sq_lst = [i**2 for i in lst if i%2 == 0]
print(sq_lst)