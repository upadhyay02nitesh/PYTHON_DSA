def missing_number(n,s):
    actual_sum=(n*(n+1))//2
    solu_sum=sum(s)
    return actual_sum-solu_sum
    

if __name__=="__main__":
    n=int(input("Enter how mny element you :"))
    s=list(map(int,input("Enter element in space ").split()))
    print(missing_number(n,s))