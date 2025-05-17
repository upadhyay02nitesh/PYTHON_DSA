def rec_num(n):
    if n>0:
        rec_num(n-1)
        print(n**2,end=" ")
rec_num(12)