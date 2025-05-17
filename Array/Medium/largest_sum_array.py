l=[5,4,1,7,8]
n=len(l)
max=0
for i in range(n):
    sum=l[i]
    for j in range(i+1,n):
        sum+=l[j]
        if sum>max:
            max=sum 
        
print(max)
