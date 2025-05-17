l=[2,3,4,-4,-3,2,3,4,5,6,7,-10]

# When we sort then all egative value will shift to left side
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l)