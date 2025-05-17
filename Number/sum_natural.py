def sum_natural(n):
    if n==1:
        return 1
    else:
        return n+sum_natural(n-1)
print(sum_natural(5))


# f(5)= n>1  5+f(4)
#              4+f(3)
#                3+f(2)
#                  2+f(1)
#                     1
# 1+2+3+4+5=15

#n natural odd num sum 

def sum_natural(n):
    if n==1:
        return 1
    else:
        return (2*n-1)+sum_natural(n-1)
print(sum_natural(5))


#n natural even num sum 

def sum_natural(n):
    if n==1:
        return 1
    else:
        return (2*n)+sum_natural(n-1)
print(sum_natural(5))

#n natural square num sum 

def sum_natural(n):
    if n==1:
        return 1
    else:
        return (n**2)+sum_natural(n-1)
print(sum_natural(5))