
def sum_zero_subarray(l,n):
    s=[]
    
    for i in range(n):
        curr_sum=l[i]
        for j in range(i+1,n):
            curr_sum+=l[j]
            if curr_sum==0:
                s.append((i,j))
                
    return s    





n=int(input("Enter the Number of the input : "))

l=list(map(int,input("Enter Element in one line with space ").split()))[:n]
if __name__=="__main__":
    
    print(sum_zero_subarray(l,n))