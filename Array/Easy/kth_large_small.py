def kth_large_small(l,k):
    l.sort()
    n=l[-k]
    m=l[k-1]
    return n,m


l=[1,2,9,3,4,5,0]
k=2
l,s=kth_large_small(l,k)
print(k,"Large",l)
print(k,"Small",s)