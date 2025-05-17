def max_sum(l,n):
    max_sum=l[0]
    cur_sum=l[0]
    for i in range(1,n):
        cur_sum+=l[i]
        # print(cur_sum)
       
        if cur_sum>max_sum:
            max_sum=cur_sum

    return max_sum


n=int(input("Enter the Number of the input : "))
l=list(map(int,input("Enter Element in one line with space ").split()))[:n]
if __name__=="__main__":
    print(max_sum(l,n))