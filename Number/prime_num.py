
# def prime_num(n):

#     for i in range(2,n):
#         if n%i==0:
#             break

#     else:
#         return True
#     return False
    
# n=11
# s=prime_num(n)
# if s==True:
#     print("Prime")
# else:
#     print("Not Prime")

# s=0
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        # s+=1
        print(i,end=" ")
# print()
# print(s)