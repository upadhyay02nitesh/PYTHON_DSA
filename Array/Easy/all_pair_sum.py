def get_sum(l,n,s):
    
    get_sum=s
    c=0
    for i in range(n):
        for j in range(i+1,n):
            cur_sum=l[i]+l[j]
            # print("Current sum",cur_sum)
            if cur_sum==get_sum:
                c+=1
                print(i,j) 
    return c



n=int(input("Enter the Number of the input : "))
s=int(input("Enter the Number of sum : "))
l=list(map(int,input("Enter Element in one line with space ").split()))[:n]
if __name__=="__main__":
    print(get_sum(l,n,s))