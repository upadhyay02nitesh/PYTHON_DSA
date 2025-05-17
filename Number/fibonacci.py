def fibo(n):
    if n<=0:
        return n 
    elif n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo(5))
    

n=5
a,b=0,1
for i in range(n):
    print(a,end=" ")
    temp=a 
    a=b 
    b=temp+b