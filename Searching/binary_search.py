def binary_search(l,s,start,end):
    l.sort()
    while start<=end:
        mid=(start+end)//2 
        if l[mid]==s:
            return mid
        elif l[mid]>s:
            end=mid-1
        else:
            start=mid+1 
    return -1
l=[3,4,5,2,1]
s=5
b=binary_search(l,s,0,len(l))
if s!=-1:
    print(s,"is Find on",b,"Position in this list")
else:
    print(s,"IS Not Find")



# when we sort l=[1,2,3,4,5],start=0,end=5,s=5

# mid(0+5)//2=2   if l[2]=(3)==5  false  5  3<5 start=2+1=3
# mid(3+5)//2=4    if l[4]==5  True   then return mid that is 4
