# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# n=5
# s=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(s,end=" ")
#         s+=1
#     print()


# A 
# A B
# A B C
# A B C D
# A B C D E

# def numtochar(num):
#     return chr(num+65)
# n=5
# for i in range(n+1):
#     for j in range(i):
#         print(numtochar(j),end=" ")

#     print()


# A B C D E 
# A B C D
# A B C
# A B
# A

# def numtochar(num):
#     return chr(num+65)
# n=5
# for i in range(n,-1,-1):
#     for j in range(i):
#         print(numtochar(j),end=" ")

#     print()




# A 
# B B
# C C C
# D D D D
# E E E E E

# def numtochar(num):
#     return chr(num+65)
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(numtochar(i),end=" ")

#     print()


#    A
#   ABC
#  ABCDE
# ABCDEFG

# def numtochar(num):
#     return chr(num+65)
# n=4
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print(numtochar(j),end="")

#     print()


#    A
#   ABA
#  ABCBA
# ABCDCBA

# def numtochar(num):
#     return chr(num+65)
# n=4
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i-1):
#         print(numtochar(j),end="")
#     for j in range(i-1,-1,-1):
#         print(numtochar(j),end="")

#     print()




# E 
# D E
# C D E
# B C D E
# A B C D E

# def numtochar(num):
#     return chr(num+65)
# n=5
# for i in range(1,n+1):
#     for j in range(i-1,-1,-1):
#         print(numtochar(n-j-1),end=" ")
  
#     print()


