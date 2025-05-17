n=145
temp=n 
v=0

def fact(n):
    if n==0:
        return 1
    else:
        res=1
        for i in range(1,n+1):
            res=res*i 
        return res
while temp>0:
    s=temp%10
    v=v+fact(s)
    temp//=10
if v==n:
    print("strong")
else:
    print("not strong")