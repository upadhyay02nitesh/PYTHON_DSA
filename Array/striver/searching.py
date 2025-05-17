def searching(n,k,s):
    p=0
    q=n-1
    mid=(p+q)//2
    while p<=q:
        if s[mid]==k:
            return mid 
        elif s[mid]>k:
            q=mid-1
        else:
            p=mid+1
    return False


if __name__=="__main__":
    n=int(input("Enter how mny element you :"))
    k=int(input("Enter searching  element : "))
    s=list(map(int,input("Enter element in space ").split()))
    s.sort()
    print(searching(n,k,s))