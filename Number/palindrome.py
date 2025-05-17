n=121
temp=n 
v=0
while temp>0:
    s=temp%10 
    v=v*10+s 
    temp//=10
if v==n:
    print("Palindrome")
else:
    print("not palindrome")
