# n=210
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=" ")


# Prime Factor
n=210
for i in range(2,n):
    if n%i==0:
        print(i,end=" ")
        n=n//i
