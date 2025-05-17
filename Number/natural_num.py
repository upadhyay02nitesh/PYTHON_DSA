# #base case
# n=12
# for i in range(1,n+1):
#     print(i,end=" ")


#recursive  case
def rec_num(n):
    if n>0:
        rec_num(n-1)
        print(n,end=" ")
rec_num(12)


# lets understand
# n=3
# n>0
#     f(3)
#         f(2)
#             f(1) break (0>0 false )
# output 1,2,3


print()


# #base case reverse way
# n=12
# for i in range(n,0,-1):
#     print(i,end=" ")


# #recursive  case reverse manner
# def rec_num(n):
#     if n>0:
#         print(n,end=" ")
#         rec_num(n-1)
# rec_num(12)

# lets understand 
# n=3
# n>0
#     print(3)
#     f(2)
#         print(2)
#         f(1)
#             print(1)
#             f(0)-false
# output-3,2,1


# # recursive case for odd natural num 
# def rec_num(n):
#     if n>0:
#         rec_num(n-1)
#         print(2*n-1,end=" ")
# rec_num(12)

# # recursive case for odd natural num reverse 
# def rec_num(n):
#     if n>0:
#         print(2*n-1,end=" ")
#         rec_num(n-1)
# rec_num(12)


# # recursive case for even natural num 
# def rec_num(n):
#     if n>0:
#         rec_num(n-1)
#         print(2*n,end=" ")
# rec_num(12)

# # recursive case for evem  natural num reverse 
# def rec_num(n):
#     if n>0:
#         print(2*n,end=" ")
#         rec_num(n-1)
# rec_num(12)

# # # recursive case for square natural num 
# def rec_num(n):
#     if n>0:
#         rec_num(n-1)
#         print(n**2,end=" ")
# rec_num(12)

# # recursive case for even square natural num 
# def rec_num(n):
#     if n>0:
#         rec_num(n-1)
#         print((2*n)**2,end=" ")
# rec_num(12)


# recursive case for odd square natural num 
# def rec_num(n):
#     if n>0:
#         rec_num(n-1)
#         print((2*n-1)**2,end=" ")
# rec_num(12)
