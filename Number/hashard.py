n=21
s=0
temp=n 
while temp>0:
    r=temp%10
    s+=r 
    temp//=10
if n%s==0:
    print("Harshad Number")
else:
    print("Not Harshad Number")
