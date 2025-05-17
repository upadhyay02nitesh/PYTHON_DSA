# # *****
# # *****
# # *****
# # *****
# # *****
# n=5
# for i in range(n):
#     print("*"*n)

# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print()


# # *
# # **
# # ***
# # ****
# # *****


# n=5
# for i in range(1,n+1):
#     print("*"*i)

# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end="")
#     print()



# 1
# 12
# 123
# 1234
# 12345
# # n=5
# # for i in range(1,n+1):
# #     for j in range(1,i+1):
# #         print(j,end="")
# #     print()



# 1
# 22
# 333
# 4444
# 5555

# # n=5
# # for i in range(1,n+1):
# #     for j in range(1,i+1):
# #         print(i,end="")
# #     print()




# *****
# ****
# ***
# **
# *

# # n=5
# # for i in range(n,-1,-1):
# #     for j in range(i):
# #         print("*",end="")
# #     print()


# 12345
# 1234
# 123
# 12
# 1

n=5
for i in range(n,-1,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()




