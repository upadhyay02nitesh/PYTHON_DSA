def nth_small(l,k):
    l.sort()
    return l[k-1]

n=int(input("Enter the Number of the input : "))
k=int(input("Enter the smallest value  : "))
l=list(map(int,input("Enter Element in one line with space ").split()))[:n]
if __name__=="__main__":
    print(k,"th smallest value :",nth_small(l,k))