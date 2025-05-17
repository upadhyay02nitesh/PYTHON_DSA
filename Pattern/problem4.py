# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********

# n=5
# for i in range(2*n):
#     if i<n:
#         for j in range(n-i):
#             print("*",end="")
    
#         for j in range(2*i):
#             print(" ",end="")

#         for j in range(n-i):
#             print("*",end="")
#         print()
#     else:
#         for j in range(i-n+1):
#             print("*",end="")

#         for j in range(2*(n-(i-n)-1)):  # 8 6 4 2 0
#             print(" ",end="")
#         for j in range(i-n+1):
#             print("*",end="")
#         print()



# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

# n=5
# for i in range(1,2*n+1):
#     if i<n+1:
#         for j in range(i):
#             print("*",end="")
#         for j in range(2*(n-i)):
#             print(" ",end="")
#         for j in range(i):
#             print("*",end="")
#         print()
#     else:
#         for j in range(2*n-i):
#             print("*",end="")
#         for j in range(2*(i-n)):
#             print(" ",end="")
#         for j in range(2*n-i):
#             print("*",end="")
#         print()


# ****
# *  *
# *  *
# ****

# n=4
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()




# 4 4 4 4 4 4 4 
# 4 3 3 3 3 3 4
# 4 3 3 3 3 3 4
# 4 3 3 3 3 3 4
# 4 3 3 3 3 3 4
# 4 3 3 3 3 3 4 
# 4 4 4 4 4 4 4

# n=4
# for i in range(2*n-1):
#     for j in range(2*n-1):
#         if i==0 or i==2*n-2 or j==0 or j==2*n-2:
#             print(n,end=" ")
#         else:
#             print(n-1,end=" ")
#     print()


# *******
#  *****
#   ***
#    *
#    *
#   ***
#  *****
# *******


# n=4
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()




#         1 
#       1 2
1#     1 2 3
#   1 2 3 4
# 1 2 3 4 5

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(' ',end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()



# 1 
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

# n=5
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

# 5 4 3 2 1 
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1
        
# n=5
# for i in range(n):
#     for j in range(n,0,-1):
#         print(j,end=" ")
#     print()
        



# 1                 1 
# 1 2             1 2
# 1 2 3         1 2 3
# 1 2 3 4     1 2 3 4
# 1 2 3 4 5 1 2 3 4 5

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     for j in range(2*(n-i)):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
    
#     print()



# 1 2 3 4 5 5 4 3 2 1 
#   1 2 3 4 4 3 2 1
#     1 2 3 3 2 1
#       1 2 2 1
#         1 1


# n=5
# for i in range(n,-1,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     for j in range(i,0,-1):
#         print(j,end=" ")
    

#     print()


#         1 1 
#       1 2 2 1
#     1 2 3 3 2 1
#   1 2 3 4 4 3 2 1
# 1 2 3 4 5 5 4 3 2 1

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()


#         1 1 
#       1 2 2 1
#     1 2 3 3 2 1
#   1 2 3 4 4 3 2 1
# 1 2 3 4 5 5 4 3 2 1
# 1 2 3 4 5 5 4 3 2 1
#   1 2 3 4 4 3 2 1
#     1 2 3 3 2 1
#       1 2 2 1
#         1 1

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

# 5 5 5 5 5 
#  4 4 4 4
#   3 3 3
#    2 2
#     1

# n=5
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
