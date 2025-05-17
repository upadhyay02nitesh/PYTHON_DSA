def max_min(l):
    max=0
    min=l[0]
    for i in l:
        if i>max:
            max=i
        if i<min:
            min=i
    return max,min
l=1,2,3,4,5
m,n=max_min(l)
print("Max",m)
print("Min",n)