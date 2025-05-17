# n=153
# temp=n 
# su=0
# lt=len(str(n))
# while temp>0:
#     s=temp%10 
#     su=su+s**lt 
#     temp//=10 
# print(su)

for i in range(10,1000):
    temp=i 
    v=0
    while temp>0:
        s=temp%10
        v=v+s**(len(str(i)))
        temp//=10
    if i==v:
        print(i,end=" ")

