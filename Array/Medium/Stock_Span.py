l=[100,80,60,70,60,75,85]
n=len(l)
for i in range(n-1):
    if i==0:
        print(i+1,end=" ")
    else:
        if l[i+1]<l[i]:
            print(1,end=" ")
        else:
            print(i+1,end=" ")

