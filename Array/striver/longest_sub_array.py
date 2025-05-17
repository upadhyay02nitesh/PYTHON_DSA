def long_subarray(n,s,k):
    cum_sum=0
    max_len=0
    cum_map={}
    for i in range(n):
        cum_sum+=s[i]
        if cum_sum not in cum_map:
            cum_map[cum_sum]=i 
            
            # print(cum_map) 
        # print(cum_sum)
        if cum_sum==k:
            max_len=i+1
            # print(max_len)
        if (cum_sum-k) in cum_map:
            max_len=max(max_len,i-cum_map[cum_sum-k])
            # print(max_len)
        
    return max_len


    
if __name__=="__main__":
    n=int(input("Enter how mny element you : "))
    k=int(input("Enter sum : "))
    s=list(map(int,input("Enter element in space ").split()))
    print(long_subarray(n,s,k))