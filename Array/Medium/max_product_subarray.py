l=[6,-3,-11,0,2]
n=len(l)
max=0
for i in range(n):
    multi=l[i]
    for j in range(i+1,n):
        multi*=l[j]
        if multi>max:
            max=multi
     
print(max)
