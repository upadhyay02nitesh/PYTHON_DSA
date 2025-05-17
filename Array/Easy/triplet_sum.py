def get_sum(l,n,s):
    

    get_sum=s
    for i in range(n):
    # i+1 (never similar because some cases i and j will similar to give result)
        for j in range(i+1,n):
            cur_sum=l[i]+l[j]
            for k in range(j+1,n):
                cur_sum+=l[k]
                if cur_sum==get_sum:
                    return True



n=int(input("Enter the Number of the input : "))
s=int(input("Enter the Number of sum : "))
l=list(map(int,input("Enter Element in one line with space ").split()))[:n]
if __name__=="__main__":
    print(get_sum(l,n,s))