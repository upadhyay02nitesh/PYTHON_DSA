def max_min_diff(l,n,k):
    
    l.sort()
    min_val=l[0]+k
    max_val=l[n-1]-k
    diff=max_val-min_val
    for i in range(1,n):
        if l[i]-k<0:
            continue
        min_val=min(min_val,l[i]-k)
        max_val=max(max_val,l[i-1]+k)
        diff=min(diff,max_val-min_val)
    return diff


         


n=int(input("Enter the Number of the input : "))
k=int(input("Enter the Number of the input : "))
l=list(map(int,input("Enter Element in one line with space ").split()))[:n]
if __name__=="__main__":
    print(max_min_diff(l,n,k))