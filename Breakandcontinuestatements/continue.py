# even_sum,odd_sum = 0,0
# n = int(input("Enter the value of n\n"))
# for i in range (1,n+1):
#     if i%2==0:
#         even_sum += i
#     else:
#         odd_sum += i
# print("sum of all even numbers :",even_sum)
# print("sum of all odd numbers :",odd_sum)

lst = [1,2,3,4,5,6,7]
even = 0
odd = 0
for i in range(0,len(lst)):
    if lst[i]%2==0:
        even = even+1

    else:
        odd = odd+1

print("even sum",even)
print("odd sum",odd)
