def rec_fact(n):
    if n<0:
        return n
    elif n==1 or n==0:
        return 1 
    else:
        return n*rec_fact(n-1)
print(rec_fact(3))