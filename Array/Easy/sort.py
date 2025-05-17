def Quick_sort(l):
    if len(l)<=1:
        return l 
    else:
        lower=[]
        higher=[]
        pivot=l.pop()
        for i in l:
            if i>pivot:
                higher.append(i)
            else:
                lower.append(i)
        return Quick_sort(lower)+[pivot]+Quick_sort(higher)



l=[2,4,1,6,2,4,3]
q=Quick_sort(l)
print(q)
