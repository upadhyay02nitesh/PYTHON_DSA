l=[1,5,7,-1]
k=6
n=len(l)
c=0
for i in range(n):
    for j in range(i+1,n):
        if l[i]+l[j]==k:
            c+=1
            print(l[i],l[j])
# print(c)