def long_subsequence(l,n):
    n_set=set(l)
    longest=0
    for i in l:
        if (i-1) not in n_set:
            # print("Enter element who doesnot have prev value",i)
            # means we have not previous element this is start point
            length=0
            while(i+length) in n_set:
                # print(i+length)
                length+=1
            if length>longest:
                longest=length
            # print("longest:",longest)
    return longest

    


n=int(input("Enter the Number of the input : "))
l=list(map(int,input("Enter Element in one line with space ").split()))[:n]
if __name__=="__main__":
    print(long_subsequence(l,n))