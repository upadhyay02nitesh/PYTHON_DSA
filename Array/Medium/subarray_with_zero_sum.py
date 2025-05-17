l=[4,2,-1,1,6,0]
n=len(l)
for i in range(n):
    s=l[i]
    if s==0:
        print("0 find in index of ",i)
    for j in range(i+1,n):
        s+=l[j]
        if s==0:
            print("0 find in index between",i,"and",j)
       
        
