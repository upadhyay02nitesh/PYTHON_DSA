def most_ones(n,s):
    curr=0
    max_curr=0
    for i in s:
        if i==1:
            curr+=1
            # print(curr)
            if curr>max_curr:
                max_curr=curr
        else:
            curr=0
            # print(curr)
    
    return max_curr

if __name__=="__main__":
    n=int(input("Enter how mny element you : "))
    s=list(map(int,input("Enter element in space ").split()))
    print(most_ones(n,s))