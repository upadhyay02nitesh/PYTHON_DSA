#      *
#     ***
#    *****
#   *******
#  *********

# n=5
# for i in range(1,n+1):
#     print((n-i)*" ",(2*i-1)*"*")

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()


#  *********
#   *******
#    *****
#     ***
#      *



#      *
#     ***
#    *****
#   *******
#  *********
#  *********
#   *******
#    *****
#     ***
#      *
n=5
for i in range(1,n+1):
    print(" "*(n-i),"*"*(2*i-1))
for i in range(n,-1,-1):
    print(" "*(n-i),"*"*(2*i-1))


# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()
# for i in range(n,-1,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()



#      *
#     **
#    ***
#   ****
#  *****
#  *****
#   ****
#    ***
#     **
#      *
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i),"*"*(i))
# for i in range(n,-1,-1):
#     print(" "*(n-i),"*"*(i))



# n=5
# for i in range(1,n+1):
    # for j in range(n-i):
        # print(" ",end="")
    # for j in range(i):
        # print("*",end="")
    # print()
# for i in range(n,-1,-1):
    # for j in range(n-i):
        # print(" ",end="")
    # for j in range(i):
        # print("*",end="")
    # print()






 
# *
# **
# ***
# ****
# *****
# *****
# ****
# ***
# **
# *

# n=5
# for i in range(1,n+1):
#     print("*"*(i))
# for i in range(n,-1,-1):
#     print("*"*(i))

# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#     print()
# for i in range(n,-1,-1):
#     for j in range(i):
#         print("*",end="")
#     print()




# 0 
# 1 0
# 0 1 0
# 1 0 1 0
# 0 1 0 1 0

# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         if (i+j)%2==0:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()





# 1      1
# 12    21
# 123  321
# 12344321

# n=4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     for j in range((n-i)*2):
#         print(" ",end="")
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()


